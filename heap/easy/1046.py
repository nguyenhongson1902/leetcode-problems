# Last Stone Weight
# https://leetcode.com/problems/last-stone-weight/description/


import heapq
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Brute force, time: O(n^2log(n)), space O(1)
        # if len(stones) == 1:
        #     return stones[0]
        # stones = sorted(stones) # O(nlogn)
        # while len(stones) > 1: # O(n - 1), because we have (n - 1) pairs in a sorted array
        #     a, b = stones[-2:]
        #     diff = abs(a - b)
        #     if diff != 0:
        #         stones = stones[:-2] + [diff] # O(n)
        #         stones = sorted(stones) # O(nlogn)
        #     else:
        #         stones = stones[:-2] # O(n)
            
        # return stones[0] if len(stones) == 1 else 0

        if len(stones) == 1:
            return stones[0]

        negative_weights = [-weight for weight in stones]
        heapq.heapify(negative_weights)

        while len(negative_weights) > 1: # O(n)
            a = heapq.heappop(negative_weights) # O(logn)
            b = heapq.heappop(negative_weights) # O(logn)
            diff = abs(a - b)
            if diff != 0:
                heapq.heappush(negative_weights, -diff) # O(logn)
        return -negative_weights[0] if len(negative_weights) == 1 else 0
        # Time: O(nlogn), n = len(stones)
        # Space: O(n), n = len(stones)
        

        
        