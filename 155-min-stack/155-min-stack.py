class Stack:
    def __init__(self):
        self.stack_list = []

    def is_empty(self):
        return len(self.stack_list) == 0

    def top(self):
        if self.is_empty():
            return None
        return self.stack_list[-1]

    def size(self):
        return len(self.stack_list)

    def push(self, value):
        self.stack_list.append(value)

    def pop(self):
        if self.is_empty():
            return None
        return self.stack_list.pop()


class MinStack(Stack):

    def __init__(self):
        super().__init__()

    def push(self, val: int) -> None:
        super().push([val, min(val, self.getMin())])
        

    def pop(self) -> None:
        if not self.stack_list:
            return -1
        return super().pop()[-1]

    def top(self) -> int:
        return super().top()[0]

    def getMin(self) -> int:
        return float("inf") if not self.stack_list else super().top()[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()