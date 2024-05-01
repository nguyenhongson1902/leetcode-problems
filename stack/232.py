# Implementing Queue using Stacks
# https://leetcode.com/problems/implement-queue-using-stacks/


class MyQueue:

    def __init__(self):
        # stack1 is responsible for pushing
        # stack2 is responsible for popping
        self.stack1, self.stack2 = [], []

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> int:
        if not self.stack2:
            for _ in range(len(self.stack1)):
                x = self.stack1.pop()
                self.stack2.append(x)
        result = self.stack2.pop()
        
        # for _ in range(len(self.stack2)):
        #     x = self.stack2.pop()
        #     self.stack1.append(x)

        return result

    def peek(self) -> int:
        if not self.stack2:
            for _ in range(len(self.stack1)):
                x = self.stack1.pop()
                self.stack2.append(x)
        
        result = self.stack2[-1]
        return result

    def empty(self) -> bool:
        return len(self.stack1) == 0 and len(self.stack2) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()