
import copy
import pygame
import numpy as np
from Pieces import Piece
from Cases import Case

class Board:
    #le joueur jour toujours les blancs et se trouve en bas de l'ecran au debut
    def __init__(self):
        self.plateau = np.empty((8, 8), Case)
        self.couleur_jouee = 0
        self.piece_selectionnee = None
        self.case_selectionnee = None
        self.cases_selectionnables = []
        self.screen = pygame.display.set_mode((600,600))
        self.chess = pygame.image.load("chess.gif")
        self.position_rois = [[7,3],[0,3]]

    #getter
    def get_plateau(self):
        return self.plateau
  
    #on selectionne une case avec ses coordonnees
    def selectionner_case(self,y,x):
        if [y,x] in self.cases_selectionnables :
            self.get_plateau()[y,x].piece = self.piece_selectionnee
            self.get_plateau()[self.case_selectionnee[0],self.case_selectionnee[1]].piece = None
            if self.piece_selectionnee.nature.nom == 'R' :
                position_rois[piece_selectionnee.couleur] = [y,x]
            self.couleur_jouee = 1 - self.couleur_jouee
            self.cases_selectionnables = []
            self.piece_selectionnee = None
            self.case_selectionnee = None
            
        elif self.get_plateau()[y,x].piece == None :
            pass
        
        elif self.get_plateau()[y,x].piece.couleur == self.couleur_jouee :
            self.piece_selectionnee = self.get_plateau()[y,x].piece
            self.case_selectionnee = [y,x]
            self.cases_selectionnables = self.verifie_echec(self.piece_selectionnee.nature.deplacements(y,x,self.couleur_jouee,self))

    def display(self):
        self.screen.fill((0,0,0))
        self.screen.blit(self.chess,(0,0))
        self.draw_cases_selectionnables(self.cases_selectionnables)
        for k in self.get_plateau():
            for case in k:
                if case.piece != None :
                    case.draw_piece(self)
        pygame.display.flip()

    def clic_to_case(self,pos):
        if (36 < pos[0]< 564) and (36 <= pos[1] <= 564):
            case_x = (pos[0]-36)//66
            case_y = (pos[1]-36)//66
            self.selectionner_case(case_y,case_x)

    def draw_cases_selectionnables(self, cases_a_colorier):
        for case in cases_a_colorier :
            pygame.draw.rect(self.screen, (0,255,0), [case[1]*66+36, case[0]*66+36, 66, 66])

    def verifie_echec(self, liste_cases):
        Liste_possible = []
        for case in liste_cases :
            board_copie = self.copier()
            board_copie.get_plateau()[case[0], case[1]].piece = self.piece_selectionnee
            board_copie.get_plateau()[self.case_selectionnee[0], self.case_selectionnee[1]].piece = None
            if board_copie.roi_en_echec(self.couleur_jouee) == False:
                Liste_possible += [case]
        return Liste_possible

    def roi_en_echec(self, couleur):
        for i in range(8):
            for j in range(8):
                if self.get_plateau()[i,j].piece == None :
                    pass
                elif (self.get_plateau()[i,j].piece.couleur == 1-couleur) and (self.position_rois[couleur] in self.get_plateau()[i,j].piece.nature.deplacements(i,j,1-couleur,self)) :
                    return True
        return False

    def copier(self):
        copie = Board()
        for i in range(8):
            for j in range(8):
                copie.plateau[i,j] = Case(i,j,self.get_plateau()[i,j].piece)
        copie.position_rois = self.position_rois
        return copie



      

       
