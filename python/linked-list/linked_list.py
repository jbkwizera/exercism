class Node:
    def __init__(self, item, prev=None, next=None):
        self.item = item
        self.prev = prev
        self.next = next

class LinkedList:
    def __init__(self):
        self.size = 0
        self.head = Node(None, None, None)
        self.tail = Node(None, None, None)
        self.head.next = self.tail
        self.tail.prev = self.head


    def insert_between(self, item, prev, next):
        temp = Node(item, prev, next)
        prev.next = temp
        next.prev = temp
        self.size+= 1

    def delete_node(self, node):
        temp = node.item
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size     -= 1
        return temp

    def __len__(self):
        return self.size

    def __iter__(self):
        x = self.head.next
        while x is not self.tail:
            yield x.item
            x = x.next

    def push(self, item):
        self.insert_between(item, self.tail.prev, self.tail)

    def pop(self):
        return self.delete_node(self.tail.prev)

    def shift(self):
        return self.delete_node(self.head.next)

    def unshift(self, item):
        self.insert_between(item, self.head, self.head.next)
