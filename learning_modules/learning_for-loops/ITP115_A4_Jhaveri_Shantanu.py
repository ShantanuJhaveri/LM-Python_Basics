# Shantanu Jhaveri, sj06434@usc.edu
# ITP 115, Spring 2020
# Assignment 4
# Description:
# Describe what this program does.

print("PART 1 - Character Counter")
alphabet = 'abcdefghijklmnopqrstuvwxyz'
input = input("Please enter a sentence:")
character = input.lower()
print("Here is the character distribution:")

# for i in alphabet:
#     print(i + ": ", end="")
#     count = 0
#     if i in character:
#         for a in i:
#             print("*", end="")
#         # for a in character:
#         #     print("*", end="")
#         print("")
#     else:
#         print("NONE")

for i in alphabet:
    print(i + ": ", end="")
    count = 0
    for a in i:
        if i in character:
            print("*", end="")
        # for a in character:
        #     print("*", end="")
            print("")
        else:
            print("NONE")

print("special characters: ", end='')
for i in character:
    if i.isalpha() != True and i != ' ':
        print("*", end='')



