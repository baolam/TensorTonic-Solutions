import numpy as np
from collections import defaultdict

def random_forest_vote(predictions):
    """
    Compute the majority vote from multiple tree predictions.
    """
    # Write code here
    answer = []
    
    m, n = len(predictions), len(predictions[0])
    for j in range(n):
        votes = defaultdict(int)
        
        for i in range(m):
            votes[predictions[i][j]] += 1
            
        label = max(votes.items(), key = lambda x : (x[1], -x[0]))[0]
        answer.append(label)

    return answer
        