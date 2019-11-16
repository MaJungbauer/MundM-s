# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 22:27:12 2019

@author: martin
"""

import getpass
from _datetime import datetime
import functions
import player
import computer
import documentation


if __name__ == '__main__':
    #pfad fuer data
    date = str(datetime.now().year) + str(datetime.now().month) + str(datetime.now().day)
    user = getpass. getuser()
    pfad = 'C:\\Python_scripts\\4Gewinnt\\4inarow_' + user + '_' + date + '.csv'
    i = input('Wer ist Spieler 1? (1-->Computer, 2-->Player)  ')
    if int(i) == 1:
        comp1 = True
    elif int(i) == 2:
        comp1 = False
    i = input('Wer ist Spieler 2? (1-->Computer, 2-->Player)  ')
    if int(i) == 1:
        comp2 = True
    elif int(i) == 2:
        comp2 = False
    if comp1:
        if comp2:
            anzahlSpiele = 1000
        else:
            anzahlSpiele = 1
    else:
        anzahlSpiele = 1
    for spielNr in range(0, anzahlSpiele):
        spielID = str(datetime.now())
        #spielfeld ist eine liste mit sieben einzelnen listen, jede fuer eine spalte
        #die spalten im spielfeld werden pro zug mit 1 oder 2 gefuellt
        spielfeld = [[],[],[],[],[],[],[]]
        doc = documentation.doc_anlegen()
        #pro spiel kann man max 42x ziehen, dann ist das spielfeld voll
        for zugNummer in range(0,42):
            #player1 faengt an 
            #--> jede gerade zahl ist ein zug von player1, eine ungerade ein zug von player2
            player1 = True if (zugNummer % 2) == 0 else False
            if player1:
                if comp1:
                    zug = computer.zug_bestimmen(spielfeld, player1)
                elif not comp1:
                    zug = player.zug_bestimmen(spielfeld, player1)
            elif not player1:
                if comp2:
                    zug = computer.zug_bestimmen(spielfeld, player1)
                elif not comp2:
                    zug = player.zug_bestimmen(spielfeld, player1)
            
            #soll der zug doumentiert werden
            doc = documentation.zugDokumentieren(doc, spielID, zugNummer, zug, spielfeld, 1 if player1 else 2)
            #wenn der zug gueltig ist, wird er auf dem spielfeld hinzugefuegt
            spielfeld = functions.ziehen(spielfeld, zug, player1)
            #nach jedem zug wird das spielfeld auf der konsole ausgegeben
            functions.paintSpielfeld(spielfeld)
            #nach jedem zug wird geprueft, ob es einen gewinner gibt
            gewinner = functions.pruefeGewinner(spielfeld, player1)
            #wenn es einen gewinner gibt, wird die Info ausgegeben, es erfolgen dann keine weiteren zuege
            if gewinner[0]:
                print('---' + ('Player1' if gewinner[1] else 'Player2') + ' hat gewonnen---' )
                doc = documentation.siegerDokumentieren(doc, 1 if gewinner[1] else 2)
                break
        #gibt es nach 42 zuegen keinen gewinner, ist das spielfeld voll und es ist unentschieden
        if not gewinner[0]:
            print('---unentschieden---')
            doc = documentation.siegerDokumentieren(doc, 0)
        #Spiel dokumentieren
        documentation.spielDokumentieren(doc, pfad)
        
        
        
        
        