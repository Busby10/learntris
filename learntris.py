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
            for x,i in enumerate(row.split(" ")):
                play_grid.grid[y][x] = i

    elif command == "c":
        play_grid.reset_grid()

    elif command == "?s":
        print(score)

    elif command == "?n":
        print(cleared_lines)



