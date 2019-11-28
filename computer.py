# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 20:35:13 2019

@author: marti
"""

import functions
import player
import random
import copy
import pandas as pd

#bestimmt, welchen zug der computer als naechstes waehlt
def zug_bestimmen(spielfeld, player1, level):
    if level == 1:
        return level1(spielfeld, player1)
    elif level == 2:
        return level2(spielfeld, player1)
    
    
    #winInTwoZuege = winInTwo(spielfeld, player1)
    #print(winInTwo)
    
def level1(spielfeld, player1):
    #wenn der computer mit dem naechsten zug gewinnen kann, waehlt er diesen zug, um zu gewinnen
    winnerZug = winInOne(spielfeld, player1)
    lastChanceZug = winInOne(spielfeld, not player1)
    if len(winnerZug) > 0:
        return winnerZug['zug1'][0]
    #wenn der gegener des computers mit dem naechsten zug gewinnen kann, waehlt er diesen zug, um nicht zu verlieren
    elif len(lastChanceZug) > 0:
        return lastChanceZug['zug1'][0]
    else:
        #ansonsten waehlt er einen zufaelligen zug, der moeglich ist
        zug = random.randint(1,7)
        while not player.pruefeZug(spielfeld, zug, False):
            zug = random.randint(1,7)
        return zug
    
    
def level2(spielfeld, player1):
    winnerZug = winInOne(spielfeld, player1)
    lastChanceZug = winInOne(spielfeld, not player1)
    #alle Kombinationen, mit dene
    winInTwoZuege = winInTwo(spielfeld, player1)
    loseInTwoZuege = winInTwo(spielfeld, not player1)
    #wenn der computer mit dem naechsten zug gewinnen kann, waehlt er diesen zug, um zu gewinnen --> Sicherer Sieg
    if len(winnerZug) > 0:
        return winnerZug['zug1'][0]
    #wenn der gegener des computers mit dem naechsten zug gewinnen kann, waehlt er diesen zug, um nicht zu verlieren --> Sichere Niederlage verhindern
    elif len(lastChanceZug) > 0:
        return lastChanceZug['zug1'][0]
    #wenn es mehr als zwei Moeglichkeiten mit WinInTwo gibt, dann waehle diesen Zug --> Sicherer Sieg
    elif len(winInTwoZuege) > 0:
        guteWinInTwoZuege = winInTwoZuege.groupby('zug1').count()
        guteWinInTwoZuege = guteWinInTwoZuege[guteWinInTwoZuege['zug2'] > 1]
        if len(guteWinInTwoZuege) > 0:
            return guteWinInTwoZuege['zug2'].index[0]
    #wenn es mehr als zwei Moeglichkeiten mit LoseInTwo gibt, dann waehle diesen Zug --> Sicherer Niederlage verhindern
    elif len(loseInTwoZuege) > 0:
        guteLoseInTwoZuege = loseInTwoZuege.groupby('zug1').count()
        guteLoseInTwoZuege = guteLoseInTwoZuege[guteLoseInTwoZuege['zug2'] > 1]
        if len(guteLoseInTwoZuege) > 0:
            return guteLoseInTwoZuege['zug2'].index[0]

    #ansonsten waehlt er einen zufaelligen zug, der moeglich ist
    zug = random.randint(1,7)
    while not player.pruefeZug(spielfeld, zug, False):
        zug = random.randint(1,7)
    return zug
    
    
    

#diese Funktion prueft, ob ein Spieler mit dm naesten zug gewinnen kann
def winInOne(spielfeld, player1):
    zuege = pd.DataFrame(columns=['zug1'])
    #laufe durch alle spalten
    for spalte in range(1,8):
        #das spielfeld muss kopiert werden, da nur ein zug simuliert wird, es wird nicht in Wirklichkeit gezogen
        s = copy.copy(spielfeld)
        zug = spalte
        #wenn moeglich, dann in diese spalte werfen
        if player.pruefeZug(s, zug, False):
            s = functions.ziehen(s, zug, player1)
            #pruefe, ob es einen gewinner gibt
            if functions.pruefeGewinner(s, player1)[0]:
                dfZug = pd.DataFrame(columns=['zug1'])
                dfZug['zug1'] = [zug]
                
                zuege = zuege.append(dfZug, ignore_index=True)
                #return [True, zug]
    #print ('WinInOne: ' + str(zuege))
    return zuege


'''
#diese Funktion prueft, ob ein Spieler mit dm naesten zug gewinnen kann
def winInOne(spielfeld, player1):
    zuege = []
    #laufe durch alle spalten
    for spalte in range(0,7):
        #das spielfeld muss kopiert werden, da nur ein zug simuliert wird, es wird nicht in Wirklichkeit gezogen
        s = copy.copy(spielfeld)
        zug = spalte
        #wenn moeglich, dann in diese spalte werfen
        if player.pruefeZug(s, zug, False):
            s = functions.ziehen(s, zug, player1)
            #pruefe, ob es einen gewinner gibt
            if functions.pruefeGewinner(s, player1)[0]:
                zuege = zuege + [zug]
                #return [True, zug]
    return zuege
'''
#gibt alle Kombinationen mit zwei ZUegen zurueck, mit denen der player gewinnen kann
def winInTwo(spielfeld, player1):
    zuege = pd.DataFrame(columns=['zug1', 'zug2'])
    #laufe durch alle spalten
    for spalte in range(1,8):
        #das spielfeld muss kopiert werden, da nur ein zug simuliert wird, es wird nicht in Wirklichkeit gezogen
        s1 = copy.copy(spielfeld)
        zug1 = spalte
        #wenn moeglich, dann in diese spalte werfen
        if player.pruefeZug(s1, zug1, False):
            #ziehe in jede moegliche spalte und pruefe WInInOne
            s1 = functions.ziehen(s1, zug1, player1)
            winnerZug = winInOne(s1, player1)
            #wenn dann WininOne moeglich ist, schreibe die Kombination in einen DataFrame
            for index, z in winnerZug.iterrows():  
                dfZug = pd.DataFrame(columns=['zug1', 'zug2'])
                dfZug['zug1'] = [zug1]
                dfZug['zug2'] = [int(z)]
                zuege = zuege.append(dfZug, ignore_index=True)
            #if len(winnerZug) > 0:   
                #zuege = zuege + [zug1, [winInOne(s1, player1)]]
    return zuege


#diese funktion prueft, ob ein Spieler in X zuegen gewinnen kann
def winInX(X, spielfeld, player1):
    pass
    '''
     #das spielfeld muss kopiert werden, da nur ein zug simuliert wird, es wird nicht in Wirklichkeit gezogen
     s1 = copy.copy(spielfeld)
    for i in range(0,X):
        winInOne(s1, player1)
    '''
    
    


        