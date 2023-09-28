import random


def choose_random_word_from_list(list):
    word = random.choice(list)

    return word


def check_guessed_letter(guessed_letter):
    guessed_letter = guessed_letter.lower()
    if guessed_letter in word_to_guessed_letter:
        print(f"Good guess! {guessed_letter} is in the word.")
    else:
        print(f"Sorry, {guessed_letter} is not in the word. Try again.")


def ask_for_input(word_to_guessed_letter):
    while True:
        guessed_letter = input("enter a signle letter")

        if len(guessed_letter) == 1 and guessed_letter.isalpha():
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")

    check_guessed_letter(guessed_letter)


word_list = ["apple", "orange", "banana", "pear", "kiwi"]
word_to_guess = choose_random_word_from_list(word_list)
ask_for_input(word_to_guess)
