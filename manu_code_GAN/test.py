import tensorflow as tf
import numpy as np
import sys
import scipy.misc


from utils import *
from model import *


def test():

    z_data = tf.placeholder(tf.float32, [None, 100])    

    output = Generator(z_data)

    sess = tf.Session()
    sess.run(tf.global_variables_initializer())
    saver = initialize(sess)

    noise = np.random.normal(0, 1, size=[BATCH_SIZE, 100]).astype(np.float32)
    test_output = sess.run(output, feed_dict={z_data: noise})

    scipy.misc.imsave("test_results/output.jpg", test_output[0])


    print("Output saved in test_results/")

if __name__ == "__main__":
    test()
    
