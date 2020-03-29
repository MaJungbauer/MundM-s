# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 10:13:27 2020

@author: marti
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 16:56:22 2019

@author: marti
"""

#import tensorflow as tf
from tensorflow import keras
import numpy as np
#import matplotlib.pyplot as plt
import pandas as pd
import functions as fc
import random as rd
import documentation
#import functions


#neuronales Netz anlernen
def lernNN(data):
    
    model = fourinARowNN(data)
    return model

#frage den player in welche spalte er werfen will und lese seine eingabe ein
def zugAnfrage(spielfeld, model):
    zug = np.argmax(model.predict(fc.spielfeld_to_numpy(spielfeld)/7.0))
    return zug

def zug_bestimmen(spielfeld, model):
    zug = zugAnfrage(spielfeld, model)
    #pruefung, ob der zug moeglich ist, ist noch platz in der spalte oder gibt es die spalte
    #der spieler kann so lange ziehen, bis eer einen gueltigen zug macht
    while not fc.pruefeZug(spielfeld, zug, False):
        #print('NN gibt ungueltigen Zug aus!')
        zug = rd.randint(0,6)
        
    return zug



def str_to_Numpy(feld):
    feld = feld.replace(', ', '')
    feld = feld.replace('[', '')
    feld = feld.replace(']', '')
    arr = np.array(list(feld), dtype=np.uint8)
    return arr
    
    
    


def fourinARowNN(data_source):
    
    #'C:\\Users\\marti\\OneDrive\\Desktop\\4inarowDoku\\4inarow_marti_2020118.csv'
    #data = pd.read_csv(data_source,
     #                  sep=';')
    data = data_source[data_source.player1 == data_source.sieger]
    #data = data.reindex(range(0,len(data)))
    
    data_zuege = np.zeros(len(data), dtype=np.uint8)
    data_spieler = np.zeros(len(data), dtype=np.uint8)
    data_spielfeld = np.zeros((len(data),7,6), dtype=np.uint8)
    i = 0
    for index, row in data.iterrows():
        data_zuege[i] = int(row['zug'])
        data_spieler[i] = int(row['player1'])
        for spalte in range(0,6):
            arr = str_to_Numpy(row['spalte_'+str(spalte+1)])
            for zeile in range(0,5):
                wert = arr[zeile]
                data_spielfeld[i][spalte][zeile] = wert
        i = i+1
        
    train_spielfeld = data_spielfeld[0:int(len(data_spielfeld)/2)]
    train_zuege = data_zuege[0:int(len(data_zuege)/2)]
    
    test_spielfeld = data_spielfeld[int(len(data_spielfeld)/2):]
    test_zuege = data_zuege[int(len(data_zuege)/2):]
        
    class_names = ['Spalte 1', 'Spalte 2', 'Spalte 3', 'Spalte 4', 
                   'Spalte 5', 'Spalte 6', 'Spalte 7']
    
    train_spielfeld = train_spielfeld/7.0
    test_spielfeld = test_spielfeld/7.0
    
    model = keras.Sequential([
            keras.layers.Flatten(input_shape=(7, 6)),
            keras.layers.Dense(128, activation='relu'),
            keras.layers.Dense(7, activation='softmax')
            ])
    
    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    
    model.fit(train_spielfeld, train_zuege, epochs=10)
    
    return model
    
    #prediction = model.predict(test_spielfeld)
    '''
    for i in range(5):
        plt.grid(False)
        plt.imshow(test_images[i], cmap=plt.cm.binary)
        plt.xlabel('Actual: ' + class_names[test_labels[i]])
        plt.title('Prediction ' + class_names[np.argmax(prediction[i])])
        plt.show()
    '''
    '''
    for i in range(20):
        #print(data_spielfeld[i])
        print('---------------------')
        print('Spielfeld: ')
        functions.paintSpielfeld(data_spielfeld[i])
        print('Spieler: ' + str(data_spieler[i]))
        print('Zug: Spalte ' + str(data_zuege[i]))
        print('Netz: ' + class_names[np.argmax(prediction[i])])
        print('---------------------')
    '''
        
    
    
    
    