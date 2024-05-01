import collections
# Implement Stack using Queues
# https://leetcode.com/problems/implement-stack-using-queues/description/


class MyStack:

    def __init__(self):
        self.queue = collections.deque([])

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        return self.queue.pop()

    def top(self) -> int:
        return self.queue[-1]

    def empty(self) -> bool:
        return True if not self.queue else False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()