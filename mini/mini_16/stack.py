class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def push(self, val):
        node = ListNode(val)
        node.next = self.head
        self.head = node

    def pop(self):
        res = self.head.val
        self.head = self.head.next
        return res

    def top(self):
        if self.head is not None:
            return self.head.val
        else:
            return None
