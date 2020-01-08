
import copy
import pygame
import numpy as np
from Pieces import Piece
from Cases import Case
from Pieces import Piece,Pion,Cavalier,Fou,Tour,Roi,Reine


class Board:
    # Initialization of the board, a board consists of 64 spots
    # A board has a value that allows it to select a particular spot at any given time
    # whites are down and blacks are up
    def __init__(self):
        self.plateau = np.empty((8, 8), Case)
        self.couleur_jouee = 0
        self.piece_selectionnee = None
        self.case_selectionnee = None
        self.cases_selectionnables = []
        self.screen = pygame.display.set_mode((600,600))
        self.chess = pygame.image.load("chess.gif")
        self.echecB = pygame.image.load("echecB.gif")
        self.echecN = pygame.image.load("echecN.gif")
        self.changeN = pygame.image.load("changeN.gif")
        self.changeB = pygame.image.load("changeB.gif")
        self.position_rois = [[7,3],[0,3]]
        self.echec_et_maths = [False,None]

    # getter
    def get_plateau(self):
        return self.plateau
  
    # Method which allow us to select a spot of the board.
    def selectionner_case(self,y,x):
        if [y,x] in self.cases_selectionnables :
            self.get_plateau()[y,x].piece = self.piece_selectionnee
            self.get_plateau()[self.case_selectionnee[0],self.case_selectionnee[1]].piece = None
            if self.piece_selectionnee.nature.nom == 'K' :
                self.position_rois[self.piece_selectionnee.couleur] = [y,x]
            if (self.piece_selectionnee.nature.nom == 'P') and (y == 7*self.couleur_jouee) :
                if self.couleur_jouee == 0:
                    self.display(self.changeB)
                else :
                    self.display(self.changeN)
                self.transformer_pion(y,x)
            self.couleur_jouee = 1 - self.couleur_jouee
            self.echec_maths()
            self.cases_selectionnables = []
            self.piece_selectionnee = None
            self.case_selectionnee = None

            
        elif self.get_plateau()[y,x].piece == None :
            pass
        
        elif self.get_plateau()[y,x].piece.couleur == self.couleur_jouee :
            self.piece_selectionnee = self.get_plateau()[y,x].piece
            self.case_selectionnee = [y,x]
            self.cases_selectionnables = self.verifie_echec(self.piece_selectionnee.nature.deplacements(y,x,self.couleur_jouee,self))

            
            
            
    # Method which takes a pawn and, when it reaches the other side of the board, changes with in another piece that the user select
    def transformer_pion(self,y,x):
        event = pygame.event.wait()
        while event.type != pygame.MOUSEBUTTONDOWN :
            event = pygame.event.wait()
        if event.pos[0] <= 300 and event.pos[1] >= 300:
            self.get_plateau()[y,x].piece = Piece(self.couleur_jouee,Cavalier())
        elif event.pos[0] <= 300 and event.pos[1] <= 300 :
            self.get_plateau()[y,x].piece = Piece(self.couleur_jouee,Tour())
        elif event.pos[0] >= 300 and event.pos[1] >= 300 :
            self.get_plateau()[y,x].piece = Piece(self.couleur_jouee,Fou())
        elif event.pos[0] >= 300 and event.pos[1] <= 300 :
            self.get_plateau()[y,x].piece = Piece(self.couleur_jouee,Reine())

            
    # Method which display the board on the graphic interface.
    def display(self, changement = None):
        self.screen.fill((0,0,0))
        self.screen.blit(self.chess,(0,0))
        self.draw_cases_selectionnables(self.cases_selectionnables)
        for k in self.get_plateau():
            for case in k:
                if case.piece != None :
                    case.draw_piece(self)
        self.display_echec_et_maths()
        if changement != None :
            self.screen.blit(changement, (0,0))
        pygame.display.flip()

        
    # Method which display a message which stops the game and annoces the winner if one of the player is checkmate.
    def display_echec_et_maths(self):
        if (self.echec_et_maths[0] == True) and (self.echec_et_maths[1] == 0):
            self.screen.blit(self.echecB,(0,0))
        elif (self.echec_et_maths[0] == True) and (self.echec_et_maths[1] == 1):
            self.screen.blit(self.echecN,(0,0))

            
    # When the user clicks on the board, this function will select the spot the user clicked on
    def clic_to_case(self,pos):
        if (36 < pos[0]< 564) and (36 <= pos[1] <= 564):
            case_x = (pos[0]-36)//66
            case_y = (pos[1]-36)//66
            self.selectionner_case(case_y,case_x)

            
    # Method which fills with green the spots where the piece that we clicked on can move.
    def draw_cases_selectionnables(self, cases_a_colorier):
        for case in cases_a_colorier :
            pygame.draw.rect(self.screen, (0,255,0), [case[1]*66+36, case[0]*66+36, 66, 66])

            
    # Method which test if, when a player want to move a piece, he doesn't put himself in check
    def verifie_echec(self, liste_cases):
        Liste_possible = []
        for case in liste_cases :
            board_copie = self.copier()
            board_copie.get_plateau()[case[0], case[1]].piece = self.piece_selectionnee
            board_copie.get_plateau()[self.case_selectionnee[0], self.case_selectionnee[1]].piece = None
            if board_copie.get_plateau()[case[0],case[1]].piece.nature.nom == 'K':
                board_copie.position_rois[self.couleur_jouee] = [case[0],case[1]]
            else :
                board_copie.position_rois = self.position_rois*1
            if board_copie.roi_en_echec(self.couleur_jouee) == False:
                Liste_possible += [case]
        return Liste_possible

    
    # Method which test if the selected player is in check.
    def roi_en_echec(self, couleur):
        for i in range(8):
            for j in range(8):
                if self.get_plateau()[i,j].piece == None :
                    pass
                elif (self.get_plateau()[i,j].piece.couleur == 1-couleur) and (self.position_rois[couleur] in self.get_plateau()[i,j].piece.nature.deplacements(i,j,1-couleur,self)) :
                    return True
        return False

    
    # Test if one of the players is checkmate.
    def echec_maths(self):
        for i in range(8):
            for j in range(8):
                if (self.get_plateau()[i,j].piece == None):
                    pass
                elif self.get_plateau()[i,j].piece.couleur == self.couleur_jouee :
                    self.piece_selectionnee = self.get_plateau()[i,j].piece
                    self.case_selectionnee = [i,j]
                    self.cases_selectionnables = self.verifie_echec(self.piece_selectionnee.nature.deplacements(i,j,self.couleur_jouee,self))
                    if (self.cases_selectionnables != []):
                        return False
        self.echec_et_maths = [True, self.couleur_jouee]
        return True

    
    # Method which creates a new board, which is a copy the original board
    def copier(self):
        copie = Board()
        for i in range(8):
            for j in range(8):
                copie.plateau[i,j] = Case(i,j,self.get_plateau()[i,j].piece)
        return copie


       
