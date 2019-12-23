# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 22:27:12 2019

@author: marti
"""

from _datetime import datetime
import functions
import player
import computer
import documentation


if __name__ == '__main__':
    #pfad fuer data
    pfad = functions.ertelleDirectory()
    #Es kann gewährt werden, ob player1 oder player2 manuell eingegeben wird, oder ob der der Computer spielen soll
    i = input('Wer ist Spieler 1? (1-->Computer, 2-->Player)  ')
    if int(i) == 1:
        comp1 = True
        levComp1 = int(input('Mit welchem Level soll der Compuer spielen? (1-->leicht, 2-->schwer)  '))
    elif int(i) == 2:
        comp1 = False
    i = input('Wer ist Spieler 2? (1-->Computer, 2-->Player)  ')
    if int(i) == 1:
        comp2 = True
        levComp2 = int(input('Mit welchem Level soll der Compuer spielen? (1-->leicht, 2-->schwer)  '))
    elif int(i) == 2:
        comp2 = False
    #Es kann festgelegt werden, wieviel Spiele hintereinander gespielt werden sollen
    anzahlSpiele = input('Wieviel Spiele sollen gespielt werden?  ')
    for spielNr in range(0, int(anzahlSpiele)):
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
            #wenn player1 computer ist zieht der computer selbstständig, ansonsten wird ein manueller zug abgefragt
            if player1:
                if comp1:
                    zug = computer.zug_bestimmen(spielfeld, player1, levComp1)
                elif not comp1:
                    zug = player.zug_bestimmen(spielfeld, player1)
            elif not player1:
                if comp2:
                    zug = computer.zug_bestimmen(spielfeld, player1, levComp2)
                elif not comp2:
                    zug = player.zug_bestimmen(spielfeld, player1)
            
            #soll der zug doumentiert werden
            doc = documentation.zugDokumentieren(doc, spielID, zugNummer, zug, functions.spielfeld_auffuellen(spielfeld)[0], 1 if player1 else 2)
            #wenn der zug gueltig ist, wird er auf dem spielfeld hinzugefuegt
            spielfeld = functions.ziehen(spielfeld, zug, player1)
            #nach jedem zug wird das spielfeld auf der konsole ausgegeben
            #functions.paintSpielfeld(spielfeld)
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
        print('SpielNr: ' + str(spielNr))
        
        
        
        
        