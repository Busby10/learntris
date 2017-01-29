#!/usr/bin/env python

def reset_grid():
    grid = [[".",".",".",".",".",".",".",".",".","."] for x in range(22)]
    return grid



play_grid = reset_grid()

score = 0
cleared_lines = 0

while True:
    command = input()

    if command == "q":
        exit()

    elif command == "p":
        for i,row in enumerate(play_grid):
            print(" ".join(row))

    elif command == "g":

        for y in range(22):
            row = input()
            for x,i in enumerate(row.split(" ")):
                play_grid[y][x] = i

    elif command == "c":
        play_grid = reset_grid()

    elif command == "?s":
        print(score)

    elif command == "?n":
        print(cleared_lines)



