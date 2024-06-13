from typing import List
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/
# Two Sum II - Input Array Is Sorted

# The first time
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        s = 0
        begin, end = 0, len(numbers) - 1
        result = [begin, end]

        while begin < end:
            s = numbers[begin] + numbers[end]
            if s == target:
                result[0] = begin
                result[1] = end
                break
            elif s < target:
                begin += 1
            else:
                end -= 1
        
        result[0] += 1
        result[1] += 1

        return result

# The second time
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left + 1, right + 1]
            elif numbers[left] + numbers[right] < target:
                left += 1
            else:
                right -= 1
        # Time complexity: O(n), n = len(numbers)
        # Space complexity: O(1)
        
        