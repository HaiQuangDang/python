import random

start = 1
end = 100
number = random.randint(start, end)
guess = int(input(f"Guess a number between {start} - {end}: "))

while guess != number:
    if guess < number:
        guess = int(input("higher: "))
    elif guess > number:
        guess = int(input("lower: "))
print(f"Correct the number is {number}")

