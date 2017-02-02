#!/usr/bin/env python

class Grid(object):

    def __init__(self):
        self.grid = []
        self.reset_grid()
        self.score = 0
        self.cleared_lines = 0
        self.active_tet = None


    def reset_grid(self):
        self.grid = [[".",".",".",".",".",".",".",".",".","."] for x in range(22)]

    def print_grid(self, given_grid = None):
        #prints a given grid, or self.grid if no arguments given
        if given_grid == None:
            for i,row in enumerate(self.grid):
                print(" ".join(row))
        else:
            for i,row in enumerate(given_grid):
                print(" ".join(row))

    def set_row(self, row_num, row=None):
        #sets a given row at a specified row number, or clears the row number if
        # no new row is given. Input row is provided as a string
        if row == None:
            self.grid[row_num] = [".",".",".",".",".",".",".",".",".","."]
        else:
            for col_num,item in enumerate(row.split(" ")):
                self.grid[row_num][col_num] = item

    def full_row_check(self):
        #checks for a complete row. If found, clears it and adds score
        for row_num,row in enumerate(self.grid):
            if "." not in row:
                self.set_row(row_num)
                self.score += 100
                self.cleared_lines += 1

    def print_active_grid(self):
        #prints grid with the active tetramino on it.

        #Creates a new grid that is a copy of self.grid
        new_grid = [list(i) for i in self.grid]

        for y,row in enumerate(self.active_tet.tet):
            for x,col in enumerate(row):
                #copies the active tet over the top of the new grid starting at the set entry point.
                if col not in ".":
                    new_grid[self.active_tet.current_point[0]+y][self.active_tet.current_point[1]+x] = col.upper()
        self.print_grid(new_grid)

    def set_active_tet(self, tetramino):
        self.active_tet = Tetramino(tetramino)


    def shift_tet(self, direction):
        #move the active tetramino in the given direction

        if direction == "<" and not (self.active_tet.current_point[1] - self.active_tet.limits[0]) == 0:
            self.tet_current_point[1] -= 1

        if direction == ">" and not (self.active_tet.current_point[1] + self.active_tet.limits[1]) == 9:
            self.active_tet.current_point[1] += 1

        if direction == "v" and not (self.active_tet.current_point[0] + self.active_tet.limits[3]) == 21:
            self.active_tet.current_point[0] += 1
            self.impact_check()

        if direction == "V":
            #fix this
            for v in range(22):
                self.active_tet.current_point[0] += 1
                self.impact_check()

    def impact_check(self):

        if (self.active_tet.current_point[0] + self.active_tet.limits[3]) == 21:
            self.write_active_tet()

        else:
            for x,col in enumerate(self.active_tet[self.active_tet.limits[3]]):
                if self.grid[(self.active_tet.current_point[0] + self.active_tet.limits[3])+1][self.active_tet.current_point[1]+x] not in ".":
                    self.write_active_tet()

    def write_active_tet(self):
        for y,row in enumerate(self.active_tet):
            for x,col in enumerate(row):
                #copies the active tet over the top of the new grid starting at the current point
                if col not in ".":
                    self.grid[self.active_tet.current_point[0]+y][self.active_tet.current_point[1]+x] = col


class Tetramino(object):
    def __init__(self, tet_type):

        self.current_point = [0,0] #y, x
        self.limits = [0,0,0,0] #left,right,up,down
        self.tet = self.set_type(tet_type)

    def print_tet(self):
        #prints active tetramino
        for i,row in enumerate(self.tet):
            print(" ".join(row))

    def set_type(self,tetramino):
        #Sets active tetramino to the argument and its entry point

        if tetramino == "I":

            return  [[".", ".", ".", "."],
                     ["c", "c", "c", "c"],
                     [".", ".", ".", "."],
                     [".", ".", ".", "."]]
            self.current_point = [0,3]

        elif tetramino == "O":
            return  [["y", "y"],
                     ["y", "y"]]
            self.current_point = [0,4]

        elif tetramino == "Z":
            return [["r", "r", "."],
                    [".", "r", "r"],
                    [".", ".", "."]]

            self.current_point = [0,3]

        elif tetramino == "S":
            return [[".", "g", "g"],
                    ["g", "g", "."],
                    [".", ".", "."]]

            self.current_point = [0,3]

        elif tetramino == "J":
            return [["b", ".", "."],
                    ["b", "b", "b"],
                    [".", ".", "."]]

            self.current_point = [0,3]

        elif tetramino == "L":
            return [[".", ".", "o"],
                    ["o", "o", "o"],
                    [".", ".", "."]]

            self.current_point = [0,3]

        elif tetramino == "T":
            return [[".", "m", "."],
                    ["m", "m", "m"],
                    [".", ".", "."]]

            self.current_point = [0,3]

        self.limits = self.find_tet_limits()

    def find_tet_limits(self):
        #find the tetramino limits in the active tet grid
        left = len(self.tet[1])-1
        right = 0
        up = len(self.tet)-1
        down = 0

        for y, row in enumerate(self.tet):
                for x, col in enumerate(row):
                    if col not in ".":

                        if x < left:
                            left = x
                        if x > right:
                            right = x
                        if y < up:
                            up = y
                        if y > down:
                            down = y

        return [left,right,up,down]

    def rotate_tet(self,direction):
        #rotates the active tetramino a given direction.

        #Creates a new grid that is the same size as the active tetramino
        new_tet = [["." for x in range(len(self.tet))] for x in range(len(self.tet))]

        if direction == "(":

            for y, row in enumerate(self.tet):
                for x, col in enumerate(row):
                    new_tet[-(x+1)][y] = col

        elif direction == ")":

            for y, row in enumerate(self.tet):
                for x, col in enumerate(row):
                    new_tet[x][-(y+1)] = col

        self.tet = new_tet
        self.limits = self.find_tet_limits()

def take_action(command):
    if command == "q":
        #Quits program
        exit()

    elif command == "p":
        #Prints current Grid
        play_grid.print_grid()

    elif command == "P":
        #Prints current active Grid
        play_grid.print_active_grid()

    elif command == "g":
        #Set grid to given grid
        for y in range(22):
            row = input()
            play_grid.set_row(y,row)

    elif command == "c":
        #Clear grid
        play_grid.reset_grid()

    elif command == "?s":
        #Print score
        print(play_grid.score)

    elif command == "?n":
        #Print number of lines cleared
        print(play_grid.cleared_lines)

    elif command == "s":
        #Step
        play_grid.full_row_check()

    elif command in "IOZSJLT":
        #sets the active tetranimo
        play_grid.set_active_tet(command)

    elif command == "t":
        #prints the active tetranimo
        play_grid.active_tet.print_tet()

    elif command == ")" or command == "(":
        #rotates the tet
        play_grid.active_tet.rotate_tet(command)

    elif command == ";":
        #prints a blank line
        print("")

    elif command in "<>vV":
        #moves the active tetramino
        play_grid.shift_tet(command)

    else:
        print("Incorrect input: ", command)
        exit()


play_grid = Grid()

while True:

    command = input()
    itercomm = iter(command)
    # create iterable of input line
    for c in itercomm:
        #loop over command line

        if c == " ":
            #ignore spaces
            continue

        elif c == "?":
            take_action(c+next(itercomm))
            #queries start with ? followed by next letter. This adds the next
            #item in the iterable to the ? and passes to take action.

        else:
            take_action(c)

