import os


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