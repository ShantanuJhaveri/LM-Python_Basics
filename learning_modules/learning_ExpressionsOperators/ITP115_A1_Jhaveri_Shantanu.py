# Shantanu Jhaveri, sj06434@usc.edu
# ITP 115, Spring 2020
# Assignment 1
# Description:
# This program creates a Mad Libs story that was generated through an interview with a 10 year old cousin.
# The text generated is what he wanted.
# The code takes an input from the user and prints output, which in this case is the Mad Lib.

# 5 strings requirement
print("\n\n\nPlease refrain from entering spaces after the \":\" and after your input.\n\n\n")
name = str(input("Enter a name:").capitalize())
name1_gender = str(input("Enter the gender of " + '"{}"'.format(name) + " by stating his or her:").lower())
name2 = str(input("Enter another name:").capitalize())
name2_gender = str(input("Enter the gender of " + '"{}"'.format(name2) + " by stating his or her:").lower())
animal = str(input("Enter an animal (singular):").lower())
animal2 = str(input("Enter another animal (singular):").lower())
adjective1 = input("Enter an adjective:").lower()
adjective2 = input("Enter another adjective:").lower()
verb = input("Enter a verb:").lower()
gerund = input("Enter a verb ending in 'ing':").lower()

# 3 numbers requirement
number = int(input("Enter a number:"))
number2 = int(input("Enter a second number:"))
number3 = int(input("Enter a third number:"))

# 1 float requirement
decimal = float(input("Enter a number with a decimal:"))

# spaces
print("\n\n\n")

# Madlib story
print('"{}"'.format(name) + ", the " + '"{}"'.format(adjective1) + " " + '"{}"'.format(animal) + ", loved it when " +
      '"{}"'.format(name2) + ", the " + '"{}"'.format(adjective2) + " " + '"{}"'.format(animal2) + ", would gargle the "
      + '"{}"'.format(number) + " tons of saliva in " + '"{}"'.format(name2_gender) + " mouth.")
print("Sometimes, " + '"{}"'.format(name) + " would push " + '"{}"'.format(name2) + " to the limit by adding " +
      '"{}"'.format(number2) + " additional tons to the mix. That meant " + '"{}"'.format(name2) + " would have " +
      '"{}"'.format(number + number2) + " tons of saliva in his mouth. I know, " + '"{}"'.format(name) +
      " is a pretty crazy guy, right...")
print("Anyways, I think we should " + '"{}"'.format(verb) + " in a cave with " + '"{}"'.format(name) +
      " to end this madness before it's too late. This way " + '"{}"'.format(name2) + " can continue " +
      '"{}"'.format(gerund) + " in piece, ya feel. We will give " + '"{}"'.format(name2) + " approximately " +
      '"{}"'.format(decimal) + " oz of water to gargle to prevent withdrawals from past habits.")
print("We will probably have to " + '"{}"'.format(verb) + " with " + '"{}"'.format(name) + " for at least " +
      '"{}"'.format(number3) + " years before this weird interaction is over.")
