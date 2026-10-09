import numpy as np

def standard_scaler(X_train: np.ndarray, X_test: np.ndarray) -> np.ndarray:

    col_means = np.mean(X_train, axis = 0 )
    col_sigmas = np.std(X_train, axis = 0)
    mask = col_sigmas == 0 
    col_sigmas[mask] = 1

    # print(col_means, col_sigmas)

    return (X_test - col_means)/col_sigmas




   