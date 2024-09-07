import csv

with open("hi.txt") as file:
    # data = file.read()
    data = file.read().splitlines()

# print(data)
# data_list = [line.strip() for line in data]
# print(data_list)
phones = []
with open("phonebook.csv") as phonebook:
    pb = csv.DictReader(phonebook)
    # for phone in pb:
    #     phones.append(phone)
    print(pb.fieldnames)
