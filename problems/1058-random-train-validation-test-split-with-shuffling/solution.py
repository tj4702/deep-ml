import numpy as np

def random_split(data, train_frac, validation_frac, seed=123):
    n = data.shape[0]
    idx = np.random.default_rng(seed).permutation(n)
    shuffled = data[idx]

    train_end = int(n * train_frac)
    validation_end = train_end + int(n * validation_frac)

    train = shuffled[:train_end]
    validation = shuffled[train_end: validation_end]     
    test = shuffled[validation_end :]    

    return [train, validation, test]