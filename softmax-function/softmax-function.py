import numpy as np

def softmax(x):
    """
    Compute the softmax of input x.
    Works for 1D or 2D NumPy arrays.
    For 2D, compute row-wise softmax.
    """
    # Write code here
    x = np.array(x)
    if x.ndim == 1:
        x = np.exp(x - np.max(x))
        return x / np.sum(x)
    x = np.exp(x - np.max(x, axis=1, keepdims=True))
    return x / np.sum(x, axis=1, keepdims=True)