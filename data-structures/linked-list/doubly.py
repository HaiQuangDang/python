class DoublyNode:
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev
    def __str__(self):
        return str(self.val)
    

def display(head):
    curr = head
    elements = []
    while curr:
        elements.append(str(curr.val))
        curr = curr.next
    print(" -> ".join(elements))


def insert_at_beginning(head, tail, val):
    new_node = DoublyNode(val, next=head)
    head.prev = new_node
    return new_node, tail


def insert_at_end(head, tail, val):
    new_node = DoublyNode(val, prev=tail)
    tail.next = new_node
    return head, new_node


def find(head, val):
    curr = head
    while curr:
        if curr.val == val:
            return True
        curr = curr.next
    else: 
        return False


def delete_node(head, tail, val):
    curr = head
    if head.val == val and not head.next:
        return None, None
    while curr:
        if curr.val == val:
            if curr.val == head.val:
                head.next.prev = None
                head = head.next
            elif curr.prev and curr.next:
                curr.prev.next = curr.next
                curr.next.prev = curr.prev
            elif curr.val == tail.val:
                tail = tail.prev
                tail.next = None
        curr = curr.next
    return head, tail

head = tail = DoublyNode(1)
head, tail = insert_at_beginning(head, tail, 3)
head, tail = insert_at_end(head, tail, 2)
head, tail = insert_at_end(head, tail, 4)

display(head)
head, tail = delete_node(head, tail, 4)
display(head)
head, tail = delete_node(head, tail, 2)
display(head)
head, tail = delete_node(head, tail, 1)
display(head)