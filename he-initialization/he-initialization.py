import numpy as np
def he_initialization(W, fan_in):
    """
    Scale raw weights to He uniform initialization.
    """
    # Write code here
    L = (6 / fan_in) ** 0.5
    W = np.asarray(W)

    return W * 2 * L - L