# Permutations
# https://leetcode.com/problems/permutations/
from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        N = len(nums)

        def backtrack(sol):
            if len(sol) == N:
                result.append(sol)
                return

            for x in range(N):
                if nums[x] not in sol:
                    candidate = sol + [nums[x]]
                    backtrack(candidate)
                else:
                    continue
        backtrack([])
        
        return result
            

