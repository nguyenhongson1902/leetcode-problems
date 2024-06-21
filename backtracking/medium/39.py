# Combination Sum
# https://leetcode.com/problems/combination-sum/description/
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        
        comb = []
        def backtrack(i):
            if sum(comb) == target:
                result.append(comb.copy())
                return
            elif sum(comb) > target:
                return
            
            if i == len(candidates):
                return
            
            comb.append(candidates[i])
            backtrack(i)

            comb.pop()
            backtrack(i + 1)
        backtrack(0)
        return result


        # Time O(2^target)
