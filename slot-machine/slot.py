import random


slots = ["🍓", "🍒", "🍋", "🍇", "🎉"]
balance = 100

print("--------Slot Machine-------")
print(" - ".join(slots))
print("***************************")
print(f"Your balance: {balance}")


def spin_row():
    row = [random.choice(slots) for _ in range(3)]
    return row


def print_row(row):
    print("------", end="")
    for i in row:
        print(i, end="--")
    print("----")
    print()

def check_slot(bet, row):
    if row[0] == row[1] == row[2]:
        if row[0] == "🍓":
            return bet * 3
        elif row[0] == "🍒":
            return bet * 4
        elif row[0] == "🍋":
            return bet * 5
        elif row[0] == "🍇":
            return bet * 6
        elif row[0] == "🎉":
            return bet * 7
    else:
        return 0


while balance > 0:
    print("$$$$$$$$$$$$$$$$$$$")
    bet = input(">>> Place your bet: ")
    if not bet.isdigit():
        print("Please enter a valid number")
        continue
    bet = int(bet)
    if not bet > 0:
        print("Please bet greater then zero")
        continue
    elif bet > balance:
        print("Insufficent funds")
        continue

    row = spin_row()
    balance -= bet
    print_row(row)
    win = check_slot(bet, row)
    if win == 0:
        print("Better luck next time")
    else:
        print(f"You win: {win}")

    balance += win
    print(f"Your balance: {balance}")
    if balance == 0:
        print("You're out of money. Game's over. Thanks!")
        break

    play_again = input(">>> Do you want to play again (y/n): ")
    if play_again.lower() not in ["y", "yes"]:
        print("Gam's over. Thank you for your time!")
        break

    


    