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

def hide():
    input("Press enter to hide")
    for i in range(2000):
        print("\n")
    input("Press enter to continue")

def main():
    # asking for input and hiding it
    word = input("Which word?")
    hide()
    

if __name__ == "__main__":
    main()