# 153. Find Minimum in Rotated Sorted Array
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/

from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        min_val = float('inf')
        while left <= right:
            if nums[left] <= nums[right]: # Only right for rotated sorted array, because after we found the direction to search (left or right), the partial array actually was sorted. 
                min_val = nums[left] if nums[left] <= min_val else min_val
                break
            mid = (left + right) // 2
            min_val = nums[mid] if nums[mid] <= min_val else min_val
            if nums[mid] >= nums[left]:
                left = mid + 1
            else:
                right = mid - 1
        
        return min_val
        # Time: O(logn)
        # Logic: 
        # If nums[mid] >= nums[left]: 
        # search right
        # else:
        # search left

            
        