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
    if difficulty_choice in range (1,4):
        return difficulty_choice
    else:
        print("I don't know what you mean. Try again.")
difficulty_choice = game_menu()

# open file and put words into list
def file_to_list(file):
    # open file and close when done:
    with open("words.txt") as file:
    # read file and assign to string
        string = file.read()
        words_list = string.upper().split("\n")
    return words_list
all_words_list = file_to_list("words.txt")

# sort words into lists based on length
def find_easy_words(all_words_list):
    easy_words = []
    for words in all_words_list:
        if len(words) > 3 and len(words) < 7:
            easy_words == easy_words.append(words)
    return easy_words
easy_word_list = find_easy_words(all_words_list)

def find_normal_words(all_words_list):
    normal_words = []
    for words in all_words_list:
        if len(words) > 5 and len(words) < 9:
            normal_words == normal_words.append(words)
    return normal_words
normal_word_list = find_normal_words(all_words_list)

def find_hard_words(all_words_list):
    hard_words = []
    for words in all_words_list:
        if len(words) > 7:
            hard_words == hard_words.append(words)
    return hard_words
hard_word_list = find_hard_words(all_words_list)

# pick which list to use based on user input
def pick_a_list(difficulty_choice):
    mystery_word = None
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

mystery_word = pick_a_list(difficulty_choice)
print(mystery_word)