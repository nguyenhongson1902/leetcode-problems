# Explaination: https://www.code-recipe.com/post/container-with-most-water
# Container With Most Water
# https://leetcode.com/problems/container-with-most-water/description/
from typing import List


# My first implementation
def max_area(height):
    left = 0
    right = len(height) - 1
    tmp = [(right-left) * min(height[left], height[right])]
    while left < right:
        if height[left] <= height[right]:
            left += 1
        else:
            right -= 1
        tmp.append((right-left) * min(height[left], height[right]))
    
    return max(tmp)

if __name__ == '__main__':
    test_1 = [1,8,6,2,5,4,8,3,7]
    print('Expected output:', 49)
    print('Output:', max_area(test_1))


# The second time
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = 0
        while left < right:
            curr_area = min(height[left], height[right]) * (right - left)
            max_area = max(max_area, curr_area)
            
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return max_area
        # Time: O(n), n = len(height)
        # Space: O(1)

