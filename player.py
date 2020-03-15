# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 20:23:08 2019

@author: marti
"""

import functions as fc

def zug_bestimmen(spielfeld, player1):
    zug = zugAnfrage(player1) - 1
    #pruefung, ob der zug moeglich ist, ist noch platz in der spalte oder gibt es die spalte
    #der spieler kann so lange ziehen, bis eer einen gueltigen zug macht
    while not fc.pruefeZug(spielfeld, zug, True):
        zug = zugAnfrage(player1)
    return zug
    
    
    
    


#frage den player in welche spalte er werfen will und lese seine eingabe ein
def zugAnfrage(player1):
    print('Player1: ' if player1 else 'Player2: ')
    return int(input('In welche Spalte willst du werfen?  '))


