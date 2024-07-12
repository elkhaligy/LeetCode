class StackNode:
    def __init__(self, value, min_value):
        self.value = value
        self.min_value = min_value

class MinStack:

    def __init__(self):
        self.stack = []
        self.min = []

    def push(self, val: int) -> None:
        if len(self.stack) == 0:
            node = StackNode(val, val)
        else:
            if val < self.stack[-1].min_value:
                node = StackNode(val, val)
            else:
                node = StackNode(val, self.stack[-1].min_value)
        self.stack.append(node)

    def pop(self) -> None:
        val = self.stack.pop().value

    def top(self) -> int:
        return self.stack[-1].value

    def getMin(self) -> int:
        return self.stack[-1].min_value

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()