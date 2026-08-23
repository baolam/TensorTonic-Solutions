import numpy as np

def positional_encoding(seq_len: int, d_model: int, base: float = 10000.0) -> np.ndarray:
    """
    Return PE of shape (seq_len, d_model) using sin/cos formulation.
    Odd d_model -> last column is sin.
    """
    # Write code here
    pos = np.arange(seq_len)[:, np.newaxis]
    
    pe = np.zeros((seq_len, d_model))
    
    num_sin = (d_model + 1) // 2
    num_cos = d_model // 2
    
    div_sin = np.exp(np.arange(0, num_sin * 2, 2) * -(np.log(base) / d_model))
    div_cos = np.exp(np.arange(0, num_cos * 2, 2) * -(np.log(base) / d_model))
    
    pe[:, 0::2] = np.sin(pos * div_sin)
    if num_cos > 0:
        pe[:, 1::2] = np.cos(pos * div_cos)
        
    return pe