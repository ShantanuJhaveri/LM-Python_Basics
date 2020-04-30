# Shantanu Jhaveri, sj06434@usc.edu
# ITP 115, Spring 2020
# Lab 2-1

# inputs
size = input("What size coffee do you want (S, M, L)?").lower()
while size != "s" and size != "m" and size != "l":
    size = input("Oops, you did not enter a valid value. Please enter a valid response (S,M,L):")
temp_question = input("What temperature would you like (in degrees)?")
temp_number = [int(i) for i in temp_question.split() if i.isdigit()]
temp = temp_number[0]
blend = input("What type of beans / blend would you like?").capitalize()
cream = input("Would you like room for cream (y/n)?").lower()
while cream != "y" and cream != "n":
    cream = input("Oops, you did not enter a valid value. Please enter a valid response (S,M,L):")

# size calibration
if size == "m":
    final_size = "medium"

elif size == "s":
    final_size = "small"

elif size == "l":
    final_size = "large"

else:
    final_size = "unspecified size"

# temperature calibration
if temp > 90:
    final_temp = "hot"

else:
    final_temp = "iced"

# determination of cream
if cream == "y":
    final_cream = "with room for cream"

else:
    final_cream = "without room for cream"

# print statement
print("You ordered a " + final_size + " " + final_temp + " " + blend + " " + final_cream + ".")
