import tensorflow as tf
# To generate GIFs


import glob
import imageio
import matplotlib.pyplot as plt
import numpy as np
import os
import PIL
from PIL import Image,ImageOps
from tensorflow.keras import layers
import time

from IPython import display
print(tf.__version__)

inputFolder = 'w'
imageShape = [300, 300, 1]
def convertImageToNpArray(image):
    image_grey =ImageOps.grayscale(image)
    generated_image = np.array(image_grey)
    generated_image=np.expand_dims(generated_image, axis=2)
    return generated_image
    
def make_discriminator_model():
    model = tf.keras.Sequential()
    model.add(layers.Conv2D(64, (5, 5), strides=(2, 2), padding='same',
                                     input_shape=imageShape))
    model.add(layers.LeakyReLU())
    model.add(layers.Dropout(0.3))

    model.add(layers.Conv2D(128, (5, 5), strides=(2, 2), padding='same'))
    model.add(layers.LeakyReLU())
    model.add(layers.Dropout(0.3))

    model.add(layers.Flatten())
    model.add(layers.Dense(1))

    return model
images = os.listdir(inputFolder)
images.pop(0)
inputs = []
f=0
for i in images:
    image = Image.open(inputFolder+'/'+i)
    inputs.append(convertImageToNpArray(image))
    if(f>0):
        break;
    f+=1

inputs = np.array(inputs)  
print(inputs.shape)
discriminator = make_discriminator_model()
decision = discriminator(inputs)
print (decision)