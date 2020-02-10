#
# A Connect-Four Player class 
#  

from ps9pr1 import Board

# write your class below

class Player:
    def __init__(self, checker):
        """
        constructs a new Player object by initializing the checker that
        identifies player and the number of moves it has made
        """
        assert(checker == 'X' or checker == 'O')
        self.checker = checker
        self.num_moves = 0


    def __repr__(self):
        """
        returns a string representing a Player object. The string returned
        should indicate which checker the Player object is using
        """
        return "Player" + " " + self.checker


    def opponent_checker(self):
        """
        returns a one-character string representing the checker of the Player
        object’s opponent.
        """
        if self.checker == "X":
            return "O"
        else:
            return "X"


    def next_move(self, board):
        myinput = int(input("Enter a column: "))
        while True:
            if board.is_full() == True:
                return "Board full!"
            elif board.can_add_to(myinput) == False:
                print("Try again!")
                myinput = int(input("Enter a column: "))
            else:
                self.num_moves += 1
                return myinput
                
                      
        
