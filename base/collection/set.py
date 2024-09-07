# set is immutable but add/remove is ok, no duplicate
l1 = [5, 3, 4, 3, 5, 1, 1, 2]
l2 = [5, 3, 4, 2, 1, 0]
set1 = set(l1)
# set2 = set(l2)
# set1.update(l2)
# print(0 in set1)





tuple1 = (5, 6, 7, 6, 5, 3, 7, 1)
# print(set(tuple1))


dic1 = {"quang": 1, "raymond": 2, "tyler": 3}
dic2 = {2: "hi", 1: "hello", 3: "stay away from me"}
# print(set(dic1))
# print(set(dic2))

letters = set()
letters.update("a")
letters.update("c")
letters.update("b")
letters.update("c")
for l in letters:
    print(f"{l}")
print(letters)

fruit = {"banana", "apple", "orange", "coconut", "watermelon", "tomato"}
print(fruit)


