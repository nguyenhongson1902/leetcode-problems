from typing import List
# https://leetcode.com/problems/minimum-size-subarray-sum/
# Minimum Size Subarray Sum


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1 if nums[0] >= target else 0
        if nums[0] >= target:
            return 1
        begin, end = 0, 1
        # min_len = sys.maxsize
        min_len = 1e9
        current_sum = nums[begin] + nums[end]
        while end < len(nums) and begin <= end:
            current_len = end - begin + 1
            if current_sum >= target:
                min_len = min(min_len, current_len)
                current_sum -= nums[begin]
                begin += 1
            else:
                end += 1
                if end < len(nums):
                    current_sum += nums[end]

        return 0 if min_len == 1e9 else min_len
