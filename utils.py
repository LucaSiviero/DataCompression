import os
import math


def normalize_to_int(value: float) -> int:
    '''
        converts a decimal value to its integer "representation".
        eg:
            input = 0.40657
            output = 40657
    '''
    while value - int(value) != 0:
        value = value * 10
    return value


def normalize_to_float(value: int) -> float:
    '''
        converts a integer value to its decimal "representation".
        eg:
            input = 874
            output = 0.874
    '''
    return float("0." + str(value))


def compression_ratio_from_file(uncompressed_path: str, compressed_path: str, decimal_digits = 2) -> float:
    '''
        returns compression ratio for the input files.
    '''
    uncompressed_size = os.path.getsize(uncompressed_path)
    compressed_size = os.path.getsize(compressed_path)

    if compressed_size == 0: return 0

    return round(uncompressed_size/compressed_size, decimal_digits)


def compression_ratio(uncompressed_text: str, compressed_text: str, decimal_digits = 2) -> float:
    '''
        returns compression ratio for the input texts.
    '''
    uncompressed_size = len(uncompressed_text)
    compressed_size = len(compressed_text)

    if compressed_size == 0: return 0

    return round(uncompressed_size/compressed_size, decimal_digits)


def get_entropy(alphabet: dict, decimal_digits = 4) -> float:
    '''
        calculates H() for a given alphabet, entropy it's then
        rounded according to 'decimal_digits'.
    '''
    sum_ = 0

    for char in alphabet:
        prob = alphabet[char]
        if prob > 0: 
            sum_ = sum_ + (prob * math.log((1/prob), 2))
        
    return round(sum_, decimal_digits)


def get_alphabets(alphabets: dict) -> list:
    '''
        returns an ordered list of alphabets,
        alphabet entropy is used as ordering criteria.
    '''
    alphabets_names = list(alphabets.keys())

    sorted_names = sorted(
        alphabets_names,
        key = lambda name : get_entropy(alphabets[name])
    )

    return [alphabets[alph_name] for alph_name in sorted_names]


def get_algorithms(performances: dict) -> list[str]:
    '''
        returns a list containing the algorithms used
        in the compressing stage. 
    '''
    return list(performances.keys())


def get_sizes(performances: dict) -> list[int]:
    '''
        returns a list containing the sizes used
        in the compressing stage. 
    '''
    for alg in performances:
        for entropy in performances[alg]:
            sizes = performances[alg][entropy].keys()
            return list(map(int, sizes))


def get_entropies(performances: dict) -> list[float]:
    '''
        returns a list containing the entropies used
        in the compressing stage. 
    '''
    for alg in performances:
        entropies = performances[alg].keys()
        return list(map(float, entropies))


def get_performances(performances: dict, algorithm: str, entropy: float, sizes: list[int]):
    '''
        returns the compression ratios of a given algorithm
        for a given  for the given sizes. 
    '''
    return [ performances[algorithm][str(entropy)][str(size)] for size in sizes ]


def print_performances(performances: dict) -> None:
    '''
        prints the performance 3-nested dictionary.
    '''
    SEP = "-"*8

    for alg in performances:
        print(f"==={alg}===")
        for source in performances[alg]:
            print(f"|{SEP}{source}{SEP}")
            for size in performances[alg][source]:
                perf = performances[alg][source][size]
                print(f"|\t{size}:{perf}")

def update_performances(performances: dict, alg: str, scaling_factor: float) -> None:
    for source in performances[alg]:
        for size in performances[alg][source]:
            value = performances[alg][source][size] 
            performances[alg][source][size] = value * scaling_factor
    return performances