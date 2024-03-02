from math import log2

# dict(value, occurences)
def entropy(data: dict, n: int) -> float:
    x = 0
    for k in data:
        p = data[k] / n
        x += p * log2(p)
    return -x
