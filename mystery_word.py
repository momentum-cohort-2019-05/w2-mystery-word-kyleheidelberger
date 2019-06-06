
# don't run if imported
if __name__ == "__main__":
    # run mystery game function
    def word_mystery_game (file):
        # open file and close when done:
        with open(file) as file:
        # read file and assign to string
            string = file.read()
            words_list = string.upper().split("\n")
            # make dictionary
            # word_length_dictionary = {}
            # for word in words_list:
            #     words = len(word)
            #     if words in word_length_dictionary:
            #         word_length_dictionary[words].add(word)
            #     else:
            #         word_length_dictionary[words] = {word}
            # return word_length_dictionary

            # def choose_word_list(words_list):
            #     length
            #     for length in range(4,7)
                
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

    # check if okay filetype to open
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