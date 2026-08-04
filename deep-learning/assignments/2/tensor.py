import tensorflow as tf
import numpy as np

print(tf.__version__)


x = [[2.]]
m = tf.matmul(x, x)
print("x = {}".format(x))
print("m = {}".format(m))
print("hello, {}".format(m))


# Using a python list
my_variable = tf.Variable([[1.,0.]])
print(my_variable)

# Initializing variables with a NumPy array
my_variable_from_np_array = tf.Variable(np.zeros((3,3)))
print(my_variable_from_np_array)

# You can also use some tensorflow built in variables
gaussian_initialization = tf.Variable(tf.random.normal(shape=[3,3], stddev=.1))
print(gaussian_initialization)

# To convert a variable from a tensor to a NumPy array, use the numpy() function
my_np_variable = tf.Variable([[1., 2., 5.]]).numpy()
print(my_np_variable)