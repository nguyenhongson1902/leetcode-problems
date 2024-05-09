# Number of Islands
# https://leetcode.com/problems/number-of-islands/
from typing import List
import collections


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Idea: Starting points = points that have value 1
        # BFS
        visited = set()
        ROWS, COLS = len(grid), len(grid[0])
        directions = ((0, -1), (0, 1), (-1, 0), (1, 0))
        
        def bfs(r, c, visited):
            q = collections.deque([(r, c)])
            while q:
                curr_r, curr_c = q.popleft()
                if (curr_r, curr_c) not in visited:
                    visited.add((curr_r, curr_c))

                    for direction in directions:
                        next_r, next_c = curr_r + direction[0], curr_c + direction[1]
                        if 0 <= next_r < ROWS and 0 <= next_c < COLS and grid[next_r][next_c] == "1":
                            q.append((next_r, next_c))

        start = []
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    start.append((r, c))
        
        count = 0
        for r, c in start:
            if (r, c) not in visited:
                count += 1
            bfs(r, c, visited)
        return count
    
    # Time: O(mn), m = #rows, n = #cols
    # Space: O(mn)
    # When the interviewer asks to do it in DFS, just change popleft to pop