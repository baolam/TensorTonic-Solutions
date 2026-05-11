import numpy as np

def cosine_similarity(a, b):
    """
    Compute cosine similarity between two 1D NumPy arrays.
    Returns: float in [-1, 1]
    """
    # Write code here
    a = np.array(a)
    b = np.array(b)
    al = np.linalg.norm(a)
    bl = np.linalg.norm(b)
    if al == 0 or bl == 0:
        return 0.
    return np.dot(a, b) / (al * bl)