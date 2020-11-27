def make_letters_visible(letter, wrong_letters, word, visible_letters):
    if letter in word:
        for i in range(len(visible_letters)):
            # need structure to change the letters in visible_letters
            pass
    else:
        wrong_letters.append(letter)