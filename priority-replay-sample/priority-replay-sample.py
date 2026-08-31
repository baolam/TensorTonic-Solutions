import numpy as np

def priority_replay_sample(priorities: list, alpha: float, beta: float) -> list:
    """
    Returns sampling probabilities and normalized importance weights.
    """
    # Write code here
    N = len(priorities)
    p = np.array(priorities)
    p = p ** alpha

    sam_probs = p / p.sum()
    W = (N * sam_probs) ** (-beta)

    real_W = W / np.max(W)
    return [sam_probs.tolist(), real_W.tolist()]
    