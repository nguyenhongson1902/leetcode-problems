# Top K Frequent Elements
# https://leetcode.com/problems/top-k-frequent-elements/

import heapq
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # nums = sorted(nums)
        # freq = {}
        # for num in nums:
        #     freq[num] = freq.get(num, 0) + 1
        
        # result = []
        # count = 0
        # for val, freq in sorted(freq.items(), key=lambda x: x[1], reverse=True):
        #     count += 1
        #     result.append(val)
        #     if count == k:
        #         break
        # return result
        # Time: O(nlog(n))
        # Space: O(n)
        
        # freq = {}
        # for num in nums: # O(n)
        #     freq[num] = freq.get(num, 0) - 1
        
        # values = []
        # for key, val in freq.items():
        #     values.append((val, key))

        # heapq.heapify(values) # O(n)
        # # print("values", values)
        # result = []
        # for _ in range(k): # O(k)
        #     val, idx = heapq.heappop(values) # O(logn)
        #     # print("val, idx", val, idx)
        #     result.append(idx) # O(1)
        # return result
        # Time O(n + klogn), n = len(nums)
        # Space O(n)

        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        buckets = [[] for i in range(len(nums))]
        for key, val in freq.items():
            buckets[val - 1].append(key)
        
        # print("buckets", buckets)
        result = []
        for i in range(len(buckets) - 1, -1, -1):
            if len(buckets[i]) != 0:
                for idx in buckets[i]:
                    result.append(idx)
                    if len(result) == k:
                        return result
        # Time: O(nk), because k is commonly less than n, the time complexity would be O(n)
        # Space: O(n)
            
        

        
