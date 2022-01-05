from first_order_source import FirstOrderSource
from lzma_impl import LZMA
from hybrid_algorithm import HybridAlgorithm
from huffman import HuffmanCoding
from lzw import LZW
from arithmetic_coding import ArithmeticCoding
import utils
import json
import os
import shutil
import math

# creating a folder for un/compressed files.
WRITING_FILES_IS_ENABLED = False
here = os.path.dirname(os.path.abspath(__file__))

if WRITING_FILES_IS_ENABLED:
    FILEs_PATH = os.path.join(here, 'files')
    shutil.rmtree(FILEs_PATH, ignore_errors=True)
    os.mkdir(FILEs_PATH)



# loading (and then ordering) alphabets from the alphabets' file.
ALPHABETS_FILE_NAME = 'alphabets.json'

alphabets_path = os.path.join(here, ALPHABETS_FILE_NAME)
alphabets_file = open(alphabets_path)
ALPHABETS = utils.get_alphabets(json.load(alphabets_file))
alphabets_file.close()




SIZES = [ 1000, 5500 , 10000, 55000 ,100000 ]
#SIZES = [ 1000, 1200, 1400, 1600, 1800, 2000]

ALGORITHMS = [
    HybridAlgorithm([ HuffmanCoding() ]),
    HybridAlgorithm([ LZMA() ]),
    HybridAlgorithm([ HuffmanCoding(), LZMA() ]),
    HybridAlgorithm([ HuffmanCoding(), LZW() ]),
]

SOURCES = [ FirstOrderSource(alphabet) for alphabet in ALPHABETS ]

# 3-nested dictionary to store compression ratios,
# structured as follow:
#     Algorithms
#         Sources
#             Sizes 
performances = {
    str(algorithm) : {
        str(source) : {
            size : 0 
            for size in SIZES
        } 
        for source in SOURCES
    } 
    for algorithm in ALGORITHMS
}

INFO_SEP = "___"

for alphabet in ALPHABETS:
    source = FirstOrderSource(alphabet)

    for file_size in SIZES:
        text = source.generate_text(file_size)

        if WRITING_FILES_IS_ENABLED:
            # uncompressed file names will be in the form: source__size.txt
            file_name = f"{source}{INFO_SEP}{file_size}.txt"
            file_path = os.path.join(FILEs_PATH, file_name)

            with open(file_path, 'w') as file:
                file.write(text)

        for algorithm in ALGORITHMS:
            compr_text = algorithm.compress(text)

            if WRITING_FILES_IS_ENABLED:
                # compressed file names will be in the form: algorithm__source__size.txt
                compr_file_name = f"{algorithm}{INFO_SEP}{file_name}"
                compr_file_path = os.path.join(FILEs_PATH, compr_file_name)

                with open(compr_file_path, 'w') as compr_file:
                    compr_file.write(compr_text)
                    compr_ratio = utils.compression_ratio_from_file(file_path, compr_file_path)
            else:
                compr_ratio = utils.compression_ratio(text, compr_text)

            performances[str(algorithm)][str(source)][file_size] = compr_ratio


# correct huffman based algorithm compression ratios.
huffman = "Huffman"
huffman_lzma = "Huffman_LZMA"
huffman_lzw = "Huffman_LZW_nbit:10"
ALPHABETS_SIZE = len(ALPHABETS[0])
huffman_factor = math.ceil(math.log(ALPHABETS_SIZE, 2))

performances = utils.update_performances(performances, huffman, huffman_factor)
performances = utils.update_performances(performances, huffman_lzma, huffman_factor)
performances = utils.update_performances(performances, huffman_lzw, huffman_factor)


utils.print_performances(performances)

# saving performances to "output.json"
OUTPUT_FOLDER_NAME = "output"

OUTPUT_FOLDER_PATH = os.path.join(here, OUTPUT_FOLDER_NAME)
shutil.rmtree(OUTPUT_FOLDER_PATH, ignore_errors=True)
os.mkdir(OUTPUT_FOLDER_PATH)


OUTPUT_FILE_NAME = "output.json"

OUTPUT_FILE_PATH = os.path.join(OUTPUT_FOLDER_PATH, OUTPUT_FILE_NAME)
with open(OUTPUT_FILE_PATH, 'w') as output_file:
    json.dump(performances, output_file)