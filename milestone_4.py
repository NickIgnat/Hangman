import random


class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word_to_guess = random.choice(word_list)
        self.word_guessed = ["_" for _ in self.word_to_guess]
        self.num_unique_ungessed_letters = len(set(self.word_to_guess))
        self.guessed_letters = []

    def check_guess(self, guessed_letter):
        guessed_letter = guessed_letter.lower()

        if guessed_letter in self.word_to_guess:
            print(f"good guess {guessed_letter} is in the word")
        else:
            print("bad guess")

    def ask_for_input(self):
        while True:
            guessed_letter = input("enter a signle letter")

            if len(guessed_letter) != 1 or not guessed_letter.isalpha():
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guessed_letter in self.guessed_letters:
                print("You already tried that letter!")
            else:
                self.check_guess(guessed_letter)
                self.guessed_letters.append(guessed_letter)


H = Hangman(["apple", "orange", "banana", "pear", "kiwi"])
H.ask_for_input()
