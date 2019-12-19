# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 14:03:03 2019

@author: messageh
"""
# On crée une calsse Piece 
class Piece:
    def __init__(self, couleur, nature):   
# On a en paramètre la couleur qui est un nombre entre 0 et 1 qui indique si on a l'equipe noire ou l'equipe blanche
        self.couleur = couleur
# La nature correspond au type de la piece et correspond aux calasses Pion, Tour, ...
        self.nature = nature
        
# On crée une methode qui defini tous les mouvements theorique d'une piece en
    def mouvementsPieces(self,nature):
        self.deplacement = []
        if self.nature == Pion :
            if self.couleur == 0:
                self.deplacement = [[-1,0],[-1,-1],[1,-1]]
            elif self.couleur == 1:
                self.deplacement = [[1,0],[1,1],[-1,1]]
                
        elif self.nature == Tour :
            for i in range(-7,7):
                self.deplacement += [[i,0],[0,i]]
                        
        elif self.nature == Cavalier :
            self.deplacement = [[3,1],[3,-1],[1,3],[1,-3],[-3,1],[-3,-1],[-1,3],[-1,-3]]
            
        elif self.nature == Fou :
            for i in range(-7,7):
                    for j in range(-7,7):
                        if i == j :
                            self.deplacement += [i,j]
                            
        elif self.nature == Reine :
            for i in range(-7,7):
                    for j in range(-7,7):
                        if i == j :
                            self.deplacement += [i,j]
            for k in range(-7,7):
                self.deplacement += [[k,0],[0,k]]
                
        elif self.nature == Roi :
            self.deplacement = [[0,1],[0,-1],[1,0],[-1,0],[1,1],[-1,-1],[1,-1],[-1,1]]

    def mouvementsPossibles :
        if self.case.piece != None :
            self.deplacement -= [self.case.x,self.case.y]
        
#1 pour noirs, 0 pour blancs
class Pion(Piece):
    def __init__(self):
        super().__init__()
        self.nom = 'P'
        self.est_a_origine = True
        if self.est_a_origine :
            if self.couleur == 0 :        
                self.mouvementsPieces(Pion).deplacement +=  [-2,0]
            if self.couleur == 1 :
                self.mouvementsPieces(Pion).deplacemnt += [2,0]
    
class Tour:
    def __init__(self):
        self.nom = 'T'
        

class Cavalier:
    def __init__(self):
        self.nom = 'C'

class Fou:
    def __init__(self):
        self.nom = 'F'

         
class Reine:
    def __init__(self,):
        self.nom = 'Q'

    def Mouvement(self):
         pass
         
class Roi:
    def __init__(self):
        self.nom = 'K'

    def Mouvement(self):
        pass