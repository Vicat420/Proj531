# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 15:07:27 2019

@author: forestay
"""


class Case:
    
    def __init__(self, y, x, piece):
        self.piece = piece
        self.colonne = x
        self.ligne = y