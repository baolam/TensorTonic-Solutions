import numpy as np

def dropout(x, p=0.5, rng=None):
    """
    Apply dropout to input x with probability p.
    Return (output, dropout_pattern).
    """
    # Write code here
    if rng is None:
        rng = np.random

    x = np.asarray(x)
    
    keep = 1 - p
    pattern = (rng.random(x.shape) < keep) / keep
    
    output = x * pattern

    return output, pattern