import tensorflow as tf
import numpy as np


from utils import *
from model import *


def train(train_images, train_labels, val_images, val_labels):
    tf.reset_default_graph()

    global_step = tf.Variable(0, dtype=tf.int32, trainable=False, name='global_step')

    training_data = tf.placeholder(tf.float32, [None, IMAGE_SIZE, IMAGE_SIZE, N_CHANNEL])
    labels = tf.placeholder(tf.float32, [None, N_CLASSES])

    output = neural_network(training_data)

    loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(labels=labels, logits=output))
    optimizer = tf.train.AdamOptimizer(LEARNING_RATE).minimize(loss, global_step=global_step)
 
    correct_prediction = tf.equal(tf.argmax(output, 1), tf.argmax(labels, 1))
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        
        saver = initialize(sess)

        initial_step = global_step.eval()
    
        for index in range(initial_step, N_ITERATION):
            # print("Iteration "+ str(index))
            random_indices = get_random_indices(train_images.shape[0], BATCH_SIZE)
            
            input_batch = np.take(train_images, random_indices, 0)
            labels_batch = np.take(train_labels, random_indices, 0)

            sess.run(optimizer, feed_dict={training_data: input_batch, labels: labels_batch})

            if (index+1) % 100 == 0:
                saver.save(sess, CKPT_DIR, index)
                train_accuracy = sess.run(accuracy, feed_dict={training_data: input_batch, labels: labels_batch})
                val_accuracy = sess.run(accuracy, feed_dict={training_data: val_images, labels: val_labels})
                print("Iteration %d, train accuracy %g %%, validation accuracy %g %%"%(index+1, train_accuracy*100, val_accuracy*100))

if __name__ == "__main__":
    train_images, train_labels = load_data(TRAIN_DATASET_PATH)
    val_images, val_labels = load_data(VAL_DATASET_PATH)
    train(train_images, train_labels, val_images, val_labels)
    
