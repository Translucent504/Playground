#Going to implement a neural net from scratch.

import numpy as np
import math

def net(X):
    '''
    Completely static neural net which takes in X  
    and outputs the prediction Y'.

    Architecture is a 3 layer net with this structure:
    X -> [o][o] -> [o][o] -> [o] -> Y'
    input -> (lin->relu) -> (lin->relu) -> lin->tanh 
    '''

    # Recipe:
    # Take the input X, throw it into layer 1
    # Take output of layer 1 throw into layer 2
    # Take output of layer 2 and throw into layer 3
    # Output of layer 3 is the prediction
    # compute the cost
    # return the predicted value and the associated cost
    # also keep track of the parameters A1,W1,Z1 etc that are needed
    # for backprop.

    # Refined:
    # initialize parameters W1 W2 W3 and b1 b2 b3.
    # do forward propagation 
    # compute cost
    # do backward propagation
    # update parameters
    # reiterate until satisfied?
    pass

def initialize_parameters(X):
    '''
    Initialize the weights W randomly and biases to 0

    returns a dict containing params and values.
    '''
    # a more general approach would be to include layer dimensions
    # as the input which then initializes all the parameters itself.
    # layer dimensions would be (number of inputs by number of nodes)
    # X should be properly shaped. its dimensions should be
    # number of features by number of training examples
