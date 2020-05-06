# part 1
# not allowed to use random.shuffle(), random.sample(),
import random

wordList = ['hello', 'thanks', 'pycharm', 'example']
jumbleList = []

# This jumbles each word in the list
for i in wordList:
    jumbleWord = ""
    while i:
        randPos = random.randrange(len(i))
        jumbleWord += i[randPos]
        i = i[:randPos] + i[(randPos + 1):]
    jumbleList.append(jumbleWord)

# This jumbles each word seperately (doesnt work)
# selectedWord = random.choice(wordList)
# selectedWord_Mutable = list(selectedWord)
# for i in selectedWord:
#     jumbleWord_2 = ''
#     while i:
#         randPos_2 = random.randrange(len(selectedWord_Mutable))
#         jumbleWord_2 += i[randPos_2]
#         i = jumbleWord_2[:randPos_2] + jumbleWord_2[(randPos_2 + 1)]
#     selectedWord_Mutable.append(jumbleWord_2)
#
# print(selectedWord_Mutable)

choice = random.choice(jumbleList)
choiceIndex = jumbleList.index(choice)
correct = wordList[choiceIndex].lower().strip()
print("THIS IS THE DECIPHER GAME. ENTER 0 TO QUIT AT ANY TIME.\nTHE JUMBLED WORD YOU HAVE TO DECIPHER IS: " + str(choice).upper())
initialization = False
count = 0
game = False
while not initialization:
    while not game:
        guess = input("ENTER YOUR GUESS FOR THE DECIPHERED WORD:\n").lower().strip()
        count += 1
        if guess == correct:
            print("CORRECT | IT TOOK YOU " + str(count) + " TRIE(S)")
            initialization = True
            game = True
        elif guess == '0':
            game = True
            initialization = True
        else:
            print("WRONG ANSWER! IT HAS TAKEN YOU " + str(count) + "TRIES. TRY AGAIN | ", end='')