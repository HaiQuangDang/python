import random

def main():
    word = get_random_word()
    hangman(word, 10)


def get_random_word():
    words = []
    with open("dictionary.txt") as file:
        words = file.read().splitlines()
    word = random.choice(words)
    return word


def hangman(word, life):
    print("Guess this word:")
    length = len(word)
    guess = ["_" for _ in range(length)]
    letters = set()
    while "".join(guess) != word and life > 0:
        for c in guess:
            print(f"{c}", end=" ")
        print()
        print(f"You have {life} guess(es) left, and you have used these letters: ", end="")
        for l in letters:
            print(f"{l}", end=" ")
        print()
        letter = input("Your guess: ")
        if letter in letters:
            print("You've already guess this letter")
        elif not letter in letters and not letter in word:
            life -= 1
        elif not letter in letters and letter in word:
            for i in range(0, length):
                if word[i] == letter:
                    guess[i] = letter
        letters.update(letter)
    if "".join(guess) == word:
        print(f"You guess correctly the word '{word}'")
    else:
        print(f"You've failed, the word is '{word}'")

        
main()


