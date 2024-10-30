class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack():
    def __init__(self):
        self.top = None

    def push(self, data):
        if self.top is None:
            self.top = Node(data)
        else:
            node = Node(data)
            node.next = self.top
            self.top = node

    def pop(self):
        if self.top is None:
            return None
        node = self.top
        self.top = self.top.next
        return node.data

    def peek(self):
        if self.top is None:
            return None
        return self.top.data

    def is_empty(self):
        return self.top is None

class Solution:
    def isValid(self, s: str) -> bool:
        stack = Stack()
        for bracket in s:
            if bracket in {"(", "[", "{"}:        
                stack.push(bracket)
            elif bracket ==')' and stack.peek() == '(':
                stack.pop()
            elif bracket ==']' and stack.peek() == '[':
                stack.pop()
            elif bracket =='}' and stack.peek() == '{':
                stack.pop()
            else:
                return False
        return stack.is_empty()