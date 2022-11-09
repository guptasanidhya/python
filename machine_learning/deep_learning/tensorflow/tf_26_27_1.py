# Import tensorflow as alias tf
import tensorflow as tf

#generate grayscale image
gray=tf.random.uniform([2,2],maxval=255,dtype='int32')
print(gray)
#reshape grayscale image
gray=tf.reshape(gray,[2*2,1])

print(gray)