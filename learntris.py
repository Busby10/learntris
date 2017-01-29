#!/usr/bin/env python

play_grid = [[".",".",".",".",".",".",".",".",".","."] for x in range(22)]




while True:
    command = input("Command: ")
    if command == "q":
        exit()
    elif command == "p":
        for i,row in enumerate(play_grid):
            print(" ".join(row))



