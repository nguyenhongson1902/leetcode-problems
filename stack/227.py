# Basic Calculator II
# https://leetcode.com/problems/basic-calculator-ii/


import math


class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        curr = 0 # current integer
        operator = "+" # previous operator
        for i, c in enumerate(s):
            if c.isdigit():
                curr = curr * 10 + int(c)

            if c in "+-*/" or i == len(s) - 1:
                if operator == "+":
                    stack.append(curr)
                elif operator == "-":
                    stack.append(curr * -1)
                elif operator == "*":
                    top = stack.pop()
                    stack.append(top * curr)
                elif operator == "/":
                    top = stack.pop()
                    tmp = top / curr
                    res = math.ceil(tmp) if tmp < 0 else math.floor(tmp)
                    stack.append(res)

                operator = c # update the current operator to the previous operator
                curr = 0
        return sum(stack)
        # Time: O(n), n = len(s)
        # Space: O(n)
        