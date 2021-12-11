import os

def normalize_to_int(value: float) -> int:
    while value - int(value) != 0:
        value = value * 10
    return value

def normalize_to_float(value: int) -> float:
    return float("0." + str(value))

def get_compression_ratio(uncompressed_path: str, compressed_path: str) -> float:
    uncompressed_size = os.path.getsize(uncompressed_path)
    compressed_size = os.path.getsize(compressed_path)

    return compressed_size/uncompressed_size