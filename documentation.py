# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 17:39:31 2019

@author: marti
"""
import os
import pandas as pd
import copy

def doc_anlegen():
    doc = pd.DataFrame(columns=['spielID', 'zugNummer', 'player1', 'spielfeld', 'zug', 'sieger'])
    return doc


def zugDokumentieren(doc, spielID, zugNummer, zug, spielfeld, player1):
    #schreibe den Datensatz in dictionary
    s = copy.copy(spielfeld)
    data = {'spielID': spielID, 'zugNummer': zugNummer, 'zug': zug, 'spielfeld': s,  'player1': player1}
    #umwandeln in Series
    #data = pd.Series(data)
    #Datensatz an DataFrame haengen
    doc = doc.append(data, ignore_index=True)
    
    return doc
    '''
    #wenn es schon eine.csv datei gibt, haenge den datensatz an diese datei
    if os.path.exists(pfad):
        data.to_csv(path_or_buf=pfad,index=False, sep=';', header=False, mode='a')
    #wenn es noch keine .csv datei gibt, erstelle eine neue
    else:
        data.to_csv(path_or_buf=pfad,index=False, sep=';', header=True, mode='w')
        
    '''
    
    
def siegerDokumentieren(doc, sieger):
    #wenn sieger = 1 hat player1 gewonnen
    #wenn sieger = 2 hat player2 gewonnen
    #wenn sieger = 0 ist das spiel unentschieden ausgegangen
    doc['sieger'] = sieger
    return doc

def spielDokumentieren(doc, pfad):
    #wenn es schon eine.csv datei gibt, haenge den datensatz an diese datei
    if os.path.exists(pfad):
        doc.to_csv(path_or_buf=pfad,index=False, sep=';', header=False, mode='a')
    #wenn es noch keine .csv datei gibt, erstelle eine neue
    else:
        doc.to_csv(path_or_buf=pfad,index=False, sep=';', header=True, mode='w')