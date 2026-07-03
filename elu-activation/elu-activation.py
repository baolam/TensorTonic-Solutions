import numpy as np

def elu(x, alpha):
    """
    Apply ELU activation to each element.
    """
    # Write code here
    # SELU, GELU (TRansformer --> ReLU)
    x = np.array(x)
    return (np.where(x > 0, x, alpha * (np.exp(x) - 1))).tolist()