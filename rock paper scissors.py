import random

def displayRules():
    print("\n--- Rock, Paper, Scissors, Lizard, Spock ---")
    print("Rules:")
    print("* Rock crushes Scissors & crushes Lizard")
    print("* Paper covers Rock & disproves Spock")
    print("* Scissors cut Paper & decapitate Lizard")
    print("* Lizard eats Paper & poisons Spock")
    print("* Spock smashes Scissors & vaporizes Rock\n")


def getPlayerChoice(validChoices):
    playerChoice = None
    while playerChoice not in validChoices:
        playerChoice = input(f"Enter a choice {validChoices}: ").lower()
    return playerChoice


def decideWinner(playerChoice, computerChoice, winningCases):
    if playerChoice == computerChoice:
        return "It's a tie!"
    elif computerChoice in winningCases[playerChoice]:
        return "You Win!"
    else:
        return "You Lose!"

def main():

    validChoices = ("rock", "paper", "scissors", "lizard", "spock")

    winningCases = {
        "rock": ["scissors", "lizard"],
        "paper": ["rock", "spock"],
        "scissors": ["paper", "lizard"],
        "lizard": ["spock", "paper"],
        "spock": ["scissors", "rock"]
    }

    print("Welcome to the Rock, Paper, Scissors, Lizard, Spock Game!")
    displayRules()

    # Game loop
    while True:
        playerChoice = getPlayerChoice(validChoices)
        computerChoice = random.choice(validChoices)

        print(f"\nYou chose: {playerChoice}")
        print(f"Computer chose: {computerChoice}")

        # Decide winner
        result = decideWinner(playerChoice, computerChoice, winningCases)
        print(result)

        # Ask if the player wants to continue
        playAgain = input("\nDo you want to play again? (y/n): ").lower()
        if playAgain != "y":
            print("\nThanks for playing! Goodbye ")
            break

# Run the game
if __name__ == "__main__":
    main()
