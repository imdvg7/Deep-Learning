# -*- coding: utf-8 -*-
"""ANN vs CNN.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1WDK33LX6m3wAcV3DX6evHQ8hIsYMUg7f
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import tensorflow as tf
from tensorflow.keras import datasets as ds, models

(x_tr,y_tr),(x_t,y_t) = ds.cifar10.load_data()

x_tr.shape

x_tr[0]

y_tr[:7]

y_tr = y_tr.reshape(-1,)
y_tr[:7]

classes = ['airplanes', 'automobiles', 'bird', 'cat','deer','dog','frog','horse','ship','truck']

def plot_img(x,y,index):
  plt.figure(figsize=(15,2))
  plt.imshow(x[index])
  plt.xlabel(classes[y[index]])

plot_img(x_t,y_t,9)

#Data Normalization
x_tr = x_tr / 255
x_t = x_t / 255

x_tr[1] #values came in the range of 0 to 1

#First training the ANN Model
ann = model = keras.Sequential([
              keras.layers.Flatten(input_shape=(32,32,3)),
              keras.layers.Dense(3000, activation = 'relu'),
              keras.layers.Dense(1000, activation = 'relu'),
              keras.layers.Dense(10, activation = 'sigmoid') ])

# Commented out IPython magic to ensure Python compatibility.
#Compiling ann
# %timeit -n -r
ann.compile( optimizer = 'adam', loss ='sparse_categorical_crossentropy', metrics = ['accuracy'])
ann.fit(x_tr,y_tr, epochs = 1) #epochs can be given more its just provided low due to low computational power

ann.evaluate(x_t,y_t)

from sklearn.metrics import confusion_matrix, classification_report
y_pred = ann.predict(x_t)
y_pred_classes = [np.argmax(element) for element in y_pred]
print(f'Classification Report :\n {classification_report(y_t,y_pred_classes)}')

# Training CNN Model
cnn = models.Sequential([
      #CNN layer 1
      keras.layers.Conv2D(filters = 32, kernel_size = (3,3), activation = 'relu', input_shape=(32,32,3)),
      keras.layers.MaxPooling2D((2,2)),
      #CNN layer 2
      keras.layers.Conv2D(filters = 64, kernel_size = (3,3), activation = 'relu'),
      keras.layers.MaxPooling2D((2,2)),
      #Dense
      keras.layers.Flatten(),
      keras.layers.Dense(64, activation = 'relu'),
      #keras.layers.Dense(32, activation = 'relu'),
      keras.layers.Dense(10, activation = 'softmax')
])

cnn.compile(optimizer='adam', loss= 'sparse_categorical_crossentropy', metrics= ['accuracy'])

# Commented out IPython magic to ensure Python compatibility.
# %timeit -n -r
cnn.fit(x_tr,y_tr,epochs=1) #epochs can be given more its just provided low due to low computational power

cnn.evaluate(x_t,y_t)

y_pred_cnn = cnn.predict(x_t)
y_pred_classes_cnn = [np.argmax(element) for element in y_pred_cnn]
print(f'Classification Report :\n {classification_report(y_t,y_pred_classes_cnn)}')

plot_img(x_t,y_t,9)

classes[y_pred_classes_cnn[9]]
