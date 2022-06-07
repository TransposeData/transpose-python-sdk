import numpy as np


def gini(x):
    total = 0
    
    for i, xi in enumerate(x[:-1], 1):
        total += np.sum(np.abs(x[i:] - xi))
    return total / (len(x)**2 * np.mean(x))