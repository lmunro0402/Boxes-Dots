# Neural Network
#
# Author: Luke Munro

import numpy as np
import time


class Neuron:
    """Neuron for logistic regression. Given layer, index in layer, and size of data 
    it outputs a single value."""
    def __init__(self, layer, index, sizeX, seed):
        np.random.seed(seed*2)
        # time.sleep(0.1)
        self.layer = layer
        self.index = index
        # Initialize weight randomly with mean 0
        self.weights = 2*np.random.random((int(sizeX)))-1

    def assignW(self, weights):
        self.weights = weights

    def getW(self):
        return self.weights

    def getZ(self, X):
        return np.dot(X, self.weights)


    def train(self, delta):
        return None 

