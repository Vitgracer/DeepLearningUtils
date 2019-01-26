import numpy as np
from datasetLoader import loadDataset


def sigmoid(z):
    return 1.0 / (1.0 + np.exp(-z))

# dim - size of a vector w
def zeroInit(dim):
    w = np.zeros((dim, 1))
    b = 0
    
    return w, b

def computeBinaryCrossEntropy(A, Y, m):    
    return -1.0 / m * (np.sum(Y * np.log(A) + (1. - Y) * np.log(1. - A)))

def propagate(w, b, X, Y):
    """
    Arguments:
    w -- weights, a numpy array of size (w * h * 3, 1)
    b -- bias, a scalar
    X -- data of size (w * h * 3, number of examples)
    Y -- true "label" vector of size (1, number of examples)

    Return:
    cost -- negative log-likelihood cost for logistic regression
    dw -- gradient of the loss with respect to w, thus same shape as w
    db -- gradient of the loss with respect to b, thus same shape as b
    """
    
    # number of examples 
    m = X.shape[1]
    
    # compute z^(i) for every example x^(i)
    # size = (1, m)
    Z = np.dot(w.T, X) + b
    
    # compute activation for every z^(i)
    # size = (1, m)
    A = sigmoid(Z)
    
    # compute cost J as binary crossentropy 
    cost = computeBinaryCrossEntropy(A, Y, m)
    
    # compute dJ / dw = [ dJ / dw1, ... , dJ / dw_m ]
    # size is the same as w (number of features)
    # db is the same size as b, i.e scalar 
    dw = 1. / m * np.dot(X, (A - Y).T) 
    db = 1. / m * np.sum(A - Y)

    assert(dw.shape == w.shape)
    assert(db.dtype == float)
    cost = np.squeeze(cost)
    assert(cost.shape == ())
    
    grads = {"dw": dw,
             "db": db}
    
    return grads, cost 

if __name__ == "__main__":
    trainX, trainY, testX, testY, classes = loadDataset()
    
    print ("Number of training examples: {0}".format(len(trainX)))
    print ("Number of testing examples: {0}".format(len(testX)))
    print ("Shape of each image: {0}".format(trainX[0].shape))
    
    # transpose is implemented because of convenienece 
    trainXpreproc = trainX.reshape(trainX.shape[0], -1).T / 255.
    testXpreproc = testX.reshape(testX.shape[0], -1).T / 255.

    