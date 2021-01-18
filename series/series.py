def slices(series: str, length: int):
    if len(series) == 0:
        raise ValueError("Empty Series")
    if length < 0:
        raise ValueError("Length is negative")
    if length == 0:
        raise ValueError("Length is Zero")
    if len(series) < length:
        raise ValueError("Length is too large")
    slice = []
    for i in range(0, len(series) - length + 1):
        s = ''
        for j in range(i, i+length):
            s += series[j]
        slice.append(s)
    return slice
