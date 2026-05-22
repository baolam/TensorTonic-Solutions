import numpy as np

def geometric_pmf_mean(k, p):
    """
    Compute Geometric PMF and Mean.
    """
    # Write code here
    k = np.array(k)
    o = (1 - p) ** (k - 1) * p
    return (o, 1/p)