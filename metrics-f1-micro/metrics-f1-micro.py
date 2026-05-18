import numpy as np

def f1_micro(y_true, y_pred) -> float:
    """
    Compute micro-averaged F1 for multi-class integer labels.
    """
    # Write code here
    y_true = np.array(y_true)
    y_pred = np.array(y_pred)

    classes = np.unique(y_true)
    tp, fp, fn = 0, 0, 0

    for c in classes:
        actual = y_true == c
        predict = y_pred == c

        tp += np.sum(actual & predict)
        fp += np.sum(~actual & predict)
        fn += np.sum(actual & ~predict)

    return 2 * tp / (2 * tp + fp + fn)