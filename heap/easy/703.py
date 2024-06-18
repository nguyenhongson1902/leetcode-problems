import heapq
from typing import List

# Kth Largest Element in a Stream
# https://leetcode.com/problems/kth-largest-element-in-a-stream/description/


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        heapq.heapify(self.nums) # O(n)
        while len(self.nums) > self.k: # O(n - k)
            heapq.heappop(self.nums) # O(logn)

    def add(self, val: int) -> int:
        # Brute force, time O(nlogn), time limit exceeded
        # self.nums.append(val)
        # return sorted(self.nums, reverse=True)[self.k - 1]
        
        heapq.heappush(self.nums, val) # O(logk)
        if len(self.nums) > self.k: # O(1)
            heapq.heappop(self.nums) # O(logk)
        
        result = self.nums[0]
        return result
        # Time: O(logk)
        # Space: O(1)

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)