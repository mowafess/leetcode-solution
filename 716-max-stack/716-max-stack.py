class MaxStack:

    def __init__(self):
        self.stack = []
        
    def push(self, x: int) -> None:
        maximum = x if not self.stack else max(x, self.peekMax())
        self.stack.append((x, maximum))
        
    def pop(self) -> int:
        return self.stack.pop()[0]
        
    def top(self) -> int:
        return self.stack[-1][0]

    def peekMax(self) -> int:
        return self.stack[-1][1]

    def popMax(self) -> int:
        maximum = self.peekMax()
        temp = []
        while self.top() != maximum:
            temp.append(self.pop())
        
        self.pop()
        
        for item in reversed(temp):
            self.push(item)
        
        return maximum


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()