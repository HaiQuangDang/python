class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, node):
        self.head = node

    def print_list(self):
        tmp = self.head
        while tmp:
            print(tmp.data,end=" ")
            tmp = tmp.next
        print()

    def add_first(self, new_node):
        new_node.next = self.head
        self.head = new_node

    def add_last(self, new_node):
        tmp = self.head
        while tmp:
            if tmp.next == None:
                tmp.next = new_node
                break
            tmp = tmp.next

    def add_after(self, given_node, new_node):
        next_node = given_node.next
        new_node.next = next_node
        given_node.next = new_node

    def insert(self, new_node, index):
        if index < 0:
            print("Given index must be at least 0")
        elif index == 0:
            self.add_first(new_node)
        elif index > 0:
            i = 0
            tmp = self.head
            while tmp:
                if i + 1 == index and tmp.next:
                    new_node.next = tmp.next
                    tmp.next = new_node
                    break
                elif i + 1 == index and not tmp.next:
                    self.add_last(new_node)
                    break
                tmp = tmp.next
                i += 1
            else:
                print("Given index is out of reach")
        

                

        

def main():
    first= Node(0)
    second = Node(1)
    third = Node(2)
    fourth = Node(3)
    five = Node(4)
    six = Node(5)
    seven = Node(6)

    llist = LinkedList(first)
    llist.head.next = second
    second.next = third
    llist.print_list()

    llist.add_first(fourth)
    llist.add_last(five)
    llist.add_after(second, six)
    llist.insert(seven, 3)

    llist.print_list()

if __name__ == "__main__":
    main()