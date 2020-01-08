# On cree une classe Piece 
class Piece:
    def __init__(self, couleur, nature):   
# On a en parametre la couleur qui est un nombre entre 0 et 1 qui indique si on a l'equipe noire ou l'equipe blanche
        self.couleur = couleur
# La nature correspond au type de la piece et correspond aux calasses Pion, Tour, ...
        self.nature = nature
        
#1 pour noirs, 0 pour blancs
class Pion:
    def __init__(self):
        self.piece = Piece
        self.nom = 'P'
    
    def est_a_origine(self,y,couleur) :
        if (couleur == 1) and (y == 1) :
            return True
        elif (couleur == 0) and (y == 6) :
            return True
        else :
            return False

    def deplacements(self,y,x,couleur,board):
        return self.deplacements_avant(y,x,couleur,board) + self.deplacements_diag_g(y,x,couleur,board) + self.deplacements_diag_d(y,x,couleur,board)
    
    def deplacements_avant(self,y,x,couleur,board):
        if ((couleur == 1) and (y == 7)) or ((couleur == 0) and (y == 0)):
            return []
        elif board.get_plateau()[y-1+2*couleur,x].piece == None :
            return [[y-1+2*couleur,x]] + self.deplacements_avant_double(y,x,couleur,board)
        else : 
            return []
    
    def deplacements_avant_double(self,y,x,couleur,board):
        if self.est_a_origine(y,couleur) and board.get_plateau()[y-2+4*couleur,x].piece == None :
            return [[y-2+4*couleur,x]]
        else :
            return []
        
    def deplacements_diag_g(self,y,x,couleur,board):
        if (x == 0) or ((couleur == 1) and (y == 7)) or ((couleur == 0) and (y == 0)):
            return []
        elif board.get_plateau()[y-1+2*couleur,x-1].piece == None :
            return []
        elif board.get_plateau()[y-1+2*couleur,x-1].piece.couleur == couleur :
            return []
        else :
            return [[y-1+2*couleur,x-1]]
        
    def deplacements_diag_d(self,y,x,couleur,board):
        if (x == 7) or ((couleur == 1) and (y == 7)) or ((couleur == 0) and (y == 0)):
            return []
        elif board.get_plateau()[y-1+2*couleur,x+1].piece == None :
            return []
        elif board.get_plateau()[y-1+2*couleur,x+1].piece.couleur == couleur :
            return []
        else :
            return [[y-1+2*couleur,x+1]]
            

class Tour:
    def __init__(self):
        self.nom = 'T'
        
    def deplacements(self,y,x,couleur,board):
        return self.deplacements_haut(y,x,couleur,board) + self.deplacements_bas(y,x,couleur,board) + self.deplacements_gauche(y,x,couleur,board) + self.deplacements_droite(y,x,couleur,board)
    
    def deplacements_haut(self,y,x,couleur,board):
        if y == 0 :
            return []
        elif board.get_plateau()[y-1,x].piece == None :
            return [[y-1,x]] + self.deplacements_haut(y-1,x,couleur,board)
        elif board.get_plateau()[y-1,x].piece.couleur == couleur :
            return []
        else :
            return [[y-1,x]]
        
    def deplacements_bas(self,y,x,couleur,board):
        if y == 7 :
            return []
        elif board.get_plateau()[y+1,x].piece == None :
            return [[y+1,x]] + self.deplacements_bas(y+1,x,couleur,board)
        elif board.get_plateau()[y+1,x].piece.couleur == couleur :
            return []
        else :
            return [[y+1,x]]
        
    def deplacements_droite(self,y,x,couleur,board):
        if x == 7 :
            return []
        elif board.get_plateau()[y,x+1].piece == None :
            return [[y,x+1]] + self.deplacements_droite(y,x+1,couleur,board)
        elif board.get_plateau()[y,x+1].piece.couleur == couleur :
            return []
        else :
            return [[y,x+1]]
        
    def deplacements_gauche(self,y,x,couleur,board):
        if x == 0 :
            return []
        elif board.get_plateau()[y,x-1].piece == None :
            return [[y,x-1]] + self.deplacements_gauche(y,x-1,couleur,board)
        elif board.get_plateau()[y,x-1].piece.couleur == couleur :
            return []
        else :
            return [[y,x-1]]
        
        
