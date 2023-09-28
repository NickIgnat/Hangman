import random


def choose_random_word_from_list(list):
    word = random.choice(list)
    print(word)


word_list = ["apple", "orange", "banana", "pear", "kiwi"]
choose_random_word_from_list(word_list)


guess = input("enter a signle letter")

if len(guess) == 1 and guess.isalpha():
    print("Good guess!")
else:
    print("Oops! That is not a valid input")
