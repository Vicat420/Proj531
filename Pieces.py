# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 15:07:26 2019

@author: forestay
"""

class Piece:
     
    def __init__(self, couleur, nature):
        self.couleur = couleur
        self.nature = nature



#1 pour noirs, 0 pour blancs
class Pion:
    def __init__(self):
        self.est_a_origine = True
    
#liste complete des mvts possibles d'un pion, sans se soucier de la faisabilite
    def Mouvement(self):
        if self.couleur == 0:
            self.deplacement = [[0,-1],[-1,-1],[-1,1],[0,-2]]
        elif self.couleur == 1:
            self.deplacement = [[0,-1],[-1,-1],[-1,1],[0,-2]]
    
    
class Tour:
    def __init__(self):
        pass
    def Mouvement(self):
        pass
    
class Cavalier:
    def __init__(self):
        pass
    def Mouvement(self):
        pass
        
class Fou:
    def __init__(self):
        pass
    def Mouvement(self):
        pass
         
class Reine:
    def __init__(self):
        pass
    def Mouvement(self):
         pass
         
class Roi:
    def __init__(self):
        pass
    def Mouvement(self):
        pass
         