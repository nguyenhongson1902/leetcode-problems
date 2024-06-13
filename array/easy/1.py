# Two Sum
# https://leetcode.com/problems/two-sum/description/

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # hash_map = {}
        # for idx, num in enumerate(nums):
        #     hash_map[target - num] = idx
        
        # for idx, num in enumerate(nums):
        #     if num in hash_map and idx != hash_map[num]:
        #         return [idx, hash_map[num]]
        # Time complexity: O(n), n = len(nums)
        # Space complexity: O(n), because we're using a hash map

        # One-pass solution:
        hash_map = {}
        for idx, num in enumerate(nums):
            if target - num in hash_map:
                return [idx, hash_map[target - num]]
            else:
                hash_map[num] = idx