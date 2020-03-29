# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 17:39:31 2019

@author: marti
"""
import os
import pandas as pd
import copy

#fuer das spiel wird ein neuer dataframe als dokument angelegt
def doc_anlegen():
    doc = pd.DataFrame(columns=['spielID', 'zugNummer', 'player1', 'playerTyp', 'zug', 'spalte_1'
                                , 'spalte_2', 'spalte_3', 'spalte_4', 'spalte_5', 'spalte_6'
                                , 'spalte_7', 'sieger'])
    return doc

#zug wird an das Spiel-Dokument gehaengt
def zugDokumentieren(doc, spielID, zugNummer, zug, spielfeld, player1, playerTyp):
    #schreibe den Datensatz in dictionary
    s = copy.copy(spielfeld)
    data = {'spielID': spielID, 'zugNummer': zugNummer, 'player1': player1, 'playerTyp': playerTyp,
            'zug': zug, 
            'spalte_1': s[0],
            'spalte_2': s[1],
            'spalte_3': s[2],
            'spalte_4': s[3],
            'spalte_5': s[4],
            'spalte_6': s[5],
            'spalte_7': s[6]}
    #Datensatz an DataFrame haengen
    doc = doc.append(data, ignore_index=True)
    
    return doc    
    
#wenn das spiel aus ist, werden an alle Datensaetze des Spiel-Dokuments die INfor, wer gewonnen hat, gehaengt
def siegerDokumentieren(doc, sieger):
    #wenn sieger = 1 hat player1 gewonnen
    #wenn sieger = 2 hat player2 gewonnen
    #wenn sieger = 0 ist das spiel unentschieden ausgegangen
    doc['sieger'] = sieger
    return doc

#das Spiel-Dokument in eine csv schreiben
def spielDokumentieren(doc, pfad, dateiname):
    #wenn es schon eine.csv datei gibt, haenge den datensatz an diese datei
    if os.path.exists(pfad + '\\' + dateiname):
        doc.to_csv(path_or_buf=pfad + '\\' + dateiname,index=False, sep=';', header=False, mode='a')
    #wenn es noch keine .csv datei gibt, erstelle eine neue
    else:
        doc.to_csv(path_or_buf=pfad + '\\' + dateiname,index=False, sep=';', header=True, mode='w')
        
def datenSammeln(pfad):
    data = pd.DataFrame()
    csvList  = os.listdir(pfad)
    for csv in csvList:
        dfCsv = pd.read_csv(pfad + '\\' + csv, sep=';')
        data = data.append(dfCsv, ignore_index=True)
    
    return data
        