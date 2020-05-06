# Shantanu Jhaveri, SJ06434@usc.edu
# ITP 115, Spring 2020
# Lab 4-1

# notes
# 1. Take the first letter of the word and move it to the end of the word.
# 2. If the word is four letters or more, append a random vowel to the end of the
# word (aeiou).
# 3. If the word is three letters or fewer, append “en” to the end of the word.
# 5. If there is an e at the end of the word, replace it with ë (e with an umlaut). To
# type ë using Mac OS, hold down the option key and press u, and then press e.
# To type ë using Windows, hold down the ALT key and type 0235.
initialization = True

print("Elcómewó óten heten Igpén Lvísheá ránslátórtë!\n(Welcome to the Pig Elvish translator!)")
print("\n")

while initialization:
    word = input("Please enter a word you would like to translate:").lower()
    word = word.replace("k", "c")
    length = len(word)
    count = 1
    for letter in word:
        calculator = letter + str(count)
        print(calculator)
        count += 1
        if "1" in calculator:
            first_letter = calculator
        if "2" in calculator:
            second_letter = calculator





    print(word.capitalize())

    # run_again = input("Would you like to translate another word (y/n):").lower()
    # if "n" in run_again:
    #     initialization = False
    # elif "y" in run_again:
    #     initialization = True
    # else:
    #     run_again = input("You did not give a valid response. Would you like to translate another word (y/n):").lower()
