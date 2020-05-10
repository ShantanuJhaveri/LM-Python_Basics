# functions assignment through A7
# description:
# Write a program that allows the user to play Rock, Paper, Scissors against the
# computer.
# When the program begins, you randomly choose a number from 0 to 2, which will
# represent the computer’s choice with 0 for rock, 1 for paper, or 2 for scissors.
# The user then enters his/her choice of 0 for rock, 1 for paper, or 2 for scissors.
import random

run = True


def displayMenu():
    print("Welcome! Let's play rock, paper, scissors."
          "\nThe rules of the game are:"
          "\n\tRock smashes scissors"
          "\n\tScissors cut paper"
          "\n\tPaper covers rock"
          "\n\tIf both the choices are the same, it's a tie")


def getComputerChoice():
    return random.randrange(0, 3)


def getPlayerChoice():
    while run:
        try:
            playerMove = int(input(""))
        except ValueError:
            print("Not Valid response. Please choose (0) for rock, (1) for paper or (2) for scissors")
            continue
        if playerMove not in range(0, 3):
            print("Not Valid response. Please choose (0) for rock, (1) for paper or (2) for scissors")
            continue
        else:
            break


gameCalc = {
    0: 2,
    1: 0,
    2: 1
}


def playRound(computerChoice, playerChoice):
    if gameCalc[computerChoice] == playerChoice:
        return -1
    elif computerChoice == playerChoice:
        return 0
    else:
        return 1


def continueGame():
    while run:
        continueRequest = input("Do you want to continue playing (y or n)?")
        if continueRequest in ('y', 'n'):
            break
        else:
            print("not a valid input")
    if continueRequest == 'y':
        return True
    else:
        return False


def names():
    def convert(input):
        if input == 0:
            return "rock"
        elif input == 1:
            return "paper"
        elif input == 2:
            return "scissors"


def main():
    w = 0
    l = 0
    t = 0

    while run:
        displayMenu()

        computerChoice = getComputerChoice()
        playerChoice = getPlayerChoice()

        print("You chose " + str(names(playerChoice)))
        print("The computer chose " + str(names(computerChoice)))

        final = playRound(computerChoice, playerChoice)

        if final == 0:
            print("Tie!")
            t += 1
        elif final == 1:
            print("You won!")
            w += 1
        elif final == -1:
            print("You lost!")
            l += 1
        if continueGame() == True:
            continue

        else:
            print("You won ", w, " game(s).")
            print("You lost ", l, " game(s).")
            print("You tied ", t, "time(s).")
            break

main()