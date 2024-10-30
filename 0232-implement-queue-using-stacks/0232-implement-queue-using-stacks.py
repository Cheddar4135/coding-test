class MyQueue:
    def __init__(self):
        self.front =[]
        self.back =[]
    def push(self, x: int) -> None:
        self.back.append(x)

    def pop(self) -> int:
        if self.empty():
            return None
        elif len(self.front):
            return self.front.pop()
        else:
            while self.back:
                self.front.append(self.back.pop())
            return self.front.pop()
        
    def peek(self) -> int:
        if self.empty():
            return None
        elif len(self.front):#front가 남아있다면
            return self.front[-1]
        else: #front에 값이 없다면
            while self.back:
                self.front.append(self.back.pop())
            return self.front[-1]
    def empty(self) -> bool:
        return not self.front and not self.back
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()