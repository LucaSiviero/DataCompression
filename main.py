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

# loading (and then ordering) alphabets from the alphabets' file.
here = os.path.dirname(os.path.abspath(__file__))
alphabets_path = os.path.join(here, 'alphabets.json')
alphabets_file = open(alphabets_path)
alphabets = utils.order_alphabets(json.load(alphabets_file))

# creating a folder for un/compressed files.
WRITING_FILES_IS_ENABLED = False

if WRITING_FILES_IS_ENABLED:
    FILEs_PATH = os.path.join(here, 'files')
    shutil.rmtree(FILEs_PATH, ignore_errors=True)
    os.mkdir(FILEs_PATH)


SIZES = [ 100, 1000, 10000, 100000 ]

SOURCES = [ FirstOrderSource(alphabet) for alphabet in alphabets.values() ]

ALGORITHMS = [
    HybridAlgorithm([HuffmanCoding()]),
]

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
SEP = "-"*8


for source in SOURCES:
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
            print(f"uncomp_size: {len(text)}, comp_size: {len(compr_text)}, entropy: {str(source)}, size:{file_size}")

for alg in performances:
    print(f"==={alg}===")
    for source in performances[alg]:
        print(f"|{SEP}{source}{SEP}")
        for size in performances[alg][source]:
            perf = performances[alg][source][size]
            print(f"|\t{size}:{perf}")