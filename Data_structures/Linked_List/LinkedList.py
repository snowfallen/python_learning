from Node import Node


class LinkedList:
    def __init__(self, values=None):
        self.head = None
        self.tail = None

        if values is not None:
            self.add_multiple_nodes(values)

    @staticmethod
    def __create_node(value):
        return Node(value)

    def append(self, value):
        if self.head is None:
            self.head = self.tail = self.__create_node(value)
        else:
            self.tail.next = self.__create_node(value)
            self.tail = self.tail.next

        return self.tail

    def prepend(self, value):
        if self.head is None:
            self.head = self.tail = self.__create_node(value)
        else:
            current = self.head
            self.head = self.__create_node(value)
            self.head.next = current

        return self.head

    def add_multiple_nodes(self, values):
        for value in values:
            self.append(value)

    def find(self, value):
        node = self.traveled(value).next
        if node:
            return node
        return "Can't find value..."

    def delete(self, value):
        node = self.traveled(value)
        if node:
            node.next = node.next.next
            return node.next
        return "Can't find value for deleting..."

    def insert(self, value, place):
        node = self.traveled(place)
        new_node = self.__create_node(value)
        new_node.next = node.next
        node.next = new_node
        return new_node

    def traveled(self, value):
        for node in self:
            if node.next and node.next.value == value:
                return node
        return None

    def __len__(self):
        count = 0
        for _ in self:
            count += 1
        return count

    def __str__(self):
        return ' -> '.join([str(node) for node in self])

    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next
