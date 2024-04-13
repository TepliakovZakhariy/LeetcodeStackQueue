class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class Queue:
    def __init__(self):
        self.head = None
    
    def put(self, value):
        if self.head is None:
            self.head = Node(value)
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = Node(value)
    
    def get(self):
        if self.head is None:
            return None
        value = self.head.value
        self.head = self.head.next
        return value
    
    def empty(self):
        return self.head is None
    
    def top(self):
        return self.head.value if self.head is not None else None
    
    def __str__(self):
        values = []
        current = self.head
        while current is not None:
            values.append(current.value)
            current = current.next
        return str(values)

class MyStack:

    def __init__(self):
        self.first=Queue()
        self.second=Queue()

    def push(self, x: int) -> None:
        if not self.first.empty():
            self.second.put(x)
            while not self.first.empty():
                self.second.put(self.first.get())
        elif not self.second.empty():
            self.first.put(x)
            while not self.second.empty():
                self.first.put(self.second.get())
        else:
            self.first.put(x)

    def pop(self) -> int:
        if not self.first.empty():
            return self.first.get()
        elif not self.second.empty():
            return self.second.get()
        else:
            return None

    def top(self) -> int:
        if not self.first.empty():
            elem=self.first.get()
            self.push(elem)
            return elem
        elif not self.second.empty():
            elem=self.second.get()
            self.push(elem)
            return elem
        else:
            return None

    def empty(self) -> bool:
        return self.first.empty() and self.second.empty()