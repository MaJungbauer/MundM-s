# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 18:13:16 2020

@author: marti
"""

import matplotlib.pyplot as plt
import pandas as pd
import documentation


def dataStat(data):
    #print(data)
    #print(len(data))
    statData = data[data.sieger == data.player1]
    #print(len(statData))
    statData = statData[['spielID', 'playerTyp', 'sieger']]
    #print(statData)
    #print(len(statData))
    statData = statData.groupby('spielID').mean()
    #print(statData)
    
    return statData


def siegeComp(data):
    data = data[data.playerTyp == 1]
    if len(data)>0:
        sComp = data.groupby('playerTyp').count()['sieger'][1]
    else:
        sComp = 0
    #print(sComp)
    return sComp

def siegePlay(data):
    data = data[data.playerTyp == 2]
    if len(data)>0:
        sPlay = data.groupby('playerTyp').count()['sieger'][2]
    else:
        sPlay = 0
    #print(sComp)
    return sPlay

def siegeNN(data):
    data = data[data.playerTyp == 3]
    if len(data) >0:
        sNN = data.groupby('playerTyp').count()['sieger'][3]
    else:
        sNN = 0
    #print(sComp)
    return sNN

def anzahlSpiele(data):
    anzahlSpiele = len(data.groupby('spielID').count())
    return anzahlSpiele

if __name__ == '__main__':
    
    #data = pd.read_csv('C:\\Users\\marti\\OneDrive\\Desktop\\4inarowDoku\\4inarow_marti_2020328.csv',
     #                  sep=';')
    
    data = documentation.datenSammeln('C:\\Users\\marti\\OneDrive\\Desktop\\4inarowDoku')
    
    statData = dataStat(data)
    anzahlSpiele = anzahlSpiele(statData)
    #print(str(anzahlSpiele))
    
    genauigkeit = 5
    
    xAchse = [0]
    anteilSiegeComp = [0]
    anteilSiegePlay = [0]
    anteilSiegeNN = [0]
    x = int(anzahlSpiele/genauigkeit)
    
    #print(siegeComp(statData))
    #print(x)
    for i in range(1,x+1):
        xAchse = xAchse + [i*genauigkeit]
        teilData = statData[0:i*genauigkeit]
        anteilSiegeComp = anteilSiegeComp + [siegeComp(teilData)/(i*genauigkeit)]
        anteilSiegePlay = anteilSiegePlay + [siegePlay(teilData)/(i*genauigkeit)]
        anteilSiegeNN = anteilSiegeNN + [siegeNN(teilData)/(i*genauigkeit)]
        plt.plot(xAchse, anteilSiegeComp, label='Siege Computer')
        plt.plot(xAchse, anteilSiegeNN, label='Siege Neuronales Netz')
        plt.plot(xAchse, anteilSiegePlay, label='Siege Player')
        # Legende einblenden:
        plt.legend(loc='upper left', frameon=True)
        plt.show()
        #print(len(teilData))
        
  
    
    
