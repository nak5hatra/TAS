# -*- coding: utf-8 -*-
"""CNN

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1pU2CdZ8_ptHx3Mu5I5LoUTcgDbhXiRNT
"""

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
# %matplotlib inline
from keras import models
from keras import layers
import keras.preprocessing  as kp
from keras.preprocessing.image import ImageDataGenerator
from keras import regularizers
from keras import optimizers

train_datagen = ImageDataGenerator(
rescale=1./255,
rotation_range=30,
shear_range=0.3,
zoom_range=0.3
)

test_datagen = ImageDataGenerator(rescale=1./255)

train_gen=train_datagen.flow_from_directory('Training/',
                                            target_size=(250,250),
                                            batch_size=48,
                                            class_mode='binary')

valid_gen=test_datagen.flow_from_directory('Validation/',
                                           target_size=(250,250),
                                           batch_size=48,
                                           class_mode='binary')

kernel_s=(3,3)
model=models.Sequential()
model.add(layers.Conv2D(32,kernel_s,activation='relu',input_shape=(250,250,3),
                        kernel_regularizer=regularizers.l2(0.001),padding="VALID"))
model.add(layers.MaxPooling2D((2,2)))

model.add(layers.Conv2D(64,kernel_s,activation='relu'))
model.add(layers.MaxPooling2D((2,2)))
model.add(layers.Conv2D(64,kernel_s,activation='relu'))
model.add(layers.MaxPooling2D((2,2)))

model.add(layers.Conv2D(128,kernel_s,activation='relu'))
model.add(layers.MaxPooling2D((2,2)))
model.add(layers.Conv2D(128,kernel_s,activation='relu'))
model.add(layers.MaxPooling2D((2,2)))

model.add(layers.Flatten())
model.add(layers.Dense(256,activation='relu'))
model.add(layers.Dense(1,activation='sigmoid'))
model.summary()

model.compile(optimizer='rmsprop',loss='binary_crossentropy',metrics=['acc'])

history=model.fit(train_gen,steps_per_epoch=70,epochs=30,
                  validation_data=valid_gen,validation_steps=50)

test_datagen = ImageDataGenerator(rescale=1./255)
test_generator = test_datagen.flow_from_directory(
'Validation/',
target_size=(250,250),
batch_size=64,
class_mode='binary')

test_loss, test_acc = model.evaluate_generator(test_generator, steps=50)
print('test acc:', test_acc)
print('test_loss:',test_loss)

