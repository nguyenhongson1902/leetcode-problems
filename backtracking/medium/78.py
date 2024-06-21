# https://leetcode.com/problems/subsets/description/
# Subsets
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Time: O(n*2^n), n = len(nums)
        result = []
        subset = []

        def backtrack(i):
            if i == len(nums):
                result.append(subset.copy())
                return
            
            # decide to add the element, e.g. [1] (better to draw a tree)
            subset.append(nums[i])
            backtrack(i + 1)

            # decide not to add the element, []
            subset.pop()
            backtrack(i + 1)

        backtrack(0)
        return result
        '''
        [1, 2, 3]
        '''