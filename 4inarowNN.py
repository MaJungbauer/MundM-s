# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 16:56:22 2019

@author: marti
"""

import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd



if __name__ == '__main__':
    
    data = pd.read_csv('C:\\Users\\marti\\OneDrive\\Desktop\\4inarowDoku\\4inarow_marti_20191215.csv',
                       sep=';')
    
    data = data[data.player1 == data.sieger]
    
    #train_spielfeld  = pd.Series()
    
    train_spielfeld = data[0:int(len(data)/2)]['spielfeld']
    train_zuege = data[0:int(len(data)/2)]['zug']
    test_spielfeld = data[int(len(data)/2):]['spielfeld']
    test_zuege = data[int(len(data)/2):]['zug']
    
    class_names = ['Spalte 1', 'Spalte 2', 'Spalte 3', 'Spalte 4', 
                   'Spalte 5', 'Spalte 6', 'Spalte 7']
    
    train_spielfeld = train_spielfeld/7.0
    test_spielfeld = test_spielfeld/7.0
    
    model = keras.Sequential([
            keras.layers.Flatten(input_shape=(6, 7)),
            keras.layers.Dense(128, activation='relu'),
            keras.layers.Dense(7, activation='softmax')
            ])
    
    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    
    model.fit(train_spielfeld, train_zuege, epochs=5)
    
    prediction = model.predict(test_spielfeld)
    
    '''
    for i in range(5):
        plt.grid(False)
        plt.imshow(test_images[i], cmap=plt.cm.binary)
        plt.xlabel('Actual: ' + class_names[test_labels[i]])
        plt.title('Prediction ' + class_names[np.argmax(prediction[i])])
        plt.show()
    '''