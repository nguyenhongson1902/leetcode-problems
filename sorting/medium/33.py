from typing import List
# Search in Rotated Sorted Array
# https://leetcode.com/problems/search-in-rotated-sorted-array/description/
# Visualization: Neetcode, binary search


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        # left_most, right_most = nums[0], nums[-1]
        while left <= right:
            # print(left, right)
            mid = (left + right) // 2
            left_most, right_most = nums[left], nums[right]
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                if nums[mid] >= left_most: # we are in the left sorted part
                    if target >= left_most:
                        right = mid - 1
                    else:
                        left = mid + 1
                else:
                    right = mid - 1
            else:
                if nums[mid] >= left_most: # we are in the left sorted part
                    left = mid + 1
                else:
                    if target <= right_most:
                        left = mid + 1
                    else:
                        right = mid - 1
        return -1
    # Time: O(log(n))
    # Space: O(1)
                
                
