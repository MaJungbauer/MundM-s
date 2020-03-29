# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 18:21:02 2020

@author: marti
"""


import matplotlib.pyplot as plt
import pandas as pd


def dataStat(data):
    statData = data[data.sieger == data.player1]
    statData = statData[['spielID', 'playerTyp', 'sieger']]
    statData = statData.groupby('spielID').mean()
    
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
    return sPlay

def siegeNN(data):
    data = data[data.playerTyp == 3]
    if len(data) >0:
        sNN = data.groupby('playerTyp').count()['sieger'][3]
    else:
        sNN = 0
    return sNN

def anzahlSpiele(data):
    anzahlSpiele = len(data.groupby('spielID').count())
    return anzahlSpiele

def statistikAnalyse1(data, genauigkeit):
    
    print('Analyse 1')

    statData = dataStat(data)
    anzahlS = anzahlSpiele(statData)
    
    genauigkeit = 5
    
    xAchse = [0]
    anteilSiegeComp = [0]
    anteilSiegePlay = [0]
    anteilSiegeNN = [0]
    x = int(anzahlS/genauigkeit)
    
    #print(siegeComp(statData))
    #print(x)
    for i in range(1,x+1):
        xAchse = xAchse + [i*genauigkeit]
        teilData = statData[0:i*genauigkeit]
        anteilSiegeComp = anteilSiegeComp + [siegeComp(teilData)/(i*genauigkeit)]
        anteilSiegePlay = anteilSiegePlay + [siegePlay(teilData)/(i*genauigkeit)]
        anteilSiegeNN = anteilSiegeNN + [siegeNN(teilData)/(i*genauigkeit)]
        
        #print(len(teilData))
    
    plt.plot(xAchse, anteilSiegeComp, label='Siege Computer')
    plt.plot(xAchse, anteilSiegeNN, label='Siege Neuronales Netz')
    plt.plot(xAchse, anteilSiegePlay, label='Siege Player')
    print('Anzahl Spiele: ' + str(anzahlS))
    print('Anteil Computer: ' + str(round(anteilSiegeComp[-1],2)))
    print('Anteil Player: ' + str(round(anteilSiegePlay[-1],2)))
    print('Anteil Neuronales Netz: ' + str(round(anteilSiegeNN[-1],2)))
    # Legende einblenden:
    plt.legend(loc='upper left', frameon=True)
    plt.show()
    
def statistikAnalyse2(data, genauigkeit):
    
    print('Analyse 2')

    statData = dataStat(data)[-100:]
    anzahlS = anzahlSpiele(statData)
    
    genauigkeit = 5
    
    xAchse = [0]
    anteilSiegeComp = [0]
    anteilSiegePlay = [0]
    anteilSiegeNN = [0]
    x = int(anzahlS/genauigkeit)
    
    #print(siegeComp(statData))
    #print(x)
    for i in range(1,x+1):
        xAchse = xAchse + [i*genauigkeit]
        teilData = statData[0:i*genauigkeit]
        anteilSiegeComp = anteilSiegeComp + [siegeComp(teilData)/(i*genauigkeit)]
        anteilSiegePlay = anteilSiegePlay + [siegePlay(teilData)/(i*genauigkeit)]
        anteilSiegeNN = anteilSiegeNN + [siegeNN(teilData)/(i*genauigkeit)]
        
        #print(len(teilData))
    
    plt.plot(xAchse, anteilSiegeComp, label='Siege Computer')
    plt.plot(xAchse, anteilSiegeNN, label='Siege Neuronales Netz')
    plt.plot(xAchse, anteilSiegePlay, label='Siege Player')
    print('Anzahl Spiele: ' + str(anzahlS))
    print('Anteil Computer: ' + str(round(anteilSiegeComp[-1],2)))
    print('Anteil Player: ' + str(round(anteilSiegePlay[-1],2)))
    print('Anteil Neuronales Netz: ' + str(round(anteilSiegeNN[-1],2)))
    # Legende einblenden:
    plt.legend(loc='upper left', frameon=True)
    plt.show()
  
    
    

    