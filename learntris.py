#!/usr/bin/env python

class Grid(object):

    def __init__(self):
        self.grid = []
        self.reset_grid()
        self.score = 0
        self.cleared_lines = 0
        self.active_tet = []

    def reset_grid(self):
        self.grid = [[".",".",".",".",".",".",".",".",".","."] for x in range(22)]

    def print_grid(self):
        for i,row in enumerate(self.grid):
            print(" ".join(row))

    def set_row(self, row_num, row=None):
        if row == None:
            self.grid[row_num] = [".",".",".",".",".",".",".",".",".","."]
        else:
            for col_num,item in enumerate(row.split(" ")):
                self.grid[row_num][col_num] = item

    def full_row_check(self):
        for row_num,row in enumerate(self.grid):
            if "." not in row:
                self.set_row(row_num)
                self.score += 100
                self.cleared_lines += 1

    def set_active_tet(self,tetramino):
        if tetramino == "I":
            self.active_tet =  [[".", ".", ".", "."],
                                ["c", "c", "c", "c"],
                                [".", ".", ".", "."],
                                [".", ".", ".", "."]]
        elif tetramino == "O":
            self.active_tet =  [["y", "y"],
                                ["y", "y"]]
        elif tetramino == "Z":
            self.active_tet =  [["r", "r", "."],
                                [".", "r", "r"],
                                [".", ".", "."]]
        elif tetramino == "S":
            self.active_tet =  [[".", "g", "g"],
                                ["g", "g", "."],
                                [".", ".", "."]]
        elif tetramino == "J":
            self.active_tet =  [["b", ".", "."],
                                ["b", "b", "b"],
                                [".", ".", "."]]
        elif tetramino == "L":
            self.active_tet =  [[".", ".", "o"],
                                ["o", "o", "o"],
                                [".", ".", "."]]
        elif tetramino == "T":
            self.active_tet =  [[".", "m", "."],
                                ["m", "m", "m"],
                                [".", ".", "."]]

    def print_active_tet(self):
        for i,row in enumerate(self.active_tet):
            print(" ".join(row))

    def rotate_tet(self,direction):

        new_tet = [["." for x in range(len(self.active_tet))] for x in range(len(self.active_tet))]

        if direction == ")":

            for y, row in enumerate(self.active_tet):
                for x, col in enumerate(row):
                    new_tet[x][-(y+1)] = col

        self.active_tet = new_tet



def take_action(command):
    if command == "q":
    #Quits program
        exit()

    elif command == "p":
        #Prints current Grid
        play_grid.print_grid()

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
        play_grid.set_active_tet(command)

    elif command == "t":
        play_grid.print_active_tet()

    elif command == ")" or command == "(":
        play_grid.rotate_tet(command)

    else:
        print("Incorrect input: ", command)
        exit()


play_grid = Grid()

while True:
    command = input()
    if " " in command:
        commands = command.split(" ")
        for c in commands:
            take_action(c)
    else:
        take_action(command)