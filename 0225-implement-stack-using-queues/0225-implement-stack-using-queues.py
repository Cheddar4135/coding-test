class MyStack:
    """
    2개의 큐를 이용해 스택을 구현하는 문제.
    """
    def __init__(self):
        self.q = []
        self.qtmp = []

    def push(self, x: int) -> None:
        self.q.append(x)

    def pop(self) -> int:
        while len(self.q)>1:
            self.qtmp.append(self.q.pop(0))
        top = self.q.pop()
        self.q = self.qtmp
        self.qtmp = []
        return top

    def top(self) -> int:
        while len(self.q)>1:
            self.qtmp.append(self.q.pop(0))
        # 최상위 요소 가져옴
        top = self.q[0]
        self.qtmp.append(self.q.pop(0))
        self.q = self.qtmp
        self.qtmp = []
        return top
        
    def empty(self) -> bool:
        return not self.q


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()