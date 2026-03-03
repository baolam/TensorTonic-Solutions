import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    # Write code here
    x = np.asarray(x)
    p = np.asarray(p)
    if p.sum() != 1:
        raise ValueError("ValueError")
    return (x * p).sum()
