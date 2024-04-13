'''Implement Queue using Stacks'''

class Node:
    '''Node class'''
    def __init__(self, value, node_next=None):
        self.value = value
        self.next = node_next


class Stack:
    '''Stack class'''
    def __init__(self):
        self.head = None

    def append(self, value):
        '''Append value to stack'''
        self.head = Node(value, self.head)

    def pop(self):
        '''Pop value from stack'''
        if self.head is None:
            return None
        value = self.head.value
        self.head = self.head.next
        return value

    @property
    def peek(self):
        '''Get value from stack without removing it from stack'''
        return self.head.value if self.head is not None else None

    @property
    def is_empty(self):
        '''Check if stack is empty'''
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
    '''Implement Queue using Stacks class'''

    def __init__(self):
        self.first = Stack()
        self.second = Stack()

    def push(self, x: int) -> None:
        '''Push value to queue'''
        while self.first:
            self.second.append(self.first.pop())
        self.first.append(x)
        while self.second:
            self.first.append(self.second.pop())

    def pop(self) -> int:
        '''Pop value from queue'''
        return self.first.pop()

    def peek(self) -> int:
        '''Get value from queue without removing it from queue'''
        if not self.first:
            return None
        return self.first.peek

    def empty(self) -> bool:
        '''Check if queue is empty'''
        return not self.first
