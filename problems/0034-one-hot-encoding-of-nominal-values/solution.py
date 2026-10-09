import numpy as np

def to_categorical(x, n_col=None):

	x = np.array(x)

	if n_col is None:
		n_col = np.max(x) +1

	ohe = np.zeros((x.shape[0], n_col))

	for i, num in enumerate(x):
		ohe[i, num] = 1
	
	return ohe




