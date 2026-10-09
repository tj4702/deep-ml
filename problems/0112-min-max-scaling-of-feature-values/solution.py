def min_max(x: list[float]) -> list[float]:

    import numpy as np

    max_val = max(x)
    min_val = min(x)

    if max_val - min_val == 0 :
        den = 1 
    else:
        den = max_val - min_val

    x = np.array(x)

    return np.round((x- min_val)/den, 4).tolist()

    