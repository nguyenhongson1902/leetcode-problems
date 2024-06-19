# Task Scheduler
# https://leetcode.com/problems/task-scheduler/


import heapq
from collections import deque
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # if len(tasks) == 1 or n == 0:
        #     return len(tasks)

        freq = {}
        for task in tasks: # O(m), m = len(tasks)
            freq[task] = freq.get(task, 0) + 1
        
        max_heap = [-times for task_name, times in freq.items()] # O(26)
        heapq.heapify(max_heap) # O(26)
        print(max_heap)
        q = deque([])
        min_time = 0
        while len(max_heap) > 0 or q:
            if len(max_heap) > 0:
                times = heapq.heappop(max_heap)
                times += 1
                if times != 0:
                    q.append((times, min_time + n))
            
            if q and min_time == q[0][1]:
                val, t = q.popleft()
                heapq.heappush(max_heap, val)
            min_time += 1

        return min_time
        # Time: O(m), m = len(tasks)
        # Space: O(1)



