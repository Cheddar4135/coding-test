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
        for char in s:
            if char == '(':
                stack.push('small')
            elif char == '{':
                stack.push('middle')
            elif char == '[':
                stack.push('big')

            elif char == ')':
                if stack.peek() == 'small':
                    stack.pop()
                else: return False
            elif char == '}':
                if stack.peek() == 'middle':
                    stack.pop()
                else: return False
            elif char ==']':
                if stack.peek() == 'big':
                    stack.pop()
                else: return False
        if stack.is_empty():
            return True
        else:
            return False