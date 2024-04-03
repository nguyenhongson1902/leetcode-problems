# Daily Temperatures
# https://leetcode.com/problems/daily-temperatures/description/

# Monotonic Stack


from collections import deque
from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = deque([[temperatures[0], 0]])
        i = 1
        while i < len(temperatures):
            while stack and temperatures[i] > stack[-1][0]:
                temp, idx = stack.pop()
                result[idx] = i - idx
            stack.append([temperatures[i], i])
            i += 1
        
        return result

        