# Pacific Atlantic Water Flow
# https://leetcode.com/problems/pacific-atlantic-water-flow/description/

from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # Because we only visit every node once, so time complexity O(mn), m = #rows, n = #columns
        if not heights:
            return []

        ROWS, COLS = len(heights), len(heights[0])
        directions = ((0, -1), (0, 1), (-1, 0), (1, 0))

        def dfs(r, c, visited):
            if (r, c) in visited:
                return

            visited.add((r, c))

            for direction in directions:
                next_r, next_c = r + direction[0], c + direction[1]
                if 0 <= next_r < ROWS and 0 <= next_c < COLS and heights[r][c] <= heights[next_r][next_c]:
                    dfs(next_r, next_c, visited)
        
        p_visited, a_visited = set(), set()
        
        # Get the starting points for dfs
        p, a = [], [] # pacific starting points, atlantic starting points
        for r in range(ROWS):
            p.append((r, 0))
            a.append((r, COLS - 1))
        
        for c in range(COLS):
            p.append((0, c))
            a.append((ROWS - 1, c))
        
        for r, c in p:
            dfs(r, c, p_visited)
        
        for r, c in a: 
            dfs(r, c, a_visited)
            
        result = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in p_visited and (r, c) in a_visited:
                    result.append([r, c])
        return result

        # Brute force solution: For every node, we visit the neighbor nodes to see if they are satisfied with the condition. By doing that, we visit the same node twice, so time complexity O(m^2n^2), m = #rows, n = #columns
            

