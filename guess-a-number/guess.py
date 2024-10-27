import random
import sys

def enter_number(str):
    while True:
        try:
            a = int(input(str))
            return a
        except:
            continue

def main():
    start = 1
    end = 100
    number = random.randint(start, end)
    chance = 7
    guess = enter_number(f"You have {chance} chances, please enter your number: ")
    while chance > 1:
        chance -= 1
        if number == guess:
            print(f"Bingo! the number is {number}")
            sys.exit(0)
        elif guess < number:
            guess = enter_number(f"You have {chance} chances, higher: ")
            continue
        elif guess > number:
            guess = enter_number(f"You have {chance} chances, lower: ")
            continue
    else:
        print(f"The number is {number}, better luck next time.")


    
if __name__ == "__main__":
    main()
