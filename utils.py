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


def get_compression_ratio(uncompressed_path: str, compressed_path: str) -> float:
    '''
        returns compression ratio for the input files.
    '''
    uncompressed_size = os.path.getsize(uncompressed_path)
    compressed_size = os.path.getsize(compressed_path)

    return compressed_size/uncompressed_size


def get_num_char(file_size: int) -> int:
    '''
        returns the amount of characters required to obtain a
        file of 'file_size' kb.
    '''
    pass


def get_entropy(alphabet: dict) -> float:
    '''
        calculates H() for a given alphabet.
    '''
    sum_ = 0

    for char in alphabet:
        prob = alphabet[char]
        if prob > 0: 
            sum_ = sum_ + (prob * math.log((1/prob), 2))
        
    return sum_


def order_alphabets_by_entropy(alphabets) -> dict:
    '''
        returns an orderd dictionary of alphabets,
        alphabet entropy is used as ordering criteria.
    '''
    alphabets_names = list(alphabets.keys())

    sorted_names = sorted(
        alphabets_names, 
        key=lambda name : get_entropy(alphabets[name])
    )

    sorted_alphabets = {}

    for name in sorted_names: 
        sorted_alphabets[name] = alphabets[name]

    return sorted_alphabets