import numpy as np

def rmsprop_step(w, g, s, lr=0.001, beta=0.9, eps=1e-8):
    """
    Perform one RMSProp update step.
    """
    # Write code here
    w = np.asarray(w)
    g = np.asarray(g)
    s = np.asarray(s)

    t = w.shape[0]
    s_new = beta * s + (1 - beta) * (g * g)
    w_new = w - (lr / (s_new + eps) ** 0.5) * g

    return (w_new, s_new)