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
import neuralNetwork
import getpass

from tensorflow import keras
import numpy as np



if __name__ == '__main__':
    
    #pfad fuer data
    user = getpass.getuser()
    pfad = functions.ertelleDirectory('C:\\Users\\' + user + '\\OneDrive\\Desktop\\4inarowDoku', user)
    dateiname = functions.erstelleDateiname(user)
    #lerne Neurales Netz zum erten mal an
    model = neuralNetwork.lernNN(pfad)
    #Es kann gewährt werden, ob player1 oder player2 manuell eingegeben wird, oder ob der der Computer spielen soll
    p1 = input('Wer ist Spieler 1? (1-->Computer, 2-->Player, 3--> Neuronales Netz)  ')
    if int(p1) == 1:
        levComp1 = int(input('Mit welchem Level soll der Compuer spielen? (1-->leicht, 2-->schwer)  '))
    p2 = input('Wer ist Spieler 2? (1-->Computer, 2-->Player, 3--> Neuronales Netz)  ')
    if int(p2) == 1:
        levComp2 = int(input('Mit welchem Level soll der Compuer spielen? (1-->leicht, 2-->schwer)  '))
    #Es kann festgelegt werden, wieviel Spiele hintereinander gespielt werden sollen
    anzahlSpiele = input('Wieviel Spiele sollen gespielt werden?  ')
    spielfeld_zeichnen = input('Soll das Spielfeld angezeigt werden? (1-->ja, 0-->nein) ')
    
    for spielNr in range(0, int(anzahlSpiele)):
        #alle 100 Spiele wird das NN neu angelernt
        if spielNr % 100 == 0:
            model = neuralNetwork.lernNN(pfad)
        #Datensaetze zaehlen
        print('SpielNr: ' + str(spielNr))
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
                if int(p1) == 1:
                    zug = computer.zug_bestimmen(spielfeld, player1, levComp1)
                elif int(p1) == 2:
                    zug = player.zug_bestimmen(spielfeld, player1)
                elif int(p1) == 3:
                    #s = functions.spielfeld_to_numpy(spielfeld)
                    #s = s/7.0
                    zug = neuralNetwork.zug_bestimmen(spielfeld, model)
                    #print(zug)
                    
            elif not player1:
                if int(p2) == 1:
                    zug = computer.zug_bestimmen(spielfeld, player1, levComp2)
                elif int(p2) == 2:
                    zug = player.zug_bestimmen(spielfeld, player1)
                elif int(p2) == 3:
                    #s = functions.spielfeld_to_numpy(spielfeld)
                    #s = s/7.0
                    zug = neuralNetwork.zug_bestimmen(spielfeld, model)
                    #print(zug)
                    
            #soll der zug doumentiert werden
            doc = documentation.zugDokumentieren(doc, spielID, zugNummer, zug, functions.spielfeld_auffuellen(spielfeld)[0], 1 if player1 else 2, p1 if player1 else p2)
            #wenn der zug gueltig ist, wird er auf dem spielfeld hinzugefuegt
            
            spielfeld = functions.ziehen(spielfeld, zug, player1)
            #nach jedem zug wird das spielfeld auf der konsole ausgegeben
            if int(spielfeld_zeichnen) == 1:
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
        documentation.spielDokumentieren(doc, pfad, dateiname)
        
        
        
        
        
        