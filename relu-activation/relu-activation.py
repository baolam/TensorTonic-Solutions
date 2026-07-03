import numpy as np

def relu(x):
    """
    Implement ReLU activation function.
    """
    # Write code here
    x = np.array(x)
    o = np.where(x > 0, x, 0)
    # if x > 0:
    #     return x
    # else:
    #     return 0
    return o