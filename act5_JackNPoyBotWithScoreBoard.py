import random


def main():
    print("\nWelcome to Jack 'n Poy Game!")
    name = input("Enter your name: ")
    game(name)
    while True:
        try:
            print("Play Again?")
            print("Press 1> Continue\nPress 2> End")
            x = int(input("Option: "))
            if (x == 2):
                print("Thank you for playing")
                break
            elif x==1:
                game(name)
            else:
                print("Invalid")
        except ValueError:
            print("Enter only number")

def game(name):
    botCount = 0
    playerCount = 0
    race = 0
    print("1.Rock  2.)Paper  3.)Scissors")
    while True:
        try:
            print("------------------------------------")
            race += 1
            print("\nRace: ", race, "of 5")
            print(name, ": ", playerCount, "        Bot: ", botCount)
            bot = random.randint(1, 3)
            while True:
                try:
                    playerChoice = int(input("Choose number: "))
                    if(playerChoice<4 and playerChoice!=0):
                        break
                    else:
                        print("Enter only numbers from 1 to 3")
                except ValueError:
                    print("Invalid")

            # Player choice
            if (playerChoice == 1):
                print(name, ": Rock | ",end="")
            elif (playerChoice == 2):
                print(name, ": Paper | ",end="")
            else:
                print(name, ": Scissors | ",end="")       
            
            # Bot choice
            if (bot == 1):
                print("Computer: Rock")
            elif (bot == 2):
                print("Computer: Paper")
            else:
                print("Computer: Scissors")

            # Player choice
            if (playerChoice == 1 and bot == 3):
                playerCount += 1
            elif (playerChoice == 2 and bot == 1):
                playerCount += 1
            elif (playerChoice == 3 and bot == 2):
                playerCount += 1
            elif (playerChoice == bot):
                print("Tie!")
                # race -= 1
            else:
                botCount += 1

            # Who wins?
            if (race == 5):
                winGame(botCount, playerCount, name)
                break
        except ValueError:
            print("Enter only numbers")


def winGame(botCount, playerCount, name):
    print("------------------------------------")
    print("The game is over!")
    print("[SCORE:   Player:",playerCount,"     Computer:",botCount,"]")
    if (botCount > playerCount):
        print("Computer win the game\n")
    elif (playerCount > botCount):
        print(name, " when the game\n")
    else:
        print("No winner. The game is Tie\n")
    print("------------------------------------")


main()
