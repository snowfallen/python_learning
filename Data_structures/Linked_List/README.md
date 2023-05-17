# Linked List
## Implementation a Linked List in Python
### Introduction
Linked Lists are among the most fundamental data structure that represents a sequence of nodes. The first element of the sequence is called the head of the Linked List while the last element corresponds to the tail.
Every node in the sequence has a pointer to the next element and optionally a pointer to the previous element. In Singly Linked Lists each node points to only the next node.

On the other hand, in Doubly Linked Lists each node points to the next as well as to the previous node.

Linked Lists are extremely useful in various scenarios. They are typically preferred over standard arrays when

- you need a constant time when adding or removing elements from the sequence
- manage memory more efficiently especially when the number of elements is unknown (if arrays you may have to constantly shrink or grow them. Note though that filled arrays usually take up less memory than Linked Lists.
- you want to insert items in the middle point more efficiently

Unlike other general purpose languages, Python does not have a built-in implementation of Linked Lists in its standard library.

```
class Node:
    def __init__(self, value, next_node=None, prev_node=None):
        self.value = value
        self.next = next_node
        self.prev = prev_node

    def __str__(self):
        return str(self.value)
        
        
class LinkedList:
    def __init__(self, values=None):
        self.head = None
        self.tail = None
        if values is not None:
            self.add_multiple_nodes(values)
            
```
