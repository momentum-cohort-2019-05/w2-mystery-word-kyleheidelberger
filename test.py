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
    # difficulty_choice = None
    difficulty_choice = int(input("Choose 1 - 3: "))
    while True:
        if difficulty_choice in range (1,4):
            return difficulty_choice
        else:
            print("I don't know what you mean. Try again.")
            # need to fix this so menu loops
            break

# open file and put words into list
def file_to_list(file):
    # open file and close when done:
    with open("words.txt") as file:
    # read file and assign to string
        string = file.read()
        words_list = string.upper().split("\n")
    return words_list

# sort words into lists based on length
def find_easy_words(all_words_list):
    easy_words = []
    for words in all_words_list:
        if len(words) > 3 and len(words) < 7:
            easy_words == easy_words.append(words)
    return easy_words

def find_normal_words(all_words_list):
    normal_words = []
    for words in all_words_list:
        if len(words) > 5 and len(words) < 9:
            normal_words == normal_words.append(words)
    return normal_words

def find_hard_words(all_words_list):
    hard_words = []
    for words in all_words_list:
        if len(words) > 7:
            hard_words == hard_words.append(words)
    return hard_words

# pick which list to use based on user input
def pick_a_list(difficulty_choice):
    if difficulty_choice == 1:
        return pick_random_word(easy_word_list)
    elif difficulty_choice == 2:
        return pick_random_word(normal_word_list)
    elif difficulty_choice == 3:
        return pick_random_word(hard_word_list)
    else:
        exit()

# pick random word from list
def pick_random_word(word_list):
    # pick random word
    mystery_word = (random.choice(word_list))
    return mystery_word

def guess_input(mystery_word):
    # get a guess
    while True:
        guess = input("Guess a letter: ").upper()
    # make sure user only inputs one character
        if len(guess) == 1: #and been_guessed_yet is False:
            return guess
        elif len(guess) == 1: #and been_guessed_yet is True:
            print("You already guessed that. Try again.")   
        else:
            print ("Your guess must have exactly one character!")

def make_guess_list(guess):
    while True:
        guess_list == guess_list.append(guess)
        return guess_list

# def been_guessed_yet(guess, guess_list):
#     for letter in guess_list:
#         if guess == letter:
#             return True
#         else:
#             return False

def display_letter(guess, all_guesses):
    """
    Conditionally display a letter. If the letter is already in
    the list `guesses`, then return it. Otherwise, return "_".
    """
    if guess in all_guesses:
        return guess
    else:
        return "_"

def print_word(word, guesses):
    output_letters = [display_letter(guess, guesses) 
                      for guess in word]
    return (" ".join(output_letters))

def did_they_win(show_word):
    if "_" in str(show_word):
        print("Keep guessing..")
        return True
    else:
        print("You won!")
        return False

def play_again_prompt():
    play_again_input = input("Play again? Y / N: ").upper()
    if play_again_input == "Y":
        return True
    elif play_again_input == "N":
        return False
    else:
        print("I didn't get that. Try again.")

# def turn_counter(letter):
#     turns = 8
#     if letter not in word:
#         turns = turns - 1
#         return turns



if __name__ == "__main__":
    play_again = True
    while play_again:
        difficulty_choice = game_menu()
        all_words_list = file_to_list("words.txt")
        easy_word_list = find_easy_words(all_words_list)
        normal_word_list = find_normal_words(all_words_list)
        hard_word_list = find_hard_words(all_words_list)
        mystery_word = pick_a_list(difficulty_choice)
        guess_list = []
        game_round = True
        while game_round:
            word = mystery_word
            print(word)
            current_guess = guess_input(mystery_word)
            print("Current Guess:", current_guess)
            all_guesses = make_guess_list(current_guess)
            print("Your Guesses:", all_guesses)
            [display_letter(guess, all_guesses) for guess in word]
            show_word = print_word(word, all_guesses)
            print(show_word)
            game_round = did_they_win(show_word)
        play_again = play_again_prompt()