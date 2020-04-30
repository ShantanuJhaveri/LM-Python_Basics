# Shantanu Jhaveri, sj06434@usc.edu
# ITP 115, Spring 2020
# Lab 1-1

# part1
print("\n\n\n\nLoading this assignment, please enjoy this stupid joke meme \n\n\n\n")
print(" _____________________________________ ")
print("|░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░|")
print("|░░░░░░░░░░░░░░░░▄▄███▄▄▄░▄▄██▄░░░░░░░|")
print("|░░░░░░░░░██▀███████████████▀▀▄█░░░░░░|")
print("|░░░░░░░░█▀▄▀▀▄██████████████▄░░█░░░░░|")
print("|░░░░░░░█▀▀░▄██████████████▄█▀░░▀▄░░░░|")
print("|░░░░░▄▀░░░▀▀▄████████████████▄░░░█░░░|")
print("|░░░░░▀░░░░▄███▀░░███▄████░████░░░░▀▄░|")
print("|░░░▄▀░░░░▄████░░▀▀░▀░░░░░░██░▀▄░░░░▀▄|")
print("|░▄▀░░░░░▄▀▀██▀░░░░░▄░░▀▄░░██░░░▀▄░░░░|")
print("|█░░░░░█▀░░░██▄░░░░░▀▀█▀░░░█░░░░░░█░░░|")
print("|▀▀▀▀░▄▄▄▄▄▄▀▀░█░░░░░░░░░▄█░░█▀▀▀▀▀█░░|")
print("|░░░░█░░░▀▀░░░░░░▀▄░░░▄▄██░░░█░░░░░▀▄░|")
print("|░░░░█░░░░░░░░░░░░█▄▀▀▀▀▀█░░░█░░░░░░█░|")
print("|░░░░▀░░░░░░░░░░░░░▀░░░░▀░░░░▀░░░░░░░░|")
print("|░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░|")
print("|_____________________________________|")

# real part1
print(" __ ")
print("|  |")
print("|  |")
print("|__|")

# space
print("\n")

# part2
print("You don\'t frighten us, English pig-dogs!"
      + "\nGo and boil your bottoms, sons of a silly person!"
      + "\n\t-\"Monty Python and the Holy Grail\"")

# space
print("\n")

# part3
month = input("What month are we in?:")
day = input("What day is it?:")
if int(day) > 30:
    print('\n\n\n\n\nYou\'re a lying BITCH...' + "\n\n\n\n\n")
    # I added that many spaces there for comedic effect, chill
    day2 = input("I\'ll ask again, what day is it?:")
    if int(day2) > 30:
        print("\n\n\n\n\nI will never forgive you... You really gave me the wrong input twice. This is literally just "
              "a lab assignment.\n\n\n\n\n")
    # I added that many spaces there for comedic effect, chill part 2
    else:
        day_of_month = input("What day of the week is today?:")
        tomorrow = int(day)
        print("Today is " + day_of_month.capitalize() + ", " + month.capitalize() + " " + day + ". Tomorrow will be " +
              month.capitalize(), end=" ")
        print(tomorrow + 1, end=".")
else:
    day_of_month = input("What day of the week is today?:")
    tomorrow = int(day)
    print("Today is " + day_of_month.capitalize() + ", " + month.capitalize() + " " + day + ". Tomorrow will be " +
          month.capitalize(), end=" ")
    print(tomorrow + 1, end=".")
