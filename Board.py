# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""
import numpy as np
from Pieces import Piece
from Cases import Case

class Board:
    #le joueur jour toujours les blancs et se trouve en bas de l'ecran au debut
    def __init__(self):
        self.plateau = np.empty((8, 8), Case)
        
    def getplateau(self):
        return self.plateau
  

      

       