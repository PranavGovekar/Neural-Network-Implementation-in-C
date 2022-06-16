import numpy as np

class Layer_Dense:
    def __init__(self, weight_arr, bias_arr):
        self.weights = weight_arr
        self.biases = bias_arr

    def forward(self, inputs):
        w = self.weights
        self.output = np.dot(inputs, w) + self.biases


class Activation_ReLU:
    def forward(self, inputs):
        self.output = np.maximum(0, inputs)


class Activation_Softmax:
    def forward(self, inputs):
        exp_values = np.exp(inputs - np.max(inputs, axis=1, keepdims=True))
        probabilities = exp_values / np.sum(exp_values, axis=1, keepdims=True)
        self.output = probabilities

LAYERS = 3
layer = []

for i in range(1,LAYERS+1):
    filename_weights = "digit weights\\" + "layer_" + str(i) + "_weights" + ".csv"
    filename_bias = "digit weights\\" + "layer_" + str(i) + "_biases" + ".csv"
    weights = (np.loadtxt(filename_weights, delimiter=','))
    biases = (np.loadtxt(filename_bias, delimiter=','))
    layer.append(Layer_Dense(weights, biases))

rElu = Activation_ReLU()
sOft = Activation_Softmax()

X = np.loadtxt('test\\9.csv', delimiter=',')
print(type(X[1][1]))

X = X.flatten()
layer[0].forward(X)
rElu.forward(layer[0].output)
print(len(rElu.output))
layer[1].forward(rElu.output)
rElu.forward(layer[1].output)
print(len(rElu.output))
layer[2].forward(rElu.output)
rElu.forward(layer[2].output)
print(len(rElu.output))
print(np.argmax(rElu.output))
