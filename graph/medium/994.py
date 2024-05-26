from typing import List
import collections

# Rotting Oranges
# https://leetcode.com/problems/rotting-oranges/description/

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # BFS in graph
        def is_valid(r, c):
            return 0 <= r < ROWS and 0 <= c < COLS

        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        q = collections.deque([])

        fresh, empty, rotten = 0, 0, 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0:
                    empty += 1
                elif grid[i][j] == 1:
                    fresh += 1
                else:
                    rotten += 1
                    visited.add((i, j))
                    q.append((i, j)) # Starting from multiple rotten oranges (sources)
        
        if fresh == 0: # If there're no fresh oranges
            return 0
        if rotten == 0: # If there're no rotten oranges
            return -1
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] # up, down, left, right
        time = -1
        while q:
            n = len(q)
            for _ in range(n):
                curr_r, curr_c = q.popleft()

                if (curr_r, curr_c) not in visited:
                    visited.add((curr_r, curr_c))

                for dr, dc in directions:
                    new_r, new_c = curr_r + dr, curr_c + dc
                    if is_valid(new_r, new_c) and grid[new_r][new_c] != 0 and (new_r, new_c) not in visited and (new_r, new_c) not in q:
                        q.append((new_r, new_c))
                        visited.add((new_r, new_c))
                        fresh -= 1 # decreases when a fresh orange becomes rotten
            time += 1
        
        if fresh != 0: # There's at least one fresh orange left which is not adjacent to any rotten oranges
            return -1
        else:
            return time

        # Time and space: O(mn)

