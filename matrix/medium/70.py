from typing import List
# Set Matrix Zeros
# https://leetcode.com/problems/set-matrix-zeroes/description/


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # First row to indicate which column to be zeroed out
        # First column to indicate which row to be zeroed out
        # O(1) space
        ROWS, COLS = len(matrix), len(matrix[0])

        zero_first_row = False
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        zero_first_row = True

        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0

        # Zero out the first column
        # Zeroing the first column or the first row first does matter
        if matrix[0][0] == 0:
            for r in range(ROWS):
                matrix[r][0] = 0

        # Zero out the first row (if necessary)
        if zero_first_row:
            for c in range(COLS):
                matrix[0][c] = 0