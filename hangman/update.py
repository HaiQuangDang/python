import random
import sys

def get_word():
    words = []
    with open("dictionary.txt") as file:
        words = file.read().splitlines()
    return random.choice(words)

def reveal(word, used):
    revelation = ["#" for _ in range(len(word))]
    for c in used:
        for i in range(len(word)):
            if word[i] == c:
                revelation[i] = c
    print("\t", end="")
    for c in revelation:
        print(c, end="")
    print()

def check(word, used):
    for c in word:
        if c not in used:
            return False
    else:
        return True

def game(lives):
    word = get_word()
    length = len(word)
    print(f"Guess this word: {'#' * length}")
    used = set()
    while lives > 0:
        letter = input(f">>>({'🫀 ' * lives}) Enter your guess: ".center(20))
        if letter in word:
            if letter in used:
                print("You have used this letter.")
            elif letter not in used:
                used.update(letter)
                count = word.count(letter)
                print(f'There is {count} "{letter}":')
            reveal(word, used)
            if check(word, used):
                print(f'Bingo! the word is "{word}"')
                sys.exit(0)
        elif letter not in word:
            print(f'These is NO "{letter}". You lost 1 live')
            reveal(word, used)
            lives -= 1
    else:
        print(f'Better luck next time, the word is "{word}"')

if __name__ == "__main__":
    game(lives=3)

