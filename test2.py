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
        letter = input("Guess a letter: ").upper()
    # make sure user only inputs one character
        if len(letter) == 1: #and been_guessed_yet(guess, current_guesses) == False:
            return letter   
        # elif len(letter) == 1: and been_guessed_yet(guess, current_guesses) == True:
        #     print("You already guessed that letter. Guess again!")
        else:
            print ("Your guess must have exactly one character!")

def make_guess_list(letter):
    current_guesses = []
    while True:
        current_guesses == current_guesses.append(letter)
    return current_guesses

# def been_guessed_yet(guess, current_guesses):
#     for letter in current_guesses:
#         if guess == letter:
#             return True
#         else:
#             return False


def display_letter(letter, current_guesses):
    """
    If letter is already in the list of guesses, return it. Otherwise, return "_".
    """
    if letter in current_guesses:
        return letter
    else:
        return "_"

# def turn_counter(letter):
#     turns = 8
#     if letter not in word:
#         turns = turns - 1
#         return turns


def print_word(word, guesses, turns):
    output_letters = []
    for letter in word:
        output_letters.append(display_letter(letter, guesses))
    print((" ".join(output_letters)) + "\n" + "You have", turns, "guesses left.")



if __name__ == "__main__":
    difficulty_choice = game_menu()
    all_words_list = file_to_list("words.txt")
    easy_word_list = find_easy_words(all_words_list)
    normal_word_list = find_normal_words(all_words_list)
    hard_word_list = find_hard_words(all_words_list)
    mystery_word = pick_a_list(difficulty_choice)
    word = mystery_word
    user_input = guess_input(mystery_word)
    current_guesses = make_guess_list(user_input)
    # current_guess = display_letter(user_input, current_guesses)
    print("Your Guesses:", current_guesses)
   
    # turns_left = turn_counter(user_input)
    print_word(mystery_word, current_guesses) #turns_left)