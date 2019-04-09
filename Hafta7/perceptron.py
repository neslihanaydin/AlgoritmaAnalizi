
# coding: utf-8

# In[4]:

get_ipython().magic('matplotlib inline')
import numpy as np
import matplotlib.pyplot as plt
image_size = 28 # width and length
no_of_different_labels = 10 #  i.e. 0, 1, 2, 3, ..., 9
image_pixels = image_size * image_size
data_path = r"./"

training_data = np.loadtxt(data_path + "mnist_test.csv", 
                       delimiter=",") 


# In[10]:

# Make a prediction with weights
def predict(row, weights):
    activation = weights[0]
    for i in range(len(row)-1):
        activation += weights[i + 1] * row[i]
    return 1.0 if activation >= 0.0 else 0.0


# In[ ]:

for row in training_data:
    prediction = predict(row, weights)
    print("Expected=%d, Predicted=%d" % (row[-1], prediction))


# In[38]:

import numpy as np
class Perceptron(object):
    def __init__(self, no_of_inputs, threshold=10000, learning_rate=0.01):
        self.threshold = threshold
        self.learning_rate = learning_rate
        self.weights = np.zeros(no_of_inputs + 1)
    def predict(self, inputs):
        summation = np.dot(inputs, self.weights[1:]) + self.weights[0]
        if summation > 0:
            activation = 1
        else:
            activation = 0
        return activation
    def train(self, training_inputs, labels):
        for _ in range(self.threshold):                      #s
            for inputs, label in zip(training_inputs, labels):#k
                prediction = self.predict(inputs)                   # O (s k n)
                self.weights[1:] += self.learning_rate * (label - prediction) * inputs
                self.weights[0] += self.learning_rate * (label - prediction)
                


# In[47]:

import numpy as np

training_inputs = []
training_inputs.append(np.array([1, 1]))
training_inputs.append(np.array([1, 0]))
training_inputs.append(np.array([0, 1]))
training_inputs.append(np.array([0, 0]))

labels = np.array([0, 1, 1, 0])

perceptron = Perceptron(2)
perceptron.train(training_inputs, labels)





# In[48]:

inputs = np.array([0, 0])
perceptron.predict(inputs) 


# In[49]:

inputs = np.array([1, 1])
perceptron.predict(inputs) 


# In[50]:

inputs = np.array([0, 1])
perceptron.predict(inputs) 


# In[51]:

inputs = np.array([1, 0])
perceptron.predict(inputs) 


# In[ ]:



