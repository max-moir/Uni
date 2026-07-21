import gzip
import shutil
import numpy as np
import numpy.typing as npt

INPUT_HEADER_SIZE = 16
LABEL_HEADER_SIZE = 8
IMAGE_SIZE = 28 * 28

def get_data(inputs_file_path : str, labels_file_path: str, num_examples: int):
    """
    Takes in an inputs file path and labels file path, unzips both files,
    normalizes the inputs, and returns (NumPy array of inputs, NumPy
    array of labels). Read the data of the file into a buffer and use
    np.frombuffer to turn the data into a NumPy array. Keep in mind that
    each file has a header of a certain size. This method should be called
    within the main function of the assignment.py file to get BOTH the train and
    test data. If you change this method and/or write up separate methods for
    both train and test data, we will deduct points.

    Hint: look at the writeup for sample code on using the gzip library

    :param inputs_file_path: file path for inputs, something like
    'MNIST_data/t10k-images-idx3-ubyte.gz'
    :param labels_file_path: file path for labels, something like
    'MNIST_data/t10k-labels-idx1-ubyte.gz'
    :param num_examples: used to read from the bytestream into a buffer. Rather
    than hardcoding a number to read from the bytestream, keep in mind that each image
    (example) is 28 * 28, with a header of a certain number.
    :return: NumPy array of inputs as float32 and labels as int8
    """


    with gzip.open(inputs_file_path, 'rb') as f:
        f.read(INPUT_HEADER_SIZE)
        buffer = f.read(num_examples * IMAGE_SIZE)

    inputs = np.frombuffer(buffer, np.uint8)
    inputs = inputs.reshape((num_examples, IMAGE_SIZE)).astype(np.float32) / 255.0

    with gzip.open(labels_file_path, 'rb') as f:
        f.read(LABEL_HEADER_SIZE)
        buffer = f.read(num_examples)

    labels = np.frombuffer(buffer, np.uint8).reshape((num_examples, 1))

    return inputs, labels


