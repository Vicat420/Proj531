
import pygame

#Class which create a case on the board 
class Case:

    def __init__(self, y, x, piece):
        
        # A case has a position (x,y) on the board and can have a piece (None, if there's no piece, 'P' for a pawn, 'T' for a tower...)
        self.piece = piece
        self.colonne = x
        self.ligne = y

        # We import the pictures of each piece which will be used for the graphic interface
        self.PionB = pygame.image.load("PionB.gif")
        self.PionN = pygame.image.load("PionN.gif")
        self.TourB = pygame.image.load("TourB.gif")
        self.TourN = pygame.image.load("TourN.gif")
        self.FouB = pygame.image.load("FouB.gif")
        self.FouN = pygame.image.load("FouN.gif")
        self.CavalierB = pygame.image.load("CavalierB.gif")
        self.CavalierN = pygame.image.load("CavalierN.gif")
        self.RoiB = pygame.image.load("RoiB.gif")
        self.RoiN = pygame.image.load("RoiN.gif")
        self.ReineB = pygame.image.load("ReineB.gif")
        self.ReineN = pygame.image.load("ReineN.gif")

        
    # Method which draw the piece assigned to that spot on the graphic interface.
    def draw_piece(self, board):
        if (self.piece.nature.nom == 'P') and (self.piece.couleur == 0):
            board.screen.blit(self.PionB,(66*self.colonne+36,66*self.ligne+36))

        elif (self.piece.nature.nom == 'P') and (self.piece.couleur == 1):
            board.screen.blit(self.PionN,(66*self.colonne+36,66*self.ligne+36))

        elif (self.piece.nature.nom == 'T') and (self.piece.couleur == 0):
            board.screen.blit(self.TourB,(66*self.colonne+36,66*self.ligne+36))

        elif (self.piece.nature.nom == 'T') and (self.piece.couleur == 1):
            board.screen.blit(self.TourN,(66*self.colonne+36,66*self.ligne+36))

        elif (self.piece.nature.nom == 'F') and (self.piece.couleur == 0):
            board.screen.blit(self.FouB,(66*self.colonne+36,66*self.ligne+36))

        elif (self.piece.nature.nom == 'F') and (self.piece.couleur == 1):
            board.screen.blit(self.FouN,(66*self.colonne+36,66*self.ligne+36))

        elif (self.piece.nature.nom == 'C') and (self.piece.couleur == 0):
            board.screen.blit(self.CavalierB,(66*self.colonne+36,66*self.ligne+36))

        elif (self.piece.nature.nom == 'C') and (self.piece.couleur == 1):
            board.screen.blit(self.CavalierN,(66*self.colonne+36,66*self.ligne+36))

        elif (self.piece.nature.nom == 'K') and (self.piece.couleur == 0):
            board.screen.blit(self.RoiB,(66*self.colonne+36,66*self.ligne+36))

        elif (self.piece.nature.nom == 'K') and (self.piece.couleur == 1):
            board.screen.blit(self.RoiN,(66*self.colonne+36,66*self.ligne+36))

        elif (self.piece.nature.nom == 'Q') and (self.piece.couleur == 0):
            board.screen.blit(self.ReineB,(66*self.colonne+36,66*self.ligne+36))

        elif (self.piece.nature.nom == 'Q') and (self.piece.couleur == 1):
            board.screen.blit(self.ReineN,(66*self.colonne+36,66*self.ligne+36))
