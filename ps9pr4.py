#
# AI Player for use in Connect Four   
#

import random  
from ps9pr3 import *


class AIPlayer(Player):
    def __init__(self, checker, tiebreak, lookahead):
        """
        constructor for the subclass AIPlayer with additional attributes tiebreak and
        lookahead which indicate how the player break ties and how many look ahead it
        has
        """
        assert(checker == 'X' or checker == 'O')
        assert(tiebreak == 'LEFT' or tiebreak == 'RIGHT' or tiebreak == 'RANDOM' or tiebreak == "CENTER")
        assert(lookahead >= 0)
        super().__init__(checker)
        self.tiebreak = tiebreak
        self.lookahead = lookahead


    def __repr__(self):
        """
        returns a string representing an AIPlayer object. This method will override/replace
        the __repr__ method that is inherited from Player. In addition to indicating which
        checker the AIPlayer object is using, the returned string should also indicate the
        player’s tiebreaking strategy and lookahead.
        """
        return "Player" + " " + self.checker + " " + "(" + self.tiebreak + ", " + str(self.lookahead) + ")"
    
    
    def max_score_column(self, scores):
        """
        takes a list scores containing a score for each column of the board, and that returns
        the index of the column with the maximum score.
        """
        mymax = max(scores)
        mylist = []
        for i in range(len(scores)):
            if scores[i] == mymax:
                mylist += [i]
        if len(mylist) >= 1:
            if self.tiebreak == "LEFT":
                mypick = mylist[0]
            elif self.tiebreak == "RIGHT":
                mypick = mylist[-1]
            else:
                mypick = random.choice(mylist)
            # my secret method for tiebreaking that picks the center-most column
            # would have worked if parameters has board :(
            """
            else:
                myindex = len(board.width) // 2
                myindex_up = len(board.width) // 2
                myindex_down = len(board.width) // 2
                while True:
                    if board.can_add_to(myindex_up) == True:
                        mypick_up = myindex_up
                        break
                    else:
                        myindex_up += 1
                while True:
                    if board.can_add_to(myindex_down) == True:
                        mypick_down = myindex_down
                        break
                    else:
                        myindex_down -= 1
                if myindex_up - myindex > myindex - myindex_down:
                    mypick = mypick_down
                elif myindex_up - myindex < myindex - myindex_down:
                    mypick = mypick_up
                else:
                    mypick = mypick_up
                """
        return mypick


    def scores_for(self, board):
        """
        takes a Board object board and determines the called AIPlayer‘s scores for the columns in board.
        """
        scores = [-2]*board.width
        for col in range(board.width):
            if board.can_add_to(col) == False:
                scores[col] = -1
            elif board.is_win_for(self.checker) == True:
                scores[col] = 100
            elif board.is_win_for(self.opponent_checker()) == True:
                scores[col] = 0
            elif self.lookahead == 0:
                scores[col] = 50
            else:
                board.add_checker(self.checker,col)
                opp = AIPlayer(self.opponent_checker(), self.tiebreak, self.lookahead-1)
                opp_scores = opp.scores_for(board)
                if max(opp_scores) == 100:
                    scores[col] = 0
                elif max(opp_scores) == 0:
                    scores[col] = 100
                else:
                    scores[col] = 50
                board.remove_checker(col)
        return scores
                

    def next_move(self, board):
        """
        overrides (i.e., replaces) the next_move method that is inherited from Player.
        """
        myscores = self.scores_for(board)
        best_move = self.max_score_column(myscores)
        self.num_moves += 1
        return best_move
        
                
            
            

