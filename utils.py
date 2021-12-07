def normalize_to_int(value: float) -> int:
    while value - int(value) != 0:
        value = value * 10
    return value

def normalize_to_float(value: int) -> float:
    return float("0." + str(value))