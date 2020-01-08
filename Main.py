
import pygame
from Board import Board
from Cases import Case
from Pieces import Piece,Pion,Cavalier,Fou,Tour,Roi,Reine

# We create a main to launch the program

def main() :
    # We create a board which is a matrix of zeros
    board = Board()
    # We launch the program
    pygame.init()


    # Initialization of the cases
    for i in range(2,6):
        for j in range(8):
            board.plateau[i,j] = Case(i,j, None)
    

    # Place the pawns
    for i in range(8):
        board.plateau[6,i] = Case(6,i, Piece(0, Pion()))
        board.plateau[1,i] = Case(1,i, Piece(1, Pion()))
    

    # Place the towers
    for i in [0,7] :
        board.plateau[0,i] = Case(0,i,Piece(1,Tour()))
        board.plateau[7,i] = Case(7,i,Piece(0,Tour()))
    
    # Place the knights
    for i in [1,6] :
        board.plateau[0,i] = Case(0,i,Piece(1,Cavalier()))
        board.plateau[7,i] = Case(7,i,Piece(0,Cavalier()))
    
    # Place the beshops
    for i in [2,5] :
        board.plateau[0,i] = Case(0,i,Piece(1,Fou()))
        board.plateau[7,i] = Case(7,i,Piece(0,Fou()))
    
    # Place the queens
    board.plateau[0,4] = Case(0,4,Piece(1,Reine()))
    board.plateau[7,4] = Case(7,4,Piece(0,Reine()))
    
    
    # Place the kings
    board.plateau[0,3] = Case(0,3,Piece(1,Roi()))
    board.plateau[7,3] = Case(7,3,Piece(0,Roi()))

    
    # Loop the game while we don't quit by clic on the button of the window.
    while True:
        
        event = pygame.event.wait()
 
        if event.type == pygame.QUIT:
            pygame.quit()
            break 

        board.display()

        if event.type == pygame.MOUSEBUTTONDOWN :
            board.clic_to_case(event.pos)
                                  


        
# Calls the main function
if __name__ == "__main__":
    main()    


# Method that display the board
def afficher_board(board):
    Affichage = np.empty((8, 8), str)
    for i in range(8):
        for j in range(8):
            if board.get_plateau()[i,j].piece == None:
                Affichage[i,j] = 'N'
            else:
                Affichage[i,j] = board.get_plateau()[i,j].piece.nature.nom
    return Affichage

