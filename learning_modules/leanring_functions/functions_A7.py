# functions assignment through A7
# description:
# Write a program that allows the user to play Rock, Paper, Scissors against the
# computer.
# When the program begins, you randomly choose a number from 0 to 2, which will
# represent the computer’s choice with 0 for rock, 1 for paper, or 2 for scissors.
# The user then enters his/her choice of 0 for rock, 1 for paper, or 2 for scissors.
import random
run = True

def main():

def displayMenu():
    print("Welcome! Let's play rock, paper, scissors."
          "\nThe rules of the game are:"
          "\n\tRock smashes scissors"
          "\n\tScissors cut paper"
          "\n\tPaper covers rock"
          "\n\tIf both the choices are the same, it's a tie")

def getComputerChoice():
    return random.randrange(0,3)

def playerChoice():
    while run:
        try:
            playerMove = int(input(""))
        except ValueError:
            print("Not Valid response. Please choose (0) for rock, (1) for paper or (2) for scissors")
            continue
        if playerMove not in range(0,3):
            print("Not Valid response. Please choose (0) for rock, (1) for paper or (2) for scissors")
            continue
        else:
            break

gameCalc = {
    0:2,
    1:0,
    2:1
}
def playRound(computerChoice, playerChoice):
    if gameCalc[computerChoice] == playerChoice:
        return -1
    elif computerChoice == playerChoice:
        return 0
    else:
        return 1


def continueGame():
    print(run)