class Cavalier:
    def __init__(self):
        self.nom = 'C'
        
    def deplacements(self,y,x,couleur,board):
        D = []
        L = [[y+2,x+1],[y+2,x-1],[y-2,x+1],[y-2,x-1],[y+1,x+2],[y+1,x-2],[y-1,x+2,],[y-1,x-2]]
        for k in L :
            if (k[0] > 7) or (k[0] < 0) or (k[1] > 7) or (k[1] < 0) :
                pass
            elif board.get_plateau()[k[0],k[1]].piece == None :
                D += [k]
            elif board.get_plateau()[k[0],k[1]].piece.couleur != couleur :
                D += [k]
        return D
            

class Fou:
    def __init__(self):
        self.nom = 'F'
        
    def deplacements(self,y,x,couleur,board):
        return self.deplacements_h_g(y,x,couleur,board) + self.deplacements_h_d(y,x,couleur,board) + self.deplacements_b_g(y,x,couleur,board) + self.deplacements_b_d(y,x,couleur,board)
    
    def deplacements_h_g(self,y,x,couleur,board):
        if (y == 0) or (x == 0) :
            return []
        elif board.get_plateau()[y-1,x-1].piece == None :
            return [[y-1,x-1]] + self.deplacements_h_g(y-1,x-1,couleur,board)
        elif board.get_plateau()[y-1,x-1].piece.couleur == couleur :
            return []
        else :
            return [[y-1,x-1]]
        
    def deplacements_h_d(self,y,x,couleur,board):
        if (y == 0) or (x == 7):
            return []
        elif board.get_plateau()[y-1,x+1].piece == None :
            return [[y-1,x+1]] + self.deplacements_h_d(y-1,x+1,couleur,board)
        elif board.get_plateau()[y-1,x+1].piece.couleur == couleur :
            return []
        else :
            return [[y-1,x+1]]
        
    def deplacements_b_g(self,y,x,couleur,board):
        if (y == 7) or (x == 0) :
            return []
        elif board.get_plateau()[y+1,x-1].piece == None :
            return [[y+1,x-1]] + self.deplacements_b_g(y+1,x-1,couleur,board)
        elif board.get_plateau()[y+1,x-1].piece.couleur == couleur :
            return []
        else :
            return [[y+1,x-1]]
        
    def deplacements_b_d(self,y,x,couleur,board):
        if (y == 7) or (x == 7):
            return []
        elif board.get_plateau()[y+1,x+1].piece == None :
            return [[y+1,x+1]] + self.deplacements_b_d(y+1,x+1,couleur,board)
        elif board.get_plateau()[y+1,x+1].piece.couleur == couleur :
            return []
        else :
            return [[y+1,x+1]]

         
class Reine:
    def __init__(self):
        self.nom = 'Q'

    def deplacements(self,y,x,couleur,board):
         return (Fou().deplacements(y,x,couleur,board) + Tour().deplacements(y,x,couleur,board))
         
class Roi:
    def __init__(self):
        self.nom = 'K'

    def deplacements(self,y,x,couleur,board):
        D = []
        for i in range(-1,2):
            for j in range(-1,2):
                pos_y, pos_x = y+i, x+j
                if (pos_y > 7) or (pos_y <0) or (pos_x > 7) or (pos_x < 0) :
                    pass
                elif board.get_plateau()[pos_y, pos_x].piece == None :
                    D += [[pos_y, pos_x]]
                elif board.get_plateau()[pos_y, pos_x].piece.couleur != couleur :
                    D += [[pos_y, pos_x]]
        return D
