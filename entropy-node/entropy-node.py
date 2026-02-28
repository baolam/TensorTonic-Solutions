import numpy as np

def entropy_node(y):
    """
    Compute entropy for a single node using stable logarithms.
    """
    # Write code here
    y = np.asarray(y)
    v, c = np.unique(y, return_counts=True)
    
    if v.shape[0] == 1:
        return 0.0

    p = c / c.sum()
    return - (p * np.log2(p)).sum()