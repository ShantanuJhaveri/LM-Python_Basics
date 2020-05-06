# Shantanu Jhaveri, sj06434@usc.edu
# ITP 115, Spring 2020
# Lab 3-1

row = 0
numSymbols = 0
numSpaces_before = 20
while row <= 10:
    print(" " * numSpaces_before + "^ " * numSymbols)
    numSymbols = (row * 2) + 1
    numSpaces_before -= 2
    row += 1
