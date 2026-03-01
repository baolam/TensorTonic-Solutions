import numpy as np

def global_avg_pool(x):
    """
    Compute global average pooling over spatial dims.
    Supports (C,H,W) => (C,) and (N,C,H,W) => (N,C).
    """
    # Write code here
    x = np.asarray(x)
    N, C, H, W = -1, -1, -1, -1
    if x.ndim == 3:
        C, H, W = x.shape
        x = x.reshape(C, -1)
    else:
        N, C, H, W = x.shape
        x = x.reshape(N, C, -1)

    if N == -1:
        return x.sum(axis=1) / (H * W)
    return x.sum(axis=2) / (H * W)