from tensorflow import keras
import numpy as np

PATH = '20-10.h5'
N_LAYERS = 2


model = keras.models.load_model(PATH)

for i in range(0, N_LAYERS):
    weights = model.layers[i].get_weights()[0]
    biases = model.layers[i].get_weights()[1]

    filename_weights = "layer_" + str(i) + "_weights" + ".csv"
    filename_bias = "layer_" + str(i) + "_biases" + ".csv"
    np.savetxt(filename_weights, weights, delimiter=",")
    np.savetxt(filename_bias, biases, delimiter=",")
