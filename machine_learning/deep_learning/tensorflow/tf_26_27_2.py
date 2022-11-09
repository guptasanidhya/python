#Import tensorflow as alias tf
import tensorflow as tf

#generate color image
color=tf.random.uniform([2,2,3],maxval=255,dtype='int32')
print(color)
#reshape color image
color = tf.reshape(color,[2*2,3])
print(color)
