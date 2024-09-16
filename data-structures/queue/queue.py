def print_queue(queue):
    for element in queue:
        print(element, end=" ")
    print()

queue = list()

# enqueue
queue.append(0)
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)
print("enqueue: ", end="")
print_queue(queue)

# dequeue
queue.pop(0)
queue.pop(0)
print("dequeue: ", end="")
print_queue(queue)

# front
print(f"front: {queue[0]}")

# rear
print(f"rear: {queue[-1]}")