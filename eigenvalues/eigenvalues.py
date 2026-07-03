import numpy as np

def calculate_eigenvalues(matrix):
    """
    Calculate eigenvalues of a square matrix.
    """
    # Write code here
    try:
        A = np.array(matrix)
    except:
        return None
        
    if A.ndim != 2 or A.shape[0] != A.shape[1]:
        return None
    
    print(A.shape)
    
    y, _ = np.linalg.eig(A)
    return y