#
# A Connect Four Board class
#

class Board:
    def __init__(self, height, width):
        """
        constructs a new Board object by initializing the height and the width
        of the board, as well as a slot stores a reference to a two-dimensional
        list with height rows and width columns
        """
        self.height = height
        self.width = width
        self.slots = [[' '] * self.width for row in range(self.height)]


    def __repr__(self):
        """
        Returns a string representation for a Board object.
        """
        s = ''         # begin with an empty string

        # add one row of slots at a time
        for row in range(self.height):
            s += '|'   # one vertical bar at the start of the row

            for col in range(self.width):
                s += self.slots[row][col] + '|'

            s += '\n'  # newline at the end of the row

        # Add code here for the hyphens at the bottom of the board
        # and the numbers underneath it.

        for h in range(self.width*2+1):
            s += '-'
        s += '\n'
        s += ' '
        for col in range(self.width):
            s += str(col%10) + ' '
        return s


    def add_checker(self, checker, col):
        """
        accepts two inputs: checker, a one-character string that specifies the
        checker to add to the board (either 'X' or 'O').
        col, an integer that specifies the index of the column to which the
        checker should be added and that adds checker to the appropriate row
        in column col of the board.
        """
        assert(checker == 'X' or checker == 'O')
        assert(0 <= col < self.width)

        # put the rest of the method here
        row = 0
        while self.slots[row][col] == ' ':
            if row == self.height-1:
                self.slots[row][col] = checker
            elif self.slots[row+1][col] != ' ':
                self.slots[row][col] = checker
            else:
                row += 1

                
    def reset(self):
        """
        reset the Board object on which it is called by setting all slots to
        contain a space character.

        """
        for row in range(self.height):
            for col in range(self.width):
                self.slots[row][col] = ' '


    def add_checkers(self, colnums):
        """
        takes in a string of column numbers and places alternating
        checkers in those columns of the called Board object,
        starting with 'X'.
        """
        checker = 'X'   # start by playing 'X'
        for col_str in colnums:
            col = int(col_str)
            if 0 <= col < self.width:
                self.add_checker(checker, col)
            # switch to the other checker
            if checker == 'X':
                checker = 'O'
            else:
                checker = 'X'


    def can_add_to(self, col):
        """
        returns True if it is valid to place a checker in the column col on
        the calling Board object. Otherwise, it should return False.
        """
        if 0 <= col <= self.width-1:
            if self.slots[0][col] == ' ':
                return True
        return False


    def is_full(self):
        """
        returns True if the called Board object is completely full of checkers,
        and returns False otherwise.
        """
        for col in range(self.width):
            if self.can_add_to(col) == True:
                return False
        return True


    def remove_checker(self, col):
        """
        removes the top checker from column col of the called Board object.
        If the column is empty, then the method should do nothing.
        """
        if self.slots[self.height-1][col] == ' ':
            return
        elif self.slots[0][col] != ' ':
            self.slots[0][col] = ' '
        else:
            row = 0
            while self.slots[row][col] == ' ':
                if self.slots[row+1][col] != ' ':
                    self.slots[row+1][col] = ' '
                    break
                else:
                    row += 1

    def is_horizontal_win(self, checker):
        """
        Checks for a horizontal win for the specified checker.
        """
        for row in range(self.height):
            for col in range(self.width - 3):
                # Check if the next four columns in this row
                # contain the specified checker.
                if self.slots[row][col] == checker and \
                   self.slots[row][col + 1] == checker and \
                   self.slots[row][col + 2] == checker and \
                   self.slots[row][col + 3] == checker:
                    return True

        # if we make it here, there were no horizontal wins
        return False


    def is_vertical_win(self, checker):
        """
        Checks for a vertical win for the specified checker.
        """
        for row in range(self.height-3):
            for col in range(self.width):
                if self.slots[row][col] == checker and \
                   self.slots[row+1][col] == checker and \
                   self.slots[row+2][col] == checker and \
                   self.slots[row+3][col] == checker:
                    return True
        return False


    def is_down_diagonal_win(self, checker):
        """
        Checks for a down diagonal win for the specified checker.
        """
        for row in range(self.height-3):
            for col in range(self.width-3):
                if self.slots[row][col] == checker and \
                   self.slots[row+1][col+1] == checker and \
                   self.slots[row+2][col+2] == checker and \
                   self.slots[row+3][col+3] == checker:
                    return True
        return False


    def is_up_diagonal_win(self, checker):
        """
        Checks for a up diagonal win for the specified checker.
        """
        for row in range(3,self.height):
            for col in range(self.width-3):
                if self.slots[row][col] == checker and \
                   self.slots[row-1][col+1] == checker and \
                   self.slots[row-2][col+2] == checker and \
                   self.slots[row-3][col+3] == checker:
                    return True
        return False


    def is_win_for(self, checker):
        """
        accepts a parameter checker that is either 'X' or 'O', and returns
        True if there are four consecutive slots containing checker on the
        board. Otherwise, it should return False.
        """
        if self.is_horizontal_win(checker) == True:
            return True
        elif self.is_vertical_win(checker) == True:
            return True
        elif self.is_down_diagonal_win(checker) == True:
            return True
        elif self.is_up_diagonal_win(checker) == True:
            return True
        else:
            return False











        
                
