import random

HANGMAN_VISUALS = {
    0: (
        "  +---+",
        "  |   |",
        "      |",
        "      |",
        "      |",
        "      |",
        "========="
    ),
    1: (
        "  +---+",
        "  |   |",
        "  O   |",
        "      |",
        "      |",
        "      |",
        "========="
    ),
    2: (
        "  +---+",
        "  |   |",
        "  O   |",
        "  |   |",
        "      |",
        "      |",
        "========="
    ),
    3: (
        "  +---+",
        "  |   |",
        "  O   |",
        " /|   |",
        "      |",
        "      |",
        "========="
    ),
    4: (
        "  +---+",
        "  |   |",
        "  O   |",
        " /|\  |",
        "      |",
        "      |",
        "========="
    ),
    5: (
        "  +---+",
        "  |   |",
        "  O   |",
        " /|\  |",
        " /    |",
        "      |",
        "========="
    ),
    6: (
        "  +---+",
        "  |   |",
        "  O   |",
        " /|\  |",
        " / \  |",
        "      |",
        "========="
    )
}


WORD_CATEGORIES = {
    "animals": (
        "aardvark", "alligator", "alpaca", "ant", "anteater", "antelope", "ape", "armadillo", "baboon", "badger", "bat",
        "bear", "beaver", "bee", "bison", "boar", "buffalo", "butterfly", "camel", "capybara", "caribou", "cat",
        "caterpillar", "cattle", "chamois", "cheetah", "chicken", "chimpanzee", "chinchilla", "chough", "clam",
        "cobra", "cockroach", "cod", "coyote", "crab", "crane", "crocodile", "crow", "curlew", "deer", "dinosaur",
        "dog", "dogfish", "dolphin", "donkey", "dormouse", "dotterel", "dove", "dragonfly", "duck", "dugong", "dunlin",
        "eagle", "echidna", "eel", "eland", "elephant", "elk", "emu", "falcon", "ferret", "finch", "fish",
        "flamingo", "fly", "fox", "frog", "gaur", "gazelle", "gerbil", "giraffe", "gnat", "gnu", "goat", "goldfinch",
        "goldfish", "goose", "gorilla", "goshawk", "grasshopper", "grouse", "guanaco", "gull", "hamster", "hare",
        "hawk", "hedgehog", "heron", "herring", "hippopotamus", "hornet", "horse", "human", "hummingbird", "hyena",
        "ibex", "ibis", "jackal", "jaguar", "jay", "jellyfish", "kangaroo", "kingfisher", "koala", "kookaburra",
        "kouprey", "kudu", "lapwing", "lark", "lemur", "leopard", "lion", "llama", "lobster", "locust", "loris",
        "louse", "lyrebird", "magpie", "mallard", "manatee", "mandrill", "mantis", "marten", "meerkat", "mink",
        "mole", "mongoose", "monkey", "moose", "mosquito", "mouse", "mule", "narwhal", "newt", "nightingale", "octopus",
        "okapi", "opossum", "oryx", "ostrich", "otter", "owl", "ox", "oyster", "panda", "panther", "parrot",
        "partridge", "peafowl", "pelican", "penguin", "pheasant", "pig", "pigeon", "polar-bear", "pony", "porcupine",
        "porpoise", "quail", "quelea", "quetzal", "rabbit", "raccoon", "rail", "ram", "rat", "raven", "red-deer",
        "red-panda", "reindeer", "rhinoceros", "rook", "salamander", "salmon", "sand-dollar", "sandpiper", "sardine",
        "scorpion", "seahorse", "seal", "shark", "sheep", "shrew", "skunk", "snail", "snake", "sparrow", "spider",
        "spoonbill", "squid", "squirrel", "starling", "stingray", "stoat", "stork", "swallow", "swan", "tapir",
        "tarsier", "termite", "tiger", "toad", "trout", "turkey", "turtle", "viper", "vulture", "wallaby", "walrus",
        "wasp", "weasel", "whale", "wildcat", "wolf", "wolverine", "wombat", "woodcock", "woodpecker", "worm", "wren",
        "yak", "zebra"
    ),
    "countries": (
        "united states", "canada", "mexico", "brazil", "argentina", "china", "india", "russia", "australia",
        "germany", "france", "japan", "egypt", "south africa", "spain", "italy"
    ),
    "fruits": (
        "apple", "banana", "orange", "grape", "strawberry", "blueberry", "kiwi", "pineapple", "mango",
        "watermelon", "lemon", "lime", "peach"
    )
}

