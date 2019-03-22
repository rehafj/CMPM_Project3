import tensorflow as tf
import numpy as np

from utils import *

def Generator(noise):
    z = tf.layers.dense(noise, 4*4*1024, activation=tf.nn.relu, name='g_dense1')
    z = tf.reshape(z, [-1, 4, 4, 1024])

    g_hidden_layer1 = tf.layers.conv2d_transpose(z, filters=512, kernel_size=5, strides=2, activation=tf.nn.leaky_relu, name='g_conv1', padding='SAME')
    g_hidden_layer2 = tf.layers.conv2d_transpose(g_hidden_layer1, filters=256, kernel_size=5, strides=2,  activation=tf.nn.leaky_relu, name='g_conv2', padding='SAME')
    g_hidden_layer3 = tf.layers.conv2d_transpose(g_hidden_layer2, filters=128, kernel_size=5, strides=2, activation=tf.nn.leaky_relu, name='g_conv3', padding='SAME')

    g_output_layer = tf.layers.conv2d_transpose(g_hidden_layer3, filters=3, kernel_size=5, strides=2, activation=tf.nn.tanh, name='g_out', padding='SAME')
    print(g_output_layer.shape)
    return g_output_layer


def Discriminator(input_image, reuse=False):
    d_hidden_layer1 = tf.layers.conv2d(input_image, filters=64, kernel_size=5, strides=2, activation=tf.nn.leaky_relu, name='d_conv1', padding='SAME', reuse=reuse)
    d_hidden_layer2 = tf.layers.conv2d(d_hidden_layer1, filters=128, kernel_size=5, strides=2, activation=tf.nn.leaky_relu, name='d_conv2', padding='SAME', reuse=reuse)
    d_hidden_layer3 = tf.layers.conv2d(d_hidden_layer2, filters=256, kernel_size=5, strides=2, activation=tf.nn.leaky_relu, name='d_conv3', padding='SAME', reuse=reuse)
    d_hidden_layer4 = tf.layers.conv2d(d_hidden_layer3, filters=512, kernel_size=5, strides=2, activation=tf.nn.leaky_relu, name='d_conv4', padding='SAME', reuse=reuse)

    d_output_layer = tf.layers.dense(tf.layers.flatten(d_hidden_layer4), 1, reuse=reuse, name='d_out')
    return tf.nn.sigmoid(d_output_layer), d_output_layer
