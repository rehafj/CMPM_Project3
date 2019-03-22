import tensorflow as tf
import numpy as np

from utils import *

def neural_network(input_data):
    hidden_layer1 = tf.layers.conv2d(input_data, filters=32, kernel_size=3, activation=tf.nn.relu)
    hidden_layer2 = tf.layers.conv2d(hidden_layer1, filters=32, kernel_size=3, activation=tf.nn.relu)
    hidden_layer3 = tf.layers.conv2d(hidden_layer2, filters=32, kernel_size=3, activation=tf.nn.relu)
    hidden_layer4_FCN = tf.layers.flatten(hidden_layer3)
    hidden_layer4_FCN = tf.nn.relu(tf.layers.dense(hidden_layer4_FCN, 64))
    output_layer = tf.layers.dense(hidden_layer4_FCN, N_CLASSES)

    return output_layer
