# import modules
import random

def game_menu():
    """
    Menu that prompts user to select desired difficulty.
    """
    print("\n" + '{:^60}'.format("Welcome To") + "\n")
    print("?"*60)
    print("\n" + '{:^60}'.format("Mystery Word"))
    print("\n" + "?"*60 + "\n")
    print("Choose Your Difficulty:")
    print("1 - Easy (Words with 4-6 Letters)")
    print("2 - Normal (Words with 6-8 Letters)")
    print("3 - Hard (Words with 8+ Letters)")
    print("\n")
    # return the choice with a valid input
    
    while True:
        difficulty_choice = int(input("Choose 1 - 3: "))
        if difficulty_choice < 4:
            return difficulty_choice
        else:
            print("I don't know what you mean. Try again.")

game_menu()

difficulty_choice = difficulty_choice
def pick_list(difficulty_choice):
    if difficulty_choice == 1:
        word_mystery_game(file)

pick_list(difficulty_choice)

# open file and put words into list
def word_mystery_game (file):
    # open file and close when done:
    with open(file) as file:
    # read file and assign to string
        string = file.read()
        words_list = string.upper().split("\n")
    return words_list

# pick random word from list
def pick_random_word(words_list):
    # import 'random' module
    import random
    # pick random word
    random_word = (random.choice(words_list))
    return random_word

def guess_input(random_word):
    # get a guess
    current_guesses = input("Guess a letter: ").upper()
    # reprint the word
    print_word(random_word, current_guesses)

def display_letter(letter, guesses):
    """
    If letter is in guesses, return it. Otherwise, return "_".
    """
    if letter in guesses:
        return letter
    else:
        return "_"

def print_word(word,guesses):
    output_letters = []
    for letter in word:
        output_letters.append(display_letter(letter, guesses))
    print((" ".join(output_letters)) + "\n" + "You have 8 guesses left.")


# identifies valid file to run - don't mess with this!
if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        word_mystery_game(file)
    else:
        print(f"{file} does not exist!")
        exit(1)