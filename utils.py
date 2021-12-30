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


def get_alphabets(alphabets: dict) -> set:
    '''
        returns an orderd set of alphabets,
        alphabet entropy is used as ordering criteria.
    '''
    alphabets_names = list(alphabets.keys())

    sorted_names = sorted(
        alphabets_names,
        key = lambda name : get_entropy(alphabets[name])
    )

    sorted_alphabets = {}

    return sorted_alphabets