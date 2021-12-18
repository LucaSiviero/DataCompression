from first_order_source import FirstOrderSource
from hybrid_algorithm import HybridAlgorithm
import utils
import json

FILEs_PATH = "files/"

'''
alphabets_file = open("alphabets.json")
alphabets = json.load(alphabets_file)
alphabets = utils.order_alphabets_by_entropy(alphabets)
'''

# generates a list containing 1, 10, ..., 10^6
# SIZES = [10**i for i in range(0, 7) ]
# file size is expressed in KB.
SIZES = [1, 10, 100, 1000, 10000, 100000]

# change alphabets_ to alphabets when json is correctly managed.
SOURCES = [
    FirstOrderSource(alphabets_["CONST"]),
    FirstOrderSource(alphabets_["K-ARY-25"]),
    FirstOrderSource(alphabets_["K-ARY-50"]),
    FirstOrderSource(alphabets_["K-ARY-75"]),
    FirstOrderSource(alphabets_["RANDOM"]),
]

ALGORITHMS = [
    HybridAlgorithm([]),
    HybridAlgorithm([]),
    # fill with instances of compression algorithms.
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


for source in SOURCES:
    for file_size in SIZES:
        # uncompressed file names will be in the form: source__size.txt
        # where 'source' give informations about the source used to generate the file.
        file_name = f"{source}__{file_size}.txt"
        
        # writing the uncompressed file.
        with open(FILEs_PATH + file_name, 'w') as file:
            num_char = utils.get_num_char(file_size)
            text = source.generate_text(num_char)
            file.write(text)

        for algorithm in ALGORITHMS:
            # compressed file names will be in the form: algorithm__source__size.txt
            # where 'algorithm' give informations about the algorithm used to 
            # compress the file, same definition for 'source' as before.
            compr_file_name = f"{algorithm}__{file_name}"

            # writing the compressed information into a new file.
            with open(FILEs_PATH + compr_file_name, 'w') as compr_file:
                compr_text = algorithm.compress(text)
                compr_file.write(compr_text)
            
            # calculating compression ration and saving it into 'performances'.
            compr_ratio = utils.get_compression_ratio(
                FILEs_PATH + file_name, 
                FILEs_PATH + compr_file_name
            )
            performances[str(algorithm)][str(source)][file_size] = compr_ratio