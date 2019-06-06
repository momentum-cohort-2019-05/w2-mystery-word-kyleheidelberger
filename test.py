
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

