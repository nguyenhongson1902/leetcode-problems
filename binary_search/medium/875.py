# Koko Eating Bananas
# https://leetcode.com/problems/koko-eating-bananas/

import math
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Brute force
        # max_h = 0
        # k = int(sum(piles) / h + 1) if sum(piles) % h > 0 else sum(piles) // h
        # while True:
        #     time_used = []
        #     for pile in piles:
        #         if pile % k > 0:
        #             time_used.append((pile // k) + 1)
        #         else:
        #             time_used.append(pile // k)
        #     # print(time_used)
        #     # print(k)
        #     max_h = sum(time_used)
        #     # print(max_h)
        #     if max_h <= h:
        #         break
        #     k += 1
        # return k

        # Binary search
        def cum_hour(piles, k): # O(n), n = len(piles)
            cum_sum = 0
            for pile in piles:
                cum_sum += math.ceil(pile / k)
            return cum_sum

        min_speed = float('inf')
        possible_ks = range(1, max(piles) + 1)
        left, right = 0, max(piles) - 1
        while left <= right: # O(log(max(piles)))
            mid = (left + right) // 2
            k = possible_ks[mid]
            time_used = cum_hour(piles, k)
            if time_used <= h:
                min_speed = k if k <= min_speed else min_speed
                right = mid - 1
            else:
                left = mid + 1
        
        return min_speed
        
        # Time complexity: O(log(max(piles))*n), n = len(piles)


        
        
        