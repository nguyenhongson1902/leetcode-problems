from typing import List
# Non-overlapping Intervals
# https://leetcode.com/problems/non-overlapping-intervals/description/


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        sorted_intervals = sorted(intervals, key=lambda x: x[0])
        last_interval = sorted_intervals[0]
        count = 0
        for start, end in sorted_intervals[1:]:
            last_start, last_end = last_interval
            if start < last_end:
                count += 1
                if end <= last_end:
                    last_interval = [start, end]
            else:
                last_interval = [start, end]
        return count

# Time: O(nlog(n))