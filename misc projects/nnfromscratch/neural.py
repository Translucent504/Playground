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
    # layer dimensions would be (???number of inputs by number of nodes???)
    # X should be properly shaped. its dimensions should be
    # number of features by number of training examples

    W1 = np.random.randn(2,1)
    b1 = np.zeros((2,1))
    W2 = np.random.randn(2,2)
    b2 = np.zeros((2,1))
    W3 = np.random.randn(1,2)
    b3 = np.zeros((1,1))
    params = {'W1':W1,'W2':W2,'W3':W3,'b1':b1,'b2':b2,'b3':b3}
    #print(params)
    return params

def forward_prop(X, params):
    m = X.shape[0]
    X = np.reshape(X,(1,m))
    W1 = params['W1']
    W2 = params['W2']
    W3 = params['W3']
    b1 = params['b1']
    b2 = params['b2']
    b3 = params['b3']
    
    Z1 = np.dot(W1,X) + b1
    A1 = relu(Z1)
    Z2 = np.dot(W2,A1) + b2
    A2 = relu(Z2)
    Z3 = np.dot(W3,A2) + b3
    A3 = tanh(Z3)

    # compute cost
    #np.multiply(-np.log(A3),Y) + np.multiply(-np.log(1 - A3), 1 - Y)
    tmpcost = np.multiply(-np.log(A3), Y) + np.multiply(-np.log(1 - A3), 1 - Y)
    cost = 1./m *(np.sum(tmpcost))

    params['Z1'] = Z1
    params['Z2'] = Z2
    params['Z3'] = Z3
    params['A1'] = A1
    params['A2'] = A2
    params['A3'] = A3
    #print(cost)
    return cost, params

def backprop(cost, params):
    # take the cost and the params
    # use A3 to get dZ3 then keep going back
    pass

def relu(x):
    x[x<0] = 0
    return x

def tanh(x):
    #print(np.tanh(x))
    return np.tanh(x)



# fake dataset
X = [x for x in range(20000)]
Y = [int(x%3==0) for x in X]
X = np.array(X)
Y = np.array(Y)
#print(X,Y)
params = initialize_parameters(X)
forward_prop(X,params)