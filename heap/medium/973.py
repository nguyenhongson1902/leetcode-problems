# K Closest Points to Origin
# https://leetcode.com/problems/k-closest-points-to-origin/description/

import heapq
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Brute force
        # def distance(point):
        #     return (point[0]**2 + point[1]**2)**0.5
        
        # tmp = {}
        # for idx, point in enumerate(points):
        #     tmp[idx] = distance(point)
        
        # tmp = sorted(tmp.items(), key = lambda x: x[1])
        # result = []
        # for i in range(k):
        #     result.append(points[tmp[i][0]])
        # return result
        # Time: O(k + nlogn) = O(nlogn), n = len(points)
        # Space: O(n) + O(k) = O(n)

        # def distance(point):
        #     return (point[0]**2 + point[1]**2)

        # # Build a max heap
        # tmp = {}
        # for idx, point in enumerate(points): # O(n)
        #     tmp[idx] = distance(point)
        
        # max_heap = []
        # for key, val in tmp.items(): # O(n)
        #     heapq.heappush(max_heap, (-val, key)) # O(logk), because we maintain a max heap of size k
        #     if len(max_heap) > k:
        #         heapq.heappop(max_heap) # O(logk)
        
        # result = []
        # for pair in max_heap: # O(k)
        #     result.append(points[pair[1]])
        
        # return result
        # Time: O(n) + O(k) + O(nlogk) = O(nlogk), n = len(points)
        # Space: O(n) + O(k) + O(k) = O(n)


        def distance(point):
            return (point[0]**2 + point[1]**2)

        tmp = {}
        for idx, point in enumerate(points): # O(n)
            tmp[idx] = distance(point)

        min_heap = []
        for key, val in tmp.items(): # O(n)
            min_heap.append((val, key))
        
        heapq.heapify(min_heap) # O(n)

        result = []
        for _ in range(k): # O(k)
            pair = heapq.heappop(min_heap) # O(logn)
            result.append(points[pair[1]])
            if len(result) == k:
                return result
        # Time: O(n + klogn)
        # Space: O(n)