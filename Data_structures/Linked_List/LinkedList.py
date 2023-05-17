from Node import Node


class LinkedList:
    def __init__(self, values=None):
        self.head = None
        self.tail = None

        if values is not None:
            self.add_multiple_nodes(values)

    def append(self, value):
        if self.head is None:
            self.head = self.tail = Node(value)
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next

        return self.tail

    def prepend(self, value):
        if self.head is None:
            self.head = self.tail = Node(value)
        else:
            current = self.head
            self.head = Node(value)
            self.head.next = current

        return self.head

    def add_multiple_nodes(self, values):
        for value in values:
            self.append(value)

    def find(self, value):
        return self.traveled(value).next

    def delete(self, value):
        node = self.traveled(value)
        node.next = node.next.next
        return node.next

    def insert(self, value, place):
        node = self.traveled(place)
        new_node = Node(value)
        new_node.next = node.next
        node.next = new_node
        return new_node

    def traveled(self, value):
        for node in self:
            if node.next.value == value:
                return node
        return None

    def __len__(self):
        count = 0
        node = self.head
        while node:
            count += 1
            node = node.next
        return count

    def __str__(self):
        return ' -> '.join([str(node) for node in self])

    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next
