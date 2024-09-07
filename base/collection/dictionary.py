dogs = {
    "german": 4,
    "pitbull": 3,
    "chiwawa": 6
}

dogs["hmong"] = 5

for item in dogs.items():
    print(item)
# for dog in dogs:
#     print(f"{dog} - {dogs.get(dog)}")

# TODO convert number -> word
# numbers = {
#     1: "one",
#     2: "two",
#     3: "three",
#     4: "four",
#     5: "five",
#     6: "six",
#     7: "seven",
#     8: "eight",
#     9: "nine",
#     0: "zero"
# }

# sequence = input("Enter some numbers: ")
# words = ""
# for number in sequence:
#     words += numbers[int(number)] + " "
# print(words)

# TODO Emoji
def emoji_message():
    message = input("> ")
    words = message.split(" ")
    emojis = {
        ":)": "😀",
        ":(": "😞"
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    print(output)

