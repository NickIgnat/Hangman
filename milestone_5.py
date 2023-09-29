import random
import re


class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word_to_guess = random.choice(word_list)
        self.word_guessed = ["_" for _ in self.word_to_guess]
        self.num_unique_ungessed_letters = len(set(self.word_to_guess))
        self.guessed_letters = []

    # converts the list of letters word_guessed into a printable string
    def word_guessed_str(self):
        guessed_word_string = ""
        guessed_word_string = guessed_word_string.join(self.word_guessed)
        return guessed_word_string

    def check_guess(self, guessed_letter):
        guessed_letter = guessed_letter.lower()

        if guessed_letter in self.word_to_guess:
            print(f"Good guess! {guessed_letter} is in the word.")

            # loop inserts the correct letter instead of underscores in word_guessed
            for position in re.finditer(guessed_letter, self.word_to_guess):
                self.word_guessed[position.start()] = guessed_letter

            self.num_unique_ungessed_letters -= 1
        else:
            self.num_lives -= 1
            print(f"Sorry, {guessed_letter} is not in the word.")
            print(f"You have {self.num_lives} lives left.")

    def ask_for_input(self):
        print("\n\n\n")
        print(self.word_guessed_str())
        guessed_letter = input("enter a signle letter:\n")

        if len(guessed_letter) != 1 or not guessed_letter.isalpha():
            print("Invalid letter. Please, enter a single alphabetical character.")
        elif guessed_letter in self.guessed_letters:
            print("You already tried that letter!")
        else:
            self.check_guess(guessed_letter)
            self.guessed_letters.append(guessed_letter)


def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list=word_list, num_lives=num_lives)
    while True:
        if game.num_lives == 0:
            print("You lost!")
            print(f"The word was {game.word_to_guess}")
            break

        if game.num_unique_ungessed_letters > 0:
            game.ask_for_input()

        else:
            print("\n\nCongratulations. You won the game!")
            print(f"\nYou have guessed the word {game.word_to_guess}!")
            break


play_game(["apple", "orange", "banana", "pear", "kiwi"])
