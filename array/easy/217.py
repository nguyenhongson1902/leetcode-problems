from typing import List
# Contains Duplicate
# https://leetcode.com/problems/contains-duplicate/description/


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # return False if len(set(nums)) == len(nums) else True
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
            if freq[num] > 1:
                return True
        return False
    # Time: O(n)
    # Space: O(n)
    

