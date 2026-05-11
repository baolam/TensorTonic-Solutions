import numpy as np

def manhattan_distance(x, y):
    """
    Compute the Manhattan (L1) distance between vectors x and y.
    Must return a float.
    """
    # Write code here
    o = 0
    for i, j in zip(x, y):
        o += abs(i - j)
    return o