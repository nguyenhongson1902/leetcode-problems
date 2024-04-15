from typing import List
# Binary Search
# https://leetcode.com/problems/binary-search/description/



class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # def binary_search(nums, left, right, target):
        #     if left <= right:
        #         mid = (right + left) // 2
        #         if nums[mid] == target:
        #             return mid
        #         elif nums[mid] > target:
        #             return binary_search(nums, left, mid - 1, target)
        #         else:
        #             return binary_search(nums, mid + 1, right, target)
        #     else:
        #         return -1 # base case
        
        # result = binary_search(nums, 0, len(nums) - 1, target)

        # return result

        # Time: O(log(n))
        # Space: O(1)

        def binary_search(nums, left, right, target):
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            
            return -1
        
        result = binary_search(nums, 0, len(nums) - 1, target)
        return result

        # Time: O(log(n))
        # Space: O(1)