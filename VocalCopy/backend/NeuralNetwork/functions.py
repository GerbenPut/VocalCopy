import numpy as np

functions = {
    "relu": lambda x: max(0, x),
    "threshold": lambda x, t: max(t, x),
    "weighted input": lambda x, w, b: w*x+b,
    "weighted input matrix":\
        lambda x_matrix, w_matrix, b: np.dot(w_matrix, x_matrix)+b,
    "sigmoid": lambda z: 1/(1+np.exp(-z)),
    "weighted sigmoid": lambda x, w, b: 1/(1+np.exp(-1*(w*x+b))),
    "weighted sigmoid matrix":\
        lambda x_matrix, w_matrix, b:\
        1/(1+np.exp(-1*(np.dot(w_matrix, x_matrix)+b)))
}