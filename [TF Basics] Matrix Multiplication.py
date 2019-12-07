#Needed this to run v2 of tensorflow
%tensorflow_version 2.x  

import tensorflow as tf

mat_A = tf.random.normal(shape = (2,3), mean = 0, stddev = 2, dtype = tf.dtypes.float32, seed = None, name = "mat_A")

mat_B = tf.random.truncated_normal(shape = (3,5), mean = 0, stddev = 2, dtype = tf.dtypes.float32, seed = None, name = "mat_B")



result = tf.linalg.matmul(mat_A, mat_B)



print(result)
