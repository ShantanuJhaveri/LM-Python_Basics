# Shantanu Jhaveri, sj06434@usc.edu
# ITP 115, Spring 2020
# Assignment 2
# Description:
# This program asks the user to input values and finds the average, the largest number, and the smallest number

# set two initializations for the while loops to run continuously unless broken
initialization = True
run = True

# first while loop allows for the ability to re-run the program
while run:
    num = input("Input an integer greater than or equal to 0 or -1 to quit: ")
    # validates input as a number
    try:
        num = int(num)
    except ValueError:
        print("'{}' is not a valid num, please try again".format(num))
        continue

    # Initial variable values set to general max numbers and min numbers that can easily be changed by any input
    sum = 0
    count = 0
    largestNum = 0
    smallestNum = num

    # second loop to actually run the program
    while initialization:

        # qualification for termination
        if num != -1:
            # count made to reference the number of user inputs
            count += 1
            sum += num
            # if statements to change existing variables for largest number and smallest number
            if num > largestNum:
                largestNum = num
            if num < smallestNum:
                smallestNum = num

        # if number is -1, the loop will end immediately
        else:
            initialization = False

        # if the program is still running, the next number is called
        if initialization:
            num = input("Input an integer greater than or equal to 0 or -1 to quit: ")
            # validates input as a number
            try:
                num = int(num)
            except ValueError:
                print("'{}' is not a valid num, please try again.".format(num))
                continue

        # once initialization is changed to false, the program prints teh requests
        if count >= 1 and initialization == False:
            average = sum / count
            # include \n for spacing
            print("\n\n\n")
            print("Program terminated")
            print("The largest number is: " + str(largestNum))
            print("The smallest number is: " + str(smallestNum))
            # print("The number of inputs is: " + str(count))
            # print("The sum of all numbers is: " + str(sum))
            print("The average of the numbers is: " + str(average))
            print("\n\n\n")

        # if there is no inputs and the program is quit immediately, the program will print nothing
        if count < 1 and initialization == False:
            print("\n\n\n")
            print("Program did not have enough inputs to run")
            print("\n\n\n")

    # if statement that runs when the initialization loop is closed
    if not initialization:
        # input if the user would like to run again
        run_again = input("Would you like to enter another set of numbers? (y/n): ").lower()
        while run_again != "y" and run_again != "n":
            run_again = input("Oops, you did not enter a valid value. Please enter a valid response (y/n):").lower()
        # if the user chooses to run, sets both variables back to their initial states and runs again
        if run_again == "y":
            run = True
            initialization = True
        # else, both loops close
        else:
            run = False
