# Evaluate Reverse Polish Notation
# https://leetcode.com/problems/evaluate-reverse-polish-notation/


import math
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token not in ["+", "-", "*", "/"]:
                stack.append(int(token))
            else:
                second = stack.pop()
                first = stack.pop()
                if token == "+":
                    stack.append(first + second)
                elif token == "-":
                    stack.append(first - second)
                elif token == "*":
                    stack.append(first * second)
                else:
                    tmp = first / second
                    result = math.ceil(tmp) if tmp < 0 else math.floor(tmp)
                    stack.append(result)
        return stack[-1]
        # Time: O(n), n = #tokens
        # Space: O(n), n = #tokens