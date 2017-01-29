#!/usr/bin/env python

play_grid = [[".",".",".",".",".",".",".",".",".","."] for x in range(22)]


command = input()
if command == "q":
    pass
elif command == "p":
    for i,row in enumerate(play_grid):
        print(" ".join(row))

