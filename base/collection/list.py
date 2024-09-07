n = [x for x in range(10)]
# n.append(10)
# n.insert(4, 100)
# n[len(n):] = [11]
# length = len(n)
# print(n)


list1 = [1, 4, 5, 2, 8, 9, 10, 26, 24, 0, 5, 5, 2, 4, 6, 5, 7]
# list1.remove(26)
# maximun = max(list1)
# list1.pop()
# list1.index(4)
# list1.count(5)
# list1[::-1]
# list1.sort()
# list1.reverse()

unique = list(set(list1))
# for number in list1:
#      if not number in unique:
#         unique.append(number)

evens = list(set([x for x in list1 if x % 2 == 0]))
odds = list(set([x for x in list1 if x not in evens]))


