# Subsets II
# https://leetcode.com/problems/subsets-ii/
from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums = sorted(nums)
        subset = []
        def backtrack(i):
            if i == len(nums):
                result.append(subset.copy())
                return

            subset.append(nums[i])
            backtrack(i + 1)

            subset.pop()
            while i + 1 < len(nums) and nums[i] == nums[i + 1]: # Skipping duplicates
                i += 1

            backtrack(i + 1)
        
        backtrack(0)
        return result
        # Time: O(n*2^n), n = len(nums)
