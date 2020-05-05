# Description:
# This second part of the code. It is made to emulate a D20, but only with range-based for loops.
# The assignment was to print out the winning numbers but with the for-loop only to demonstrate understanding
# Things such as functions, count(), and find () were not allowed

import random

# winning cases:
# Case 1: Roll a number any even number
# Valid winning numbers for Case 1 are 2, 4, 6, (…) 18, 20

# Case 2: Roll any odd number
# Valid winning numbers for Case 2 are 1, 3, 5, (…) 15, 17, 19

# Case 3: Roll any number 5 through 10 inclusive
# Valid winning numbers for Case 3 are 5, 6, 7, 8, 9, 10

# Case 4: Roll an even number 10 or greater
# Valid winning numbers for Case 4 are 10, 12, 14, 16, 18, 20

# Case 5: Roll any multiple of 3
# Valid winning numbers for Case 5 are 3, 6, 9, 12, 15, 18

print("PART 2 - D20 Dice Game")
count = 1
print("\n")
while count <= 10:
    print("Game number #" + str(count))
    count += 1
    case = random.randrange(1, 6)
    if case == 1:
        print(
            "Case 1: Roll a number any even number \nValid winning numbers for Case 1 are "
        )
        for num in range(2, 21, 2):
            print(str(num) + ' ', end="")
        roll = random.randrange(1, 21, 1)
        print("\nNow Rolling...\nYou rolled a " + str(roll))
        if roll in range(2, 21, 2):
            print("You won\n")
        else:
            print("You lost\n")

    elif case == 2:
        print(
            "Case 2: Roll any odd number \nValid winning numbers for Case 2 are "
        )
        for num in range(1, 21, 2):
            print(str(num) + ' ', end="")
        roll = random.randrange(1, 21, 1)
        print("\nNow Rolling...\nYou rolled a " + str(roll))
        if roll in range(1, 21, 2):
            print("You won\n")
        else:
            print("You lost\n")

    elif case == 3:
        print(
            "Case 3: Roll any number 5 through 10 inclusive \nValid winning numbers for Case 3 are "
        )
        for num in range(5, 11, 1):
            print(str(num) + ' ', end="")
        roll = random.randrange(1, 21, 1)
        print("\nNow Rolling...\nYou rolled a " + str(roll))
        if roll in range(5, 11, 1):
            print("You won\n")
        else:
            print("You lost\n")

    elif case == 4:
        print(
            "Case 4: Roll an even number 10 or greater \nValid winning numbers for Case 4 are "
        )
        for num in range(10, 21, 2):
            print(str(num) + ' ', end="")
        roll = random.randrange(1, 21, 1)
        print("\nNow Rolling...\nYou rolled a " + str(roll))
        if roll in range(10, 21, 2):
            print("You won\n")
        else:
            print("You lost\n")

    elif case == 5:
        print(
            "Case 5: Roll any multiple of 3 \nValid winning numbers for Case 5 are "
        )
        for num in range(1, 21, 3):
            print(str(num) + ' ', end="")
        roll = random.randrange(1, 21, 1)
        print("\nNow Rolling...\nYou rolled a " + str(roll))
        if roll in range(1, 21, 3):
            print("You won\n")
        else:
            print("You lost\n")
