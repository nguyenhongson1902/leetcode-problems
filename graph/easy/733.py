# Flood Fill
# https://leetcode.com/problems/flood-fill/description/

from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        ROWS, COLS = len(image), len(image[0])
        visited = set()
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] # up, down, left, right
        starting_color = image[sr][sc]
        def dfs(visited, r, c):
            if (r, c) in visited:
                return
            
            visited.add((r, c))
            image[r][c] = color
            for dr, dc in directions:
                new_r, new_c = r + dr, c + dc
                if 0 <= new_r < ROWS and 0 <= new_c < COLS and image[new_r][new_c] == starting_color:
                    dfs(visited, new_r, new_c)
        
        dfs(visited, sr, sc)
        return image
        # Time: O(mn), m=#rows, n=#cols
        # Space: O(mn)
            
            