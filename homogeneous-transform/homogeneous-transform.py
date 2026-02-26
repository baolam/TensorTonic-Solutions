import numpy as np

def apply_homogeneous_transform(T, x):
    """
    Apply 4x4 homogeneous transform T to 3D point(s).
    """
    # Your code here
    T = np.asarray(T)
    x = np.asarray(x)

    only_one = x.ndim == 1
    if only_one:
        x = x[np.newaxis, :]
    
    ones = np.ones((x.shape[0], 1))
    x_com = np.hstack([x, ones])

    x_tran = x_com @ T.T
    x_tran = x_tran[:, :3]
    if only_one:
        return x_tran[0]
    return x_tran