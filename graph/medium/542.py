# 01 Matrix
# https://leetcode.com/problems/01-matrix/description/

import math
import collections
from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        # BFS because we want to find the shortest path from the nearest 0 to 1
        visited = set()
        q = collections.deque()
        ROWS, COLS = len(mat), len(mat[0])
        for r in range(ROWS):
            for c in range(COLS):
                if mat[r][c] == 1:
                    mat[r][c] = float('inf')
                else:
                    q.append((r, c, 0)) # Initialize the starting points for BFS

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] # up, down, left, right
        while q:
            # print(q)
            r, c, dist = q.popleft()
            if math.isinf(mat[r][c]):
                mat[r][c] = dist

            for dr, dc in directions:
                new_r, new_c = r + dr, c + dc
                if 0 <= new_r < ROWS and 0 <= new_c < COLS and (new_r, new_c) not in visited and math.isinf(mat[new_r][new_c]):
                    q.append((new_r, new_c, dist + 1))
                    visited.add((new_r, new_c))
        print(mat)
        return mat
        # Time: O(mn), m=#rows, n=#cols
        # Space: O(mn)
        
        
                
