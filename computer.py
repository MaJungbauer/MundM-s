# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 20:35:13 2019

@author: marti
"""

import functions
import player
import random
import copy

def zug_bestimmen(spielfeld, player1):
    if winInOne(spielfeld, player1)[0]:
        return winInOne(spielfeld, player1)[1]
    elif winInOne(spielfeld, not player1)[0]:
        return winInOne(spielfeld, not player1)[1]
    else:
        zug = random.randint(1,7)
        while not player.pruefeZug(spielfeld, zug, False):
            zug = random.randint(1,7)
        return zug



def winInOne(spielfeld, player1):
    for spalte in range(1,7):
        s = copy.copy(spielfeld)
        zug = spalte
        if player.pruefeZug(s, zug, False):
            s = functions.ziehen(s, zug, player1)
            if functions.pruefeGewinner(s, player1)[0]:
                return [True, zug]
    return [False, 0]


        