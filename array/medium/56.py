from typing import List
# Merge Intervals
# https://leetcode.com/problems/merge-intervals/description/


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sorted_intervals = sorted(intervals, key=lambda x: x[0]) # O(nlog(n))
        result = [sorted_intervals[0]] # Space: O(n)
        for i in range(1, len(sorted_intervals)): # O(n)
            if sorted_intervals[i][1] <= result[-1][1]:
                continue

            if sorted_intervals[i][0] <= result[-1][1]:
                result[-1] = [result[-1][0], sorted_intervals[i][1]]
            else:
                result.append(sorted_intervals[i])
        return result

# Time: O(nlog(n))
# Space: O(n)
            