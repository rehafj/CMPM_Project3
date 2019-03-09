import tensorflow as tf
import numpy as np

from utils import *

def Generator(noise):
    c4, c8, c16, c32, c64 = 512, 256, 128, 64, 32 # channel num from tutorial
    z = tf.layers.dense(noise, 4*4*1024, activation=tf.nn.relu, name='g_dense1')
    z = tf.reshape(z, [-1, 4, 4, 1024])

    g_hidden_layer1 = tf.layers.conv2d_transpose(z, filters=c4, kernel_initializer=tf.truncated_normal_initializer(stddev=0.02),
                                    kernel_size=5, strides=2, activation=tf.nn.relu, name='g_conv1', padding='SAME')
    g_hidden_layer2 = tf.layers.conv2d_transpose(g_hidden_layer1, filters=c8, kernel_initializer=tf.truncated_normal_initializer(stddev=0.02),
                                    kernel_size=5, strides=2,  activation=tf.nn.relu, name='g_conv2', padding='SAME')
    g_hidden_layer3 = tf.layers.conv2d_transpose(g_hidden_layer2, filters=c16, kernel_initializer=tf.truncated_normal_initializer(stddev=0.02),
                                    kernel_size=5, strides=2, activation=tf.nn.relu, name='g_conv3', padding='SAME')
    g_hidden_layer4 = tf.layers.conv2d_transpose(g_hidden_layer3, filters=c32, kernel_initializer=tf.truncated_normal_initializer(stddev=0.02),
                                    kernel_size=5, strides=2, activation=tf.nn.relu, name='g_conv4', padding='SAME')
    g_hidden_layer5 = tf.layers.conv2d_transpose(g_hidden_layer4, filters=c64, kernel_initializer=tf.truncated_normal_initializer(stddev=0.02),
                                    kernel_size=5, strides=2, activation=tf.nn.relu, name='g_conv5', padding='SAME')

    g_output_layer = tf.layers.conv2d_transpose(g_hidden_layer5, filters=3, kernel_initializer=tf.truncated_normal_initializer(stddev=0.02),
                                    kernel_size=5, strides=2, activation=tf.nn.tanh, name='g_out', padding='SAME')
    print(g_output_layer.shape)
    return g_output_layer


def Discriminator(input_image, reuse=False):
    c2, c4, c8, c16 = 64, 128, 256, 512  # channel num: 64, 128, 256, 512

    d_hidden_layer1 = tf.layers.conv2d(input_image, filters=c2,
                                 kernel_size=5, strides=2, activation=tf.nn.leaky_relu, name='d_conv1', padding='SAME', reuse=reuse)
    d_hidden_layer2 = tf.layers.conv2d(d_hidden_layer1, filters=c4, kernel_initializer=tf.truncated_normal_initializer(stddev=0.02),
                                 kernel_size=5, strides=2, activation=tf.nn.leaky_relu, name='d_conv2', padding='SAME', reuse=reuse)
    d_hidden_layer3 = tf.layers.conv2d(d_hidden_layer2, filters=c8, kernel_initializer=tf.truncated_normal_initializer(stddev=0.02),
                                 kernel_size=5, strides=2, activation=tf.nn.leaky_relu, name='d_conv3', padding='SAME', reuse=reuse)
    d_hidden_layer4 = tf.layers.conv2d(d_hidden_layer3, filters=c16, kernel_initializer=tf.truncated_normal_initializer(stddev=0.02),
                                 kernel_size=5, strides=2, activation=tf.nn.leaky_relu, name='d_conv4', padding='SAME', reuse=reuse)


    d_output_layer = tf.layers.dense(tf.layers.flatten(d_hidden_layer4), 1, reuse=reuse, name='d_out')
    return tf.nn.sigmoid(d_output_layer), d_output_layer

#kernel_initializer=tf.truncated_normal_initializer(stddev=0.02)
# pixToPix
# dc Gan
