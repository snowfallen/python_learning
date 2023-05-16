from typing import List


class Stack:
    def __init__(self):
        self.items: List = []

    def is_empty(self) -> bool:
        return not self.items

    def push(self, item) -> None:
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peak(self):
        return self.items[-1]

    def size(self) -> int:
        return len(self.items)

    def __str__(self) -> str:
        return str(self.items)
