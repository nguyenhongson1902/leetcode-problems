# Search a 2D Matrix
# https://leetcode.com/problems/search-a-2d-matrix/description/


from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binary_search_column(arr, target):
            left, right = 0, len(arr) - 1
            while left <= right:
                mid = (left + right) // 2
                if arr[mid] == target:
                    return mid
                elif arr[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1

        def binary_search_row(arr, target):
            '''
            Make sure this function will return an integer index even if it doesn't find any value that is equal to the target
            '''
            if len(arr) == 1: # when the matrix has only 1 row
                return 0
            left, right = 0, len(arr) - 1
            while left <= right:
                mid = (left + right) // 2
                if arr[mid][0] <= target <= arr[mid][-1]:
                    return mid
                elif target < arr[mid][0]:
                    right = mid - 1
                elif target > arr[mid][-1]:
                    left = mid + 1
                
                # if left == len(arr) or right == -1: # when the left index or right index is out of bound, meaning that we don't find the row index (explicitly, we can remove this if statement)
                #     return
        
        # Binary search by row, time O(log(m))
        row_idx = binary_search_row(matrix, target)
        if row_idx is None: # If we don't find the row index that contains the target
            return False
        # print(row_idx)

        # Binary search by column, time O(log(n))
        if row_idx is not None:
            col_idx = binary_search_column(matrix[row_idx], target)
        
        # print(col_idx)
        return True if col_idx is not None else False

        # Time: O(log(m)) + O(log(n)) = O(log(m*n))
        
