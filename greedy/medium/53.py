# https://leetcode.com/problems/maximum-subarray/description/
# Maximum Subarray
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # max_sum = float('-inf')
        # for i in range(len(nums)):
        #     if i > 0:
        #         curr_sum -= nums[i - 1]
        #     curr_sum = nums[i]
        #     for j in range(i, len(nums)):
        #         if j > i:
        #             curr_sum += nums[j]
        #         max_sum = max(max_sum, curr_sum)

        # return max_sum
        # Time: O(n^2), n = len(nums)
        # Space: O(1)

        # Kadane's algorithm, easier to understand
        # max_sum = nums[0]
        # curr_sum = nums[0]
        # for i in range(1, len(nums)):
        #     curr_sum = max(curr_sum + nums[i], nums[i])
        #     max_sum = max(max_sum, curr_sum)
        
        # return max_sum

        # Time: O(n), n = len(nums)
        # Space: O(1)

        # Neetcode's solution: Negative sum don't contribute to find the maximum sum
        max_sum = float('-inf')
        curr_sum = 0
        for i in range(len(nums)):
            curr_sum += nums[i]
            max_sum = max(max_sum, curr_sum)
            if curr_sum < 0:
                curr_sum = 0
        return max_sum

            
