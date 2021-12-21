from first_order_source import FirstOrderSource
from hybrid_algorithm import HybridAlgorithm
from huffman import HuffmanCoding
from lzw import LZW
import utils
import json
import os

# loading (and then ordering) alphabets from the alphabets' file.
here = os.path.dirname(os.path.abspath(__file__))
alphabets_path = os.path.join(here, 'alphabets.json')
alphabets_file = open(alphabets_path)
alphabets = utils.order_alphabets(json.load(alphabets_file))


FILEs_PATH = os.path.join(here, 'files')
os.mkdir(FILEs_PATH)


SIZES = [ 1, 10, 100, 1000, 10000, 100000 ]

SOURCES = [ FirstOrderSource(alphabet) for alphabet in alphabets.values() ]

ALGORITHMS = [
    HybridAlgorithm([HuffmanCoding(), LZW()]),
    HybridAlgorithm([HuffmanCoding()]),
]

# creating a storage for compression ratios with the following structure:
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


for source in SOURCES:
    for file_size in SIZES:
        # uncompressed file names will be in the form: source__size.txt
        # where 'source' give informations about the source used to generate the file.
        file_name = f"{source}{INFO_SEP}{file_size}.txt"
        uncomp_file_path = os.path.join(FILEs_PATH, file_name)

        # writing the uncompressed file.
        with open(uncomp_file_path, 'w') as file:
            text = source.generate_text(file_size)
            file.write(text)

        for algorithm in ALGORITHMS:
            # compressed file names will be in the form: algorithm__source__size.txt
            # where 'algorithm' give informations about the algorithm used to 
            # compress the file, same definition for 'source' as before.
            compr_file_name = f"{str(algorithm)}{INFO_SEP}{file_name}"
            compr_file_path = os.path.join(FILEs_PATH, compr_file_name)

            # writing the compressed information into a new file.
            with open(compr_file_path, 'w') as compr_file:
                compr_text = algorithm.compress(text)
                compr_file.write(compr_text)
            
            # calculating compression ration and saving it into 'performances'.
            compr_ratio = utils.get_compression_ratio(uncomp_file_path, compr_file_path)
            performances[str(algorithm)][str(source)][file_size] = compr_ratio