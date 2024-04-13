class Node:
    def __init__(self, val, freq=None, next_node=None):
        self.val=val
        self.freq=freq
        self.next=next_node

class FreqStack:
    def __init__(self):
        self.stack = None

    def push(self, val: int) -> None:
        if self.stack is None:
            self.stack=Node(val, 1)
        else:
            curr=self.stack
            while curr:
                if curr.val==val:
                    self.stack=Node(val, curr.freq+1, self.stack)
                    break
                curr=curr.next
            else:
                self.stack=Node(val, 1, self.stack)

    def pop(self) -> int:
        maxfreq=-1
        curr=self.stack
        while curr:
            if curr.freq>maxfreq:
                maxfreq=curr.freq
            curr=curr.next
        curr=self.stack
        if curr.freq==maxfreq:
            res=curr.val
            self.stack=self.stack.next
            return res
        while curr.next:
            if curr.next.freq==maxfreq:
                res=curr.next.val
                curr.next=curr.next.next
                return res
            curr=curr.next
        return None