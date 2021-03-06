# -*- coding: utf-8 -*-
"""Data Augmentation.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ywLnDaXZe4NRvzfsHJfA5NhdlEN4cXsp
"""

import numpy as np
from matplotlib import pyplot as pd
import PIL
import os
import cv2
import tensorflow as tf
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential

#Downloading dataset
data_url = 'https://storage.googleapis.com/download.tensorflow.org/example_images/flower_photos.tgz'
data = tf.keras.utils.get_file('flower_photos', origin = data_url, cache_dir = '.', untar = True)

data

import pathlib
data = pathlib.Path(data)
data

len(list(data.glob('*/*.jpg')))

roses = list(data.glob('roses/*'))
roses[:7]

PIL.Image.open(str(roses[7]))

sunflowers = list(data.glob('sunflowers/*'))
PIL.Image.open(str(sunflowers[7]))

#Creating data dictionary
flowers = {
    'roses' : list(data.glob('roses/*')),
    'sunflowers' : list(data.glob('sunflowers/*')),
    'tulips' : list(data.glob('tulips/*')),
    'dandelion' : list(data.glob('dandelion/*')),
    'daisy' : list(data.glob('daisy/*')),
}

flower_labels = {
    'roses' : 0,
    'sunflowers' : 1,
    'tulips' : 2,
    'dandelion' : 3,
    'daisy' : 4
}

PIL.Image.open(str(flowers['dandelion'][7]))

#Initiating Open CV2
img = cv2.imread(str(flowers['dandelion'][7]))
img.shape

cv2.resize(img, (180,180)).shape

#Preparing X and Y
x , y = [] , []
for flower, images in flowers.items():
  #print(flower)
  #print(len(images))
  for image in images:
    img = cv2.imread(str(image))
    resized = cv2.resize(img, (180,180))
    x.append(resized)
    y.append(flower_labels[flower])
y[:20]

x = np.array(x)
y = np.array(y)
x.shape

x_scaled = x/255
x_scaled[0]

from sklearn.model_selection import train_test_split
x_tr, x_t, y_tr, y_t = train_test_split(x, y, random_state = 0)

# x_tr_s = x_tr/255
# x_s = x_t/255

#Building Model with CNN
# Training CNN Model
cnn = Sequential([
      #CNN layer 1
      layers.Conv2D(filters = 16, kernel_size = (3,3), activation = 'relu'),
      layers.MaxPooling2D(),
      #CNN layer 2
      layers.Conv2D(filters = 32, kernel_size = (3,3),padding = 'same', activation = 'relu'),
      layers.MaxPooling2D(),
      #CNN layer 3
      layers.Conv2D(filters = 64, kernel_size = (3,3),padding = 'same', activation = 'relu'),
      layers.MaxPooling2D(),
      #Dense
      layers.Flatten(),
      layers.Dense(128, activation = 'relu'),
      #layers.Dense(32, activation = 'relu'),
      layers.Dense(len(flowers))
])

cnn.compile(
    optimizer = 'adam',
    #loss = 'sparse_categorical_crossentropy',
    loss = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
    metrics = ['accuracy']
)

# Commented out IPython magic to ensure Python compatibility.
# %timeit -n -r
cnn.fit(x_tr,y_tr,5)

pred = cnn.predict(x_t)
pred

score = tf.nn.softmax(pred[0])
np.argmax(score)

cnn.evaluate(x_t, y_t)

y_t[0]

#Data Augmentation Code
data_aug = Sequential([
           layers.experimental.preprocessing.RandomFlip('horizontal',input_shape=(180,180,3)),
           layers.experimental.preprocessing.RandomRotation(0.1),
           layers.experimental.preprocessing.RandomZoom(0.1),         
])

#Building Model with CNN
# Training CNN Model
cnn_aug = Sequential([
      #Data Augmentation layer
      data_aug,
      #CNN layer 1
      layers.Conv2D(filters = 16, kernel_size = (3,3),padding='same', activation = 'relu'),
      layers.MaxPooling2D(),
      #CNN layer 2
      layers.Conv2D(filters = 32, kernel_size = (3,3),padding = 'same', activation = 'relu'),
      layers.MaxPooling2D(),
      #CNN layer 3
      layers.Conv2D(filters = 64, kernel_size = (3,3),padding = 'same', activation = 'relu'),
      layers.MaxPooling2D(),
      #Dropout layer
      layers.Dropout(0.25),
      #Dense
      layers.Flatten(),
      layers.Dense(128, activation = 'relu'),
      #layers.Dense(32, activation = 'relu'),
      layers.Dense(len(flowers))
])

cnn_aug.compile(
    optimizer = 'adam',
    #loss = 'sparse_categorical_crossentropy',
    loss = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
    metrics = ['accuracy']
)

# Commented out IPython magic to ensure Python compatibility.
# %timeit -n -r
cnn_aug.fit(x_tr, y_tr, 5)

pred_aug = cnn_aug.predict(x_t)

score = tf.nn.softmax(pred[5])
np.argmax(score)

y_t[5]

