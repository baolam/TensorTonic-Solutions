import numpy as np

def dot_product(x, y):
    """
    Compute the dot product of two 1D arrays x and y.
    Must return a float.
    """
    # Write code here
    # Dot product trong AI???
    # --> 
    # Naive for
    s = 0
    if len(x) != len(y):
        raise ValueError()
    
    for x1, x2 in zip(x, y):
        s += x1 * x2
    
    return s