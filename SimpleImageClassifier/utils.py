import tensorflow as tf
import numpy as np
import os
import glob
import random
import scipy.misc


N_CLASSES = 2
N_CHANNEL = 3
LEARNING_RATE = 0.0001
BATCH_SIZE = 100
N_ITERATION = 10000
IMAGE_SIZE = 64
IMAGE_EXT ='jpg'

TRAIN_DATASET_PATH ='dataset/train/'
VAL_DATASET_PATH ='dataset/val/'

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

def get_folder_names():
    return [f for f in os.listdir(TRAIN_DATASET_PATH) if not f.startswith('.')]
    
def shuffle_in_unison(a, b):
     n_elem = a.shape[0]
     indices = np.random.permutation(n_elem)
     return a[indices], b[indices]


def get_random_indices(upper_limit, size):
    indices = random.sample(range(0, upper_limit), size)
    return indices

def load_data(dataset_path):
    print("loading data from " + dataset_path)
    folder_list = [f for f in os.listdir(dataset_path) if not f.startswith('.')]

    image_array=[]
    label_array=[]

    for index, folder in enumerate(folder_list):
        file_list = glob.glob(dataset_path + folder + '/*.'+IMAGE_EXT)
     
        temp_image_array = np.array([np.array(scipy.misc.imresize(scipy.misc.imread(file_name, mode='RGB').astype('float32'),(IMAGE_SIZE, IMAGE_SIZE))) for file_name in file_list])
        temp_image_array = temp_image_array/255.
    
        image_array.append(temp_image_array)

        temp_label_array = np.zeros(N_CLASSES)
        np.put(temp_label_array, index, 1)
        temp_label_array = np.array([temp_label_array for file_name in file_list])
        label_array.append(temp_label_array)
       
    image_array = np.concatenate(image_array, axis=0)
    label_array = np.concatenate(label_array, axis=0)

    image_array, label_array = shuffle_in_unison(image_array, label_array)

    return image_array, label_array

