# Kth Largest Element in an Array
# https://leetcode.com/problems/kth-largest-element-in-an-array/

import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # sorting, easy, time O(nlogn), space O(1)
        
        # without sorting
        # Using min heap
        # heapq.heapify(nums) # O(n)
        # while len(nums) > k: # O(n - k), n = len(nums)
        #     heapq.heappop(nums) # O(logn)
        
        # return nums[0]
        # Time: O(n) + O((n-k)logn) = O((n-k)logn), n = len(nums)
        # When k is much smaller than n, time O(nlogn)
        # Space: O(1)

        # Using max heap
        nums = [-n for n in nums] # O(n)
        heapq.heapify(nums)

        for _ in range(k): # O(k)
            result = heapq.heappop(nums) # O(logn)
        return -result
        # Time: O(n + klogn), n = len(nums)
        # When k << n, time complexity O(n)
        # Space: O(n)

        # Using quick select algorithm
        # Time: O(n) on average, O(n^2) in the worst-case scenarios
        # Space: O(1), in-place

        # k = len(nums) - k
        # def quick_select(left, right):
        #     p, pivot = left, nums[right]
        #     for i in range(left, right):
        #         if nums[i] <= pivot:
        #             nums[p], nums[i] = nums[i], nums[p]
        #             p += 1
            
        #     nums[p], nums[right] = nums[right], nums[p]

        #     if p > k:
        #         return quick_select(left, p - 1)
        #     elif p < k:
        #         return quick_select(p + 1, right)
        #     else:
        #         return nums[p]
        
        # return quick_select(0, len(nums) - 1)

