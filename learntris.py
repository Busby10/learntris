#!/usr/bin/env python

class Grid(object):

    def __init__(self):
        self.grid = []
        self.reset_grid()

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



play_grid = Grid()

score = 0
cleared_lines = 0

while True:
    command = input()

    if command == "q":
        exit()

    elif command == "p":
        play_grid.print_grid()

    elif command == "g":

        for y in range(22):
            row = input()
            play_grid.set_row(y,row)

    elif command == "c":
        play_grid.reset_grid()

    elif command == "?s":
        print(score)

    elif command == "?n":
        print(cleared_lines)



