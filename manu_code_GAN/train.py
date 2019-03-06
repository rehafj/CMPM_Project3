import tensorflow as tf
import numpy as np

from utils import *
from model import *

def train(celeb_images):
    tf.reset_default_graph()

    z_size = 100

    global_step = tf.Variable(0, dtype=tf.int32, trainable=False, name='global_step')

    z_data = tf.placeholder(tf.float32, [None, z_size])
    real_data = tf.placeholder(tf.float32, [None, IMAGE_HEIGHT, IMAGE_WIDTH, N_CHANNEL])
    
    Gz = Generator(z_data)
    Dx, D_logit_real = Discriminator(real_data)
    Dg, D_logit_fake = Discriminator(Gz, reuse=True)

    # d_loss = -tf.reduce_mean(tf.log(Dx) + tf.log(1.-Dg))
    # g_loss = -tf.reduce_mean(tf.log(Dg))

    D_loss_real = tf.reduce_mean(tf.nn.sigmoid_cross_entropy_with_logits(logits=D_logit_real, labels=tf.ones_like(D_logit_real)))
    D_loss_fake = tf.reduce_mean(tf.nn.sigmoid_cross_entropy_with_logits(logits=D_logit_fake, labels=tf.zeros_like(D_logit_fake)))
    d_loss = D_loss_real + D_loss_fake
    g_loss = tf.reduce_mean(tf.nn.sigmoid_cross_entropy_with_logits(logits=D_logit_fake, labels=tf.ones_like(D_logit_fake)))

    t_vars = tf.trainable_variables()
    d_vars = [var for var in t_vars if 'd_' in var.name]
    g_vars = [var for var in t_vars if 'g_' in var.name]

    d_optimizer = tf.train.AdamOptimizer(LEARNING_RATE, beta1=0.5).minimize(d_loss, var_list=d_vars, global_step=global_step)
    g_optimizer = tf.train.AdamOptimizer(LEARNING_RATE, beta1=0.5).minimize(g_loss, var_list=g_vars)
    

    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        
        saver = initialize(sess)

        initial_step = global_step.eval()
    
        for index in range(initial_step, N_ITERATION):
            # print("Iteration "+ str(index))
            random_indices = get_random_indices(celeb_images.shape[0], BATCH_SIZE)
            
            noise = np.random.normal(0, 1, size=[BATCH_SIZE, z_size]).astype(np.float32)
            real_image = np.take(celeb_images, random_indices, 0)

            _, dLoss = sess.run([d_optimizer, d_loss], feed_dict={z_data: noise, real_data: real_image})
            _, gLoss = sess.run([g_optimizer, g_loss], feed_dict={z_data: noise})
            _, gLoss = sess.run([g_optimizer, g_loss], feed_dict={z_data: noise})


            if (index+1) % 100 == 0:
                saver.save(sess, CKPT_DIR, index)
                val_noise = np.random.normal(0, 1, size=[BATCH_SIZE, z_size]).astype(np.float32)
                val_output = sess.run(Gz, feed_dict={z_data: val_noise})
                print("Iteration %d, gen loss %g %%, disc loss %g %%"%(index+1, gLoss, dLoss))
                for i, val_image in enumerate(val_output):
                    val_image = (val_image+1)/2
                    scipy.misc.imsave("validation_results/"+str(i)+".jpg", val_image)

if __name__ == "__main__":

    celeb_images = load_data(DATASET_PATH)
    print(celeb_images.shape)

    train(celeb_images)
    
