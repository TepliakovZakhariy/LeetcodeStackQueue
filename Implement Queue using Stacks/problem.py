class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class Stack:
    def __init__(self):
        self.head = None

    def append(self, value):
        self.head = Node(value, self.head)

    def pop(self):
        if self.head is None:
            return None
        value = self.head.value
        self.head = self.head.next
        return value

    @property
    def peek(self):
        return self.head.value if self.head is not None else None
    
    @property
    def is_empty(self):
        return self.head is None
    
    def __bool__(self):
        return not self.is_empty
    
    def __str__(self):
        values = []
        current = self.head
        while current is not None:
            values.append(current.value)
            current = current.next
        return str(values)

class MyQueue:

    def __init__(self):
        self.first=Stack()
        self.second=Stack()

    def push(self, x: int) -> None:
        while self.first:
            self.second.append(self.first.pop())
        self.first.append(x)
        while self.second:
            self.first.append(self.second.pop())

    def pop(self) -> int:
        return self.first.pop()

    def peek(self) -> int:
        if not self.first:
            return None
        return self.first.peek

    def empty(self) -> bool:
        return not self.first