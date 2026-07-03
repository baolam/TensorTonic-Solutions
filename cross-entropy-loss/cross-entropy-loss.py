import numpy as np
import math

def cross_entropy_loss(y_true, y_pred):
    """
    Compute average cross-entropy loss for multi-class classification.
    """
    # Write code here
    N = len(y_true)
    s = 0

    for l, logits in zip(y_true, y_pred):
        s += math.log(logits[l])
    
    return -1 / N * s