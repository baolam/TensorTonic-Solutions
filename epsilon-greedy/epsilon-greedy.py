import numpy as np

def epsilon_greedy(q_values, epsilon, rng=None):
    """
    Returns: action index (int)
    """
    # Write code here
    n = [i for i in range(len(q_values))]
    
    if rng is None:
        rng = np.random

    q_values = np.asarray(q_values)
    if rng.random() < epsilon:
        return rng.choice(n)

    return q_values.argmax()
