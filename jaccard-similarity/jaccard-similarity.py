def jaccard_similarity(set_a, set_b):
    """
    Compute the Jaccard similarity between two item sets.
    """
    # Write code here
    set_a = set(set_a)
    set_b = set(set_b)
    n = len(set_a | set_b)
    if n == 0:
        return 0.
    return len(set_a & set_b) / n 