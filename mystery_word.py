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
        
# run mystery game function
def word_mystery_game (file):
    # open file and close when done:
    with open(file) as file:
    # read file and assign to string
        string = file.read()
        words_list = string.upper().split("\n")
        # import 'random' module
        import random
        # pick random word
        random_word = (random.choice(words_list))
        # get a guess
        current_guesses = input("Guess a letter: ").upper()
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

        print_word(random_word, current_guesses)

# play the game
    while True:
        difficulty_choice = (game_menu())
        if difficulty_choice < 4:
            word_mystery_game