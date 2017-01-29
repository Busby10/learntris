#!/usr/bin/env python

play_grid = [[".",".",".",".",".",".",".",".",".","."] for x in range(22)]




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




