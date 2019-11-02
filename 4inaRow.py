# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 22:27:12 2019

@author: martin
"""

import os
import getpass
from _datetime import datetime
import pandas as pd



def printColoredString(s):
    #trennen alle zeichen des strings und schreibe sie in eine liste
    x=list(s)
    for ele in x:
        #wenn ein element = 1 oder 2 schreibe es farbig
        if ele == '1':
            print('[1;31;41m'+ ele +'[0m', end='')
        elif ele == '2':
            print('[1;34;44m'+ ele +'[0m', end='')
        else:
            print(ele, end='')
    print('', end='\n')

#diese funktion listet alle farben in der konsole auf, die moeglich sind
'''
def print_format_table():
    """
    prints table of formatted text format options
    """
    for style in range(8):
        for fg in range(30,38):
            s1 = ''
            for bg in range(40,48):
                format = ';'.join([str(style), str(fg), str(bg)])
                s1 += '\x1b[%sm %s \x1b[0m' % (format, format)
            print(s1)
        print('\n')

print_format_table()
'''


def zugWegschreiben(pfad, zugNummer, zug, spielfeld, player1):
    #schreibe den Datensatz in einen dataFrame
    data = pd.DataFrame()
    data['zugNummer'] = [zugNummer]
    data['zug'] = [zug]
    data['spielfeld'] = [spielfeld]
    data['player1'] = [player1]
    #wenn es schon eine.csv datei gibt, haenge den datensatz an diese datei
    if os.path.exists(pfad):
        data.to_csv(path_or_buf=pfad,index=False, sep=';', header=False, mode='a')
    #wenn es noch keine .csv datei gibt, erstelle eine neue
    else:
        data.to_csv(path_or_buf=pfad,index=False, sep=';', header=True, mode='w')
    
    
    
def pruefeGewinner(spielfeld, player1):
    #baue neue liste, analog zum spielfeld und fuelle alle felder, die noch nicht belegt sind mit 0 auf
    s = []
    for x in range(0,7):
        t = []
        for y in range(0,6):
            t = t + [0]
            if len(spielfeld[x]) > y:
                if spielfeld[x][y] == 1 or spielfeld[x][y] == 2:
                     t[y] = spielfeld[x][y]
        s = s + [t]
    #es gibt 4 moeglichkeiten 4 in a row zu haben: horizontal, vertical, diagonal und reverse diagonal
    #fuer jede moeglichkeit gibt es eine liste, in der alle reihen abgelegt sind
    vertical = s
    horizontal = [[s[0][0],s[1][0],s[2][0],s[3][0],s[4][0],s[5][0],s[6][0]],
                  [s[0][1],s[1][1],s[2][1],s[3][1],s[4][1],s[5][1],s[6][1]],
                  [s[0][2],s[1][2],s[2][2],s[3][2],s[4][2],s[5][2],s[6][2]],
                  [s[0][3],s[1][3],s[2][3],s[3][3],s[4][3],s[5][3],s[6][3]],
                  [s[0][4],s[1][4],s[2][4],s[3][4],s[4][4],s[5][4],s[6][4]],
                  [s[0][5],s[1][5],s[2][5],s[3][5],s[4][5],s[5][5],s[6][5]]]
    diagonal = [[s[0][5]],
                [s[0][4],s[1][5]],
                [s[0][3],s[1][4],s[2][5]],
                [s[0][2],s[1][3],s[2][4],s[3][5]],
                [s[0][1],s[1][2],s[2][3],s[3][4],s[4][5]],
                [s[0][0],s[1][1],s[2][2],s[3][3],s[4][4],s[5][5]],
                [s[1][0],s[2][1],s[3][2],s[4][3],s[5][4],s[6][5]],
                [s[2][0],s[3][1],s[4][2],s[5][3],s[6][4]],
                [s[3][0],s[4][1],s[5][2],s[6][3]],
                [s[4][0],s[5][1],s[6][2]],
                [s[5][0],s[6][1]],
                [s[6][0]]]
    reverseDiagonal = [[s[0][0]],
                [s[0][1],s[1][0]],
                [s[0][2],s[1][1],s[2][0]],
                [s[0][3],s[1][2],s[2][1],s[3][0]],
                [s[0][4],s[1][3],s[2][2],s[3][1],s[4][0]],
                [s[0][5],s[1][4],s[2][3],s[3][2],s[4][1],s[5][0]],
                [s[1][5],s[2][4],s[3][3],s[4][2],s[5][1],s[6][0]],
                [s[2][5],s[3][4],s[4][3],s[5][2],s[6][1]],
                [s[3][5],s[4][4],s[5][3],s[6][2]],
                [s[4][5],s[5][4],s[6][3]],
                [s[5][5],s[6][4]],
                [s[6][5]]]
    #pruefe, ob eine der 4 listen 4 elemente der gleichen auspraegung haben
    #wenn ja, dann haben wir einen gewinner
    gewinner = pruefe4inARow(vertical)
    if not gewinner:
        gewinner = pruefe4inARow(horizontal)
        if not gewinner:
            gewinner = pruefe4inARow(diagonal)
            if not gewinner:
                gewinner = pruefe4inARow(reverseDiagonal)
    #gebe die nachricht des sieges und den player, der gewonnen hat zurueck
    return [gewinner, player1]

def pruefe4inARow(vektor):
    #laufe durch jede liste 
    for vek in vektor:
        #man kann nur 4 in a row haben, wenn in der liste mindestens 4 elemente sind
        if len(vek) >= 4:
            #laufe ducrh alle elemente der liste - nur bis zum 4.-letzten
            #das 3.-letzte kann nicht das erste element von 4 in a row sein
            for x in range(0, len(vek) - 3):
                #pruefe nur elemente, die unglaich 0 (also gefuellt sind)
                if not vek[x] == 0:
                    #merke dir das erste element
                    y = vek[x]
                    #wenn die folgenden elemente die gleichen sind, haben iwr 4 in a row
                    if vek[x+1] == y:
                        if vek[x+2] == y:
                            if vek[x+3] == y:
                                return True
                            else:
                                continue
                        else:
                            continue
                    else:
                        continue
    return False

#um zu ziehen wird in die liste (spalte, in der der player gezogen hat, ein element hinzugefuegt
#1 steht fuer player1, 2 fuer player2
def ziehen(spielfeld, spalte, player1):
    spielfeld[spalte - 1] = spielfeld[spalte - 1] + [1 if player1 else 2]
    return spielfeld

def pruefeZug(spielfeld, spalte):
    #es gibt nur 7 spalten, waehlt der spieler eine groessere nummer ist der zug ungueltig
    if spalte <= 7:
        #in jeder spalte haben nur 6 steine platz
        #will der spieler noch einen stein auf eine volle spalte setzten, ist der zug ungueltig
        if len(spielfeld[spalte - 1]) < 6:
            return True
        else:
            print('---ungueltiger Zug---')
            return False
    else:
        print('---ungueltiger Zug---')
        return False

#frage den player in welche spalte er werfen will und lese seine eingabe ein
def zugAnfrage(player1):
    print('Player1: ' if player1 else 'Player2: ')
    return int(input('In welche Spalte willst du werfen?  '))
    
#zeichnet das spielfald auf der konsole
def paintSpielfeld(spielfeld):
    str1 = ''
    str2 = ''
    str3 = ''
    str4 = ''
    str5 = ''
    str6 = ''
    print(' _  _  _  _  _  _  _ ')
    #laufe durch jede spalte baue einen string mit dem ersten element (unterste zeile), dem zweiten element (zweitunterste zeile)...
    #wenn auf der position ein stein liegt, fuege ihn dem string hinzu, ansonsten setzt ein leerzeichen
    for spalte in spielfeld:
        if len(spalte) >= 1:
            str1 = str1 + (' ' + str(spalte[0]) + ' ') if spalte[0] > 0 else '   '
        else:
            str1 = str1 + '   '
        if len(spalte) >= 2:
            str2 = str2 + (' ' + str(spalte[1]) + ' ') if spalte[1] > 0 else '   '
        else:
            str2 = str2 + '   '
        if len(spalte) >= 3:
            str3 = str3 + (' ' + str(spalte[2]) + ' ') if spalte[2] > 0 else '   '
        else:
            str3 = str3 + '   '
        if len(spalte) >= 4:
            str4 = str4 + (' ' + str(spalte[3]) + ' ') if spalte[3] > 0 else '   '
        else:
            str4 = str4 + '   '
        if len(spalte) >= 5:
            str5 = str5 + (' ' + str(spalte[4]) + ' ') if spalte[4] > 0 else '   '
        else:
            str5 = str5 + '   '
        if len(spalte) >= 6:
            str6 = str6 + (' ' + str(spalte[5]) + ' ') if spalte[5] > 0 else '   '
        else:
            str6 = str6 + '   '
    #zeichne alle strings (zeilen) von der obersten bis zur untersten
    printColoredString(str6)
    printColoredString(str5)
    printColoredString(str4)
    printColoredString(str3)
    printColoredString(str2)
    printColoredString(str1)
    
    print(' _  _  _  _  _  _  _ ')
    print(' 1  2  3  4  5  6  7 ')
    

if __name__ == '__main__':
    #pfad fuer data
    date = str(datetime.now().year) + str(datetime.now().month) + str(datetime.now().day)
    user = getpass. getuser()
    pfad = 'C:\\Python_scripts\\4Gewinnt\\4inarow_' + user + '_' + date + '.csv'
    #print (os.environ['desktop'])
    #spielfeld ist eine liste mit sieben einzelnen listen, jede fuer eine spalte
    #die spalten im spielfeld werden pro zug mit 1 oder 2 gefuellt
    spielfeld = [[],[],[],[],[],[],[]]
    #pro spiel kann man max 42x ziehen, dann ist das spielfeld voll
    for zugNummer in range(0,42):
        #player1 faengt an 
        #--> jede gerade zahl ist ein zug von player1, eine ungerade ein zug von player2
        player1 = True if (zugNummer % 2) == 0 else False
        #liest die spalte ein, in die ein spieler werfen will
        zug = zugAnfrage(player1)
        #pruefung, ob der zug moeglich ist, ist noch platz in der spalte oder gibt es die spalte
        #der spieler kann so lange ziehen, bis eer einen gueltigen zug macht
        while not pruefeZug(spielfeld, zug):
            zug = zugAnfrage(player1)
        #soll der zug doumentiert werden
        zugWegschreiben(pfad, zugNummer, zug, spielfeld, player1)
        #wenn der zug gueltig ist, wird er auf dem spielfeld hinzugefuegt
        spielfeld = ziehen(spielfeld, zug, player1)
        #nach jedem zug wird das spielfeld auf der konsole ausgegeben
        paintSpielfeld(spielfeld)
        #nach jedem zug wird geprueft, ob es einen gewinner gibt
        gewinner = pruefeGewinner(spielfeld, player1)
        #wenn es einen gewinner gibt, wird die Info ausgegeben, es erfolgen dann keine weiteren zuege
        if gewinner[0]:
            print('---' + ('Player1' if gewinner[1] else 'Player2') + ' hat gewonnen---' )
            break
    #gibt es nach 42 zuegen keinen gewinner, ist das spielfeld voll und es ist unentschieden
    if not gewinner[0]:
        print('---unentschieden---')

        
        
        
        
        