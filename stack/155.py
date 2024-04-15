# Min Stack
# https://leetcode.com/problems/min-stack/description/


class MinStack:

    def __init__(self):
        self.stack = []
        self.min_of_top = []

    def push(self, val: int) -> None:
        if self.stack:
            if val < self.min_of_top[-1]:
                self.min_of_top.append(val)
            else:
                self.min_of_top.append(self.min_of_top[-1])
        else:
            self.min_of_top.append(val)
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.min_of_top.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_of_top[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()