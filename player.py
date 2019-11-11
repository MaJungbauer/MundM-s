# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 20:23:08 2019

@author: marti
"""

def zug_bestimmen(spielfeld, player1):
    zug = zugAnfrage(player1)
    #pruefung, ob der zug moeglich ist, ist noch platz in der spalte oder gibt es die spalte
    #der spieler kann so lange ziehen, bis eer einen gueltigen zug macht
    while not pruefeZug(spielfeld, zug, True):
        zug = zugAnfrage(player1)
    return zug
    
    
    
    


#frage den player in welche spalte er werfen will und lese seine eingabe ein
def zugAnfrage(player1):
    print('Player1: ' if player1 else 'Player2: ')
    return int(input('In welche Spalte willst du werfen?  '))


def pruefeZug(spielfeld, spalte, ausgabe):
    #es gibt nur 7 spalten, waehlt der spieler eine groessere nummer ist der zug ungueltig
    if spalte <= 7:
        #in jeder spalte haben nur 6 steine platz
        #will der spieler noch einen stein auf eine volle spalte setzten, ist der zug ungueltig
        if len(spielfeld[spalte - 1]) < 6:
            return True
        else:
            if ausgabe:
                print('---ungueltiger Zug---')
            return False
    else:
        if ausgabe:
            print('---ungueltiger Zug---')
        return False