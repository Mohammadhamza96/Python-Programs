import random

def display_welcome_message(min_number, max_number):
  
    print("------ Welcome to the Enhanced Number Guessing Game ------")
    print(f"Guess a number between {min_number} and {max_number}.")
    print("You can choose different difficulty levels to adjust the range.")
    print("Easy: 1-50 | Medium: 1-100 | Hard: 1-200")
    print("Enter 'quit' at any time to exit the game.")

def get_difficulty_level():
   
    while True:
        difficulty = input("Choose difficulty (easy/medium/hard): ").strip().lower()
        if difficulty == 'easy':
            return 1, 50
        elif difficulty == 'medium':
            return 1, 100
        elif difficulty == 'hard':
            return 1, 200
        else:
            print("Invalid choice. Please select easy, medium, or hard.")

def play_game(min_number, max_number):
   
    secret_number = random.randint(min_number, max_number)
    guess_count = 0
    is_playing = True

    print(f"\nStarting game with range {min_number} to {max_number}...")

    while is_playing:
        user_input = input("Enter your guess (or 'quit' to exit): ").strip()

        if user_input.lower() == 'quit':
            print("Thanks for playing! Goodbye.")
            return 0  

        if user_input.isdigit():
            guess = int(user_input)
            guess_count += 1

            if guess < min_number or guess > max_number:
                print(f"That number is out of range. Please guess between {min_number} and {max_number}.")
            elif guess < secret_number:
                print("Too low! Try a higher number.")
            elif guess > secret_number:
                print("Too high! Try a lower number.")
            else:
                print(f"Correct! The secret number was {secret_number}.")
                print(f"You took {guess_count} guesses to win.")
                is_playing = False
                return guess_count
        else:
            print("Invalid input. Please enter a number or 'quit'.")

    return guess_count

def main():
   
    display_welcome_message(1, 100)  

    while True:
        min_number, max_number = get_difficulty_level()
        guesses = play_game(min_number, max_number)

        if guesses == 0:  
            break

        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("Thanks for playing! Goodbye.")
            break

if __name__ == "__main__":
    main()