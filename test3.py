word = "MAGNITUDE"
current_guesses = ["G", "E", "T"]

def display_letter(letter, guesses):
    """
    Conditionally display a letter. If the letter is already in
    the list `guesses`, then return it. Otherwise, return "_".
    """
    if letter in guesses:
        return letter
    else:
        return "_"

[display_letter(letter, current_guesses)
 for letter in word]

def print_word(word, guesses):
    output_letters = [display_letter(letter, guesses) 
                      for letter in word]
    print(" ".join(output_letters))
    
print_word(word, current_guesses)

def print_word(word, guesses):
    output_letters = []
    for letter in word:
        output_letters.append(display_letter(letter, guesses))
    print(" ".join(output_letters))
    
print_word(word, current_guesses)