def precision_recall_at_k(recommended, relevant, k):
    """
    Compute precision@k and recall@k for a recommendation list.
    """
    # Write code here
    rs = recommended[:k]
    value = sum(1 for p in rs if p in relevant)

    return [value / k, value / len(relevant)]