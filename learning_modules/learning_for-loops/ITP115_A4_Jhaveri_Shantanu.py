# Shantanu Jhaveri, sj06434@usc.edu
# ITP 115, Spring 2020
# Assignment 4
# Description:
# Describe what this program does.

print("PART 1 - Character Counter")
alphabet = 'abcdefghijklmnopqrstuvwxyz'
character = input("Please enter a sentence:")
print("Here is the character distribution:")
count = 0
special = 0

for letter in alphabet:
    print(letter + ": ", end="")
    count = 0
    for a in character:
        if a == letter:
            print("*")
            count += 1
        else:
            print(" ")
