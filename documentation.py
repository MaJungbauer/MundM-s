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
    doc = pd.DataFrame(columns=['spielID', 'zugNummer', 'player1', 'spielfeld', 'zug', 'sieger'])
    return doc

#zug wird an das Spiel-Dokument gehaengt
def zugDokumentieren(doc, spielID, zugNummer, zug, spielfeld, player1):
    #schreibe den Datensatz in dictionary
    s = copy.copy(spielfeld)
    data = {'spielID': spielID, 'zugNummer': zugNummer, 'zug': zug, 'spielfeld': s,  'player1': player1}
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
def spielDokumentieren(doc, pfad):
    #wenn es schon eine.csv datei gibt, haenge den datensatz an diese datei
    if os.path.exists(pfad):
        doc.to_csv(path_or_buf=pfad,index=False, sep=';', header=False, mode='a')
    #wenn es noch keine .csv datei gibt, erstelle eine neue
    else:
        doc.to_csv(path_or_buf=pfad,index=False, sep=';', header=True, mode='w')