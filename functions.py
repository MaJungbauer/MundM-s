# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 16:41:11 2019

@author: marti

"""
import getpass
import os
from _datetime import datetime

#erstellt den Ordner fuer die doku nur wenn der ordner noch nicht existiert
def ertelleDirectory():
    user = getpass.getuser()
    directory = 'C:\\Users\\' + user + '\\OneDrive\\Desktop\\4inarowDoku'
    if not os.path.isdir(directory):
        os.mkdir(directory)
    date = str(datetime.now().year) + str(datetime.now().month) + str(datetime.now().day)
    path = directory + '\\4inarow_' + user + '_' + date + '.csv'
    
    return path

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


#um zu ziehen wird in die liste (spalte, in der der player gezogen hat, ein element hinzugefuegt
#1 steht fuer player1, 2 fuer player2
def ziehen(spielfeld, spalte, player1):
    spielfeld[spalte - 1] = spielfeld[spalte - 1] + [1 if player1 else 2]
    return spielfeld




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
    
def pruefeGewinner(spielfeld, player1):
    s = spielfeld_auffuellen(spielfeld)
    #es gibt 4 moeglichkeiten 4 in a row zu haben: horizontal, vertical, diagonal und reverse diagonal
    #fuer jede moeglichkeit gibt es eine liste, in der alle reihen abgelegt sind
    vertical = s[0]
    horizontal = s[1]
    diagonal = s[2]
    reverseDiagonal = s[3]
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


def spielfeld_auffuellen(spielfeld):
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
    return  [vertical, horizontal, diagonal, reverseDiagonal]