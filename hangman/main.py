def make_found_letters_visible(letter, wrong_letters, word, visible_letters):
    if letter in word:
        for i in range(len(visible_letters)):
            if word[i] == letter:
                visible_letters[i] = letter
    else:
        wrong_letters.append(letter)

def print_found_letters(visible_letters):
    for i in visible_letters:
        print(i, end="")
    print()

def hide():
    input("Press enter to hide")
    for i in range(2000):
        print("\n")
    input("Press enter to continue")

def main():
    # asking for input and hiding it
    word = input("Which word?").lower()
    hide()
    print("Creating word...")
    visible_letters = ["_"] * len(word)
    wrong_letters = []
    print("there are", len(word), "letters")
    while "_" in visible_letters:
        print_found_letters(visible_letters)
        print("You guessed", len(wrong_letters), "letters wrong")
        letter = input("Which letter is in the word? ")
        while len(letter) != 1:
            letter = input("Error, try again. Which letter is in the word? ")
        make_found_letters_visible(letter.lower(), wrong_letters, word, visible_letters)
        if len(wrong_letters) == 8:
            raise ConnectionAbortedError ("Hangman died.")
    print("Word found!")
    print("The word was:")
    print_found_letters(visible_letters)

if __name__ == "__main__":
    main()
