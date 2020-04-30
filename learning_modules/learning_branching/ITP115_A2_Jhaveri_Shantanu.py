# Shantanu Jhaveri, sj06434@usc.edu
# ITP 115, Spring 2020
# Assignment 2
# Description:
# This program creates a harry potter vending machine.
# It determines change and gives a discount.

# basic inputs
vending = input("Please select an item from the vending machine:" + "\na) Butterbeer: 58 knuts" + "\nb) Quill: 10 knuts"
                + "\nc) The Daily Prophet: 7 knuts" + "\nd) Book of Spells: 400 knuts").lower()

# while statement to ensure that input is correct for vending item
while vending != "a" and vending != "b" and vending != "c" and vending != "d":
    vending = input("Oops, you did not enter a valid value. Please enter a valid response (a,b,c,d):").lower()

# print statement for spacing
print("\n\n")

insta = input("Will you share this on Instagram? (y/n): ").lower()

# while statement to ensure that input is correct for coupon item
while insta != "y" and insta != "n":
    insta = input("Oops, you did not enter a valid value. Please enter a valid response (y/n):").lower()

# if/else statement to determine item and price
if vending == "a":
    item = "Butterbeer"
    price = 58

elif vending == "b":
    item = "Quill"
    price = 10

elif vending == "c":
    item = "The Daily Prophet"
    price = 7

else:
    item = "Book of Spells"
    price = 400

# if/else statement to determine if coupon will be used or not
if insta == "y":
    price = price - 5
    coupon = "(with coupon of 5 knuts)"

else:
    price = price
    coupon = "(with coupon of 0 knuts)"

# print statement for spacing
print("\n\n")

# print command to tell user what they bought
print("You bought a " + item + " for " + str(price) + " knuts " + coupon + " and paid with one galleon.")

# calculate change
change = 493 - price

# state what change is owed
print("Here is your change " + str(change) + " knuts:")
sickle = change // 29
print("Sickles: " + str(sickle))
knuts = change % 29
print("Knuts: " + str(knuts))
