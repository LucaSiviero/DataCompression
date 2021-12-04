def normalize_value(value: float) -> int:
    while value - int(value) != 0:
        value = value * 10
    return value
    