#  Game Functions 

def choose_word_and_difficulty():
    """
    Allows the user to select a word category and a difficulty level.
    Returns the chosen secret word and the maximum number of incorrect guesses.
    """
    # Print available categories
    print("Welcome to Hangman!")
    print("Choose a category:")
    for i, category in enumerate(WORD_CATEGORIES.keys()):
        print(f"{i+1}. {category.capitalize()}")

    # Get category choice from the user
    while True:
        try:
            category_choice = int(input("Enter the number of your choice: "))
            chosen_category_name = list(WORD_CATEGORIES.keys())[category_choice - 1]
            chosen_word_list = WORD_CATEGORIES[chosen_category_name]
            break
        except (ValueError, IndexError):
            print("Invalid category choice. Please enter a valid number.")

    # Get difficulty choice from the user
    print("\nChoose a difficulty level:")
    print("1. Easy (9 incorrect guesses)")
    print("2. Medium (6 incorrect guesses)")
    print("3. Hard (4 incorrect guesses)")
    
    while True:
        try:
            difficulty_choice = int(input("Enter the number of your choice: "))
            if difficulty_choice == 1:
                max_incorrect_guesses = 9
            elif difficulty_choice == 2:
                max_incorrect_guesses = 6
            elif difficulty_choice == 3:
                max_incorrect_guesses = 4
            else:
                print("Invalid difficulty choice. Please enter 1, 2, or 3.")
                continue
            break
        except ValueError:
            print("Invalid difficulty choice. Please enter a valid number.")

    # Randomly select a secret word from the chosen category
    secret_word = random.choice(chosen_word_list)
    return secret_word, max_incorrect_guesses

def display_game_state(incorrect_guesses, display_word, guessed_letters):
   
    # For a simple terminal application, we can simulate a clear screen.
    print("\n" * 50)  # Print a large number of newlines to "clear" the screen


    # Display the hangman based on the number of incorrect guesses.
    for line in HANGMAN_VISUALS[min(incorrect_guesses, 6)]:
        print(line)

    print("\n" + " ".join(display_word))
    print(f"\nIncorrect Guesses: {incorrect_guesses}")
    print(f"Letters Guessed: {', '.join(sorted(list(guessed_letters)))}")
    print("-" * 20)

def play_game():
    """
    Runs a single round of the Hangman game.
    """
    secret_word, max_incorrect_guesses = choose_word_and_difficulty()
    
    # Initialize game variables
    display_word = ["_"] * len(secret_word)
    incorrect_guesses = 0
    guessed_letters = set()
    is_game_over = False

    while not is_game_over:
        display_game_state(incorrect_guesses, display_word, guessed_letters)

        user_guess = input("Enter a letter to guess: ").lower()

        # Input validation
        if len(user_guess) != 1 or not user_guess.isalpha():
            print("Invalid input! Please enter a single letter.")
            input("Press Enter to continue...")
            continue
        
        if user_guess in guessed_letters:
            print(f"You already guessed the letter '{user_guess}'. Try another one.")
            input("Press Enter to continue...")
            continue
        
        # Add the valid guess to the set of guessed letters
        guessed_letters.add(user_guess)

        # Check if the guess is in the secret word
        if user_guess in secret_word:
            print(f"Good guess! The letter '{user_guess}' is in the word.")
            # Update the display word with the correct letter(s)
            for i in range(len(secret_word)):
                if secret_word[i] == user_guess:
                    display_word[i] = user_guess
        else:
            print(f"Sorry, the letter '{user_guess}' is not in the word.")
            incorrect_guesses += 1
        
        input("Press Enter to continue...")
        
        # Check for game-over conditions
        if "_" not in display_word:
            # Player has guessed the entire word
            is_game_over = True
            display_game_state(incorrect_guesses, display_word, guessed_letters)
            print("\nCongratulations! You have won the game!")
            print(f"The word was '{secret_word}'.")
        elif incorrect_guesses >= max_incorrect_guesses:
            # Player has run out of guesses
            is_game_over = True
            display_game_state(incorrect_guesses, display_word, guessed_letters)
            print("\nGame Over! You have been hanged!")
            print(f"The correct word was '{secret_word}'.")

def main():
    
    while True:
        play_game()
        
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again not in ["yes", "y"]:
            print("Thank you for playing! Goodbye.")
            break


if __name__ == "__main__":
    main()

