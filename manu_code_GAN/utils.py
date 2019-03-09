import tensorflow as tf
import numpy as np
import os
import glob
import random
import scipy.misc


N_CHANNEL = 3
LEARNING_RATE = 0.0001
BATCH_SIZE = 5
N_ITERATION = 150000
IMAGE_WIDTH = 190
IMAGE_HEIGHT = 110
IMAGE_EXT ='png'

DATASET_PATH ='dataset/'

CKPT_DIR = './Checkpoints/'
GRAPH_DIR = './Graphs/'

def initialize(sess):
    saver = tf.train.Saver()
    writer = tf.summary.FileWriter(GRAPH_DIR, sess.graph)

    if not os.path.exists(CKPT_DIR):
        os.makedirs(CKPT_DIR)

    ckpt = tf.train.get_checkpoint_state(os.path.dirname(CKPT_DIR))
    if ckpt and ckpt.model_checkpoint_path:
        saver.restore(sess, ckpt.model_checkpoint_path)

    return saver

def shuffle_in_unison(a, b):
     n_elem = a.shape[0]
     indices = np.random.permutation(n_elem)
     return a[indices], b[indices]


def get_random_indices(upper_limit, size):
    indices = random.sample(range(0, upper_limit), size)
    return indices

def load_data(dataset_path):
    print("loading data from " + dataset_path)

    image_array=[]

    file_list = glob.glob(dataset_path + '/*.'+IMAGE_EXT)

    temp_image_array = np.array([np.array(scipy.misc.imresize(scipy.misc.imread(file_name, mode='RGB').astype('float32'),(IMAGE_HEIGHT, IMAGE_WIDTH))) for file_name in file_list])
    temp_image_array = temp_image_array/127. -1

    image_array.append(temp_image_array)
    image_array = np.concatenate(image_array, axis=0)

    return image_array
