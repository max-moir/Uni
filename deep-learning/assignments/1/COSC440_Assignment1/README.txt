# Answer the conceptual questions here
Q1: Is there anything we need to know to get your code to work? If you did not get your code working or handed in an incomplete solution please let us know what you did complete (0-4 sentences)

No, although increasing the batch size to 400 increases the accuracy to >90%.
I implemented it as instructed, but this change could be easily made.

Q2: Why do we normalize our pixel values between 0-1? (1-3 sentences)

The values are normalized from so that any numerical overflow issues are avoided.
This is because pixels are initially stored as uint8s, which have max size 255.
Therefore, any value higher would overflow, and the values should be stored as a float.

Q3: Why do we use a bias vector in our forward pass? (1-3 sentences)

We use the bias vector to allow the model to fit data that does not pass through the origin.
A higher bias also makes it easier for a neuron to return true, meaning that a non-zero bias will allow a result even if all inputs are 0.

Q4: Why do we separate the functions for the gradient descent update from the calculation of the gradient in back propagation? (2-4 sentences)

There are multiple reasons why these should be in seperate functions. 
Firstly, the optimizer should be modular, so that it can be easily substituted for another without re-writing the model.
Seperating these might also be beneficial for testing, so that the ouput of the backprop function can be verified without updating the weights of the model.

Q5: What are some qualities of MNIST that make it a “good” dataset for a classification problem? (2-3 sentences)

One good quality of the MNIST dataset is that it is already labelled. This makes it easy to compare the accuracy of a model against the correct result.
Additionally, all of the images are the same size and each pixel has a value in a standard range. This makes processing easier for the programmer.
The dataset is also large, and already partitioned into train images and test images, which makes setup for the solution to a classification problem less difficult.

Q6: Suppose you are an administrator of the NZ Health Service (CDHB or similar). What positive and/or negative effects would result from deploying an MNIST-trained neural network to recognize numerical codes on forms that are completed by hand by a patient when arriving for a health service appointment? (2-4 sentences)

One positive is that automating the process of code recognition may save time for medical professionals who might have more utility doing something else.
Additionally, code recognition could be done in larger batches than a human could read at one time, further saving human effort.
The most important downside to this is that the model doesn't have 100% accuracy, and errors in this application could have devastating results.
It also may require hardware / software that a standard health centre would not have already, so would require a set up process nation-wide.