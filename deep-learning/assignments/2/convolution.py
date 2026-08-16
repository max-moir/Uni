from __future__ import absolute_import

import os
import tensorflow as tf
import numpy as np
import random
import math

def conv2d(inputs, filters, strides, padding):
	"""
	Performs 2D convolution given 4D inputs and filter Tensors.
	:param inputs: tensor with shape [num_examples, in_height, in_width, in_channels]
	:param filters: tensor with shape [filter_height, filter_width, in_channels, out_channels]
	:param strides: MUST BE [1, 1, 1, 1] - list of strides, with each stride corresponding to each dimension in input
	:param padding: either "SAME" or "VALID", capitalization matters
	:return: outputs, NumPy array or Tensor with shape [num_examples, output_height, output_width, output_channels]
	"""

	num_examples = inputs.shape[0]
	in_height = inputs.shape[1]
	in_width = inputs.shape[2]
	input_in_channels = inputs.shape[3]

	filter_height = filters.shape[0]
	filter_width = filters.shape[1]
	filter_in_channels = filters.shape[2]
	filter_out_channels = filters.shape[3]

	num_examples_stride = strides[0]
	strideY = strides[1]
	strideX = strides[2]
	channels_stride = strides[3]

	assert(input_in_channels == filter_in_channels)
	assert(padding == "SAME" or padding == "VALID")

	padX = 0 if padding == "VALID" else math.floor((filter_width  - 1) / 2)
	padY = 0 if padding == "VALID" else math.floor((filter_height - 1) / 2)

	output_height = (in_height + 2 * padY - filter_height) // strideY + 1 
	output_width  = (in_width  + 2 * padX - filter_width)  // strideX + 1

	# Cleaning padding input
	inputs = np.pad(inputs,((0, 0),(padY, padY),(padX, padX),(0, 0),),mode="constant")

	# Calculate output dimensions
	outputs = np.zeros(
		(num_examples, output_height, output_width, filter_out_channels)
	)

	for i in range(num_examples):
		for y in range(output_height):
			for x in range(output_width):
				area = inputs[i, y:y + filter_height, x:x+filter_width, :] 
				for channel in range(filter_out_channels):
					filter = filters[:, :, :, channel]
					outputs[i, y, x, channel] = np.sum(area * filter)

	return outputs




