import numpy as np

def contrastive_loss(a, b, y, margin=1.0, reduction="mean") -> float:
    """
    a, b: arrays of shape (N, D) or (D,)  (will broadcast to (N,D))
    y:    array of shape (N,) with values in {0,1}; 1=similar, 0=dissimilar
    margin: float > 0
    reduction: "mean" (default) or "sum"
    Return: float
    """
    # Write code here
    a = np.array(a)
    b = np.array(b)
    y = np.array(y)
    m = margin
    
    d = np.sqrt(np.sum((a - b) ** 2, axis=-1))
    
    l = y * d ** 2 + (1 - y) * np.where(m - d <= 0, 0, m - d) ** 2
    if reduction == "mean":
        return l.mean()
    return l.sum()