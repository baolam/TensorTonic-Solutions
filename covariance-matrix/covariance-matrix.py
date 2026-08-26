import numpy as np

def covariance_matrix(X: list) -> np.ndarray:
    """
    Returns the covariance matrix as a NumPy array.
    """
    # Write code here
    X = np.array(X)
    N = X.shape[0]

    mu = np.mean(X, axis=0)
    X_c = X - mu

    cov = (X_c.T @ X_c) / (N - 1)
    return cov