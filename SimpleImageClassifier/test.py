import tensorflow as tf
import numpy as np
import sys
import scipy.misc


from utils import *
from model import *


def test(image_path):

    labels = get_folder_names()
    test_image = scipy.misc.imresize(scipy.misc.imread(image_path, mode='RGB').astype('float32'),(IMAGE_SIZE_X, IMAGE_SIZE_Y))
    test_image = np.expand_dims(test_image, 0)
    test_image = test_image/255.

    test_data = tf.placeholder(tf.float32, [None, IMAGE_SIZE_X, IMAGE_SIZE_Y, N_CHANNEL])

    output = neural_network(test_data)
    softmax_output = tf.nn.softmax(output)

    sess = tf.Session()
    sess.run(tf.global_variables_initializer())
    saver = initialize(sess)



    test_output = sess.run(softmax_output, feed_dict={test_data: test_image})
    print(test_output)
    print(labels[np.argmax(test_output)])
    for index, label in enumerate(labels):
        print(label +' - '+ str(round(test_output[0][index]* 100,2))+'%' )

if __name__ == "__main__":
    image_path = sys.argv[1]
    test(image_path)
