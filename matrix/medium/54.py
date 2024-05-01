from typing import List
# Sprial Matrix
# https://leetcode.com/problems/spiral-matrix/


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # First row, last column, last row, first column
        # Move inwards by 1
        result = []
        # Using 4 pointers, top, left, right, bottom
        top, bottom, left, right = 0, len(matrix), 0, len(matrix[0])
        while top < bottom and left < right:
            if left >= right:
                break
            i = left
            while i < right:
                result.append(matrix[top][i])
                i += 1
            i -= 1
            top += 1

            if top >= bottom:
                break
            j = top
            while j < bottom:
                result.append(matrix[j][i])
                j += 1
            j -= 1
            right -= 1

            if right - 1 < left:
                break
            k = right - 1
            while k >= left:
                result.append(matrix[j][k])
                k -= 1
            k += 1
            bottom -= 1

            if bottom - 1 < top:
                break
            l = bottom - 1
            while l >= top:
                result.append(matrix[l][k])
                l -= 1
            l += 1
            left += 1
        return result
    # Time: O(mn)
    # Space: O(1) if we don't count result list
