def print_stack(stack):
    for element in stack:
        print(element, end=" ")
    print()


stack = list()

# push 
stack.append(2)
stack.append(3)
stack.append(5)
print("push: ", end="")
print_stack(stack)

# size
print(f"size: {len(stack)}")

# pop
stack.pop()
print("pop: ", end="")
print_stack(stack)

# peek or top
print(f"peek: {stack[-1]}")

# empty
print(f"empty: {len(stack) == 0}")