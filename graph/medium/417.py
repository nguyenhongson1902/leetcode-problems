# Pacific Atlantic Water Flow
# https://leetcode.com/problems/pacific-atlantic-water-flow/description/

from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # Because we only visit every node once, so time complexity O(mn), m = #rows, n = #columns
        # if not heights:
        #     return []

        # ROWS, COLS = len(heights), len(heights[0])
        # directions = ((0, -1), (0, 1), (-1, 0), (1, 0))

        # def dfs(r, c, visited):
        #     if (r, c) in visited:
        #         return

        #     visited.add((r, c))

        #     for direction in directions:
        #         next_r, next_c = r + direction[0], c + direction[1]
        #         if 0 <= next_r < ROWS and 0 <= next_c < COLS and heights[r][c] <= heights[next_r][next_c]:
        #             dfs(next_r, next_c, visited)
        
        # p_visited, a_visited = set(), set()
        
        # # Get the starting points for dfs
        # p, a = [], [] # pacific starting points, atlantic starting points
        # for r in range(ROWS):
        #     p.append((r, 0))
        #     a.append((r, COLS - 1))
        
        # for c in range(COLS):
        #     p.append((0, c))
        #     a.append((ROWS - 1, c))
        
        # for r, c in p:
        #     dfs(r, c, p_visited)
        
        # for r, c in a: 
        #     dfs(r, c, a_visited)
            
        # result = []
        # for r in range(ROWS):
        #     for c in range(COLS):
        #         if (r, c) in p_visited and (r, c) in a_visited:
        #             result.append([r, c])
        # return result

        # Brute force solution: If we run dfs on every single node in the matrix, the time complexity would be O(M.N) (iterating through every node) * O(M.N) (running a dfs) = O((M.N)^2)

        # BFS solution
        ROWS, COLS = len(heights), len(heights[0])

        # Getting the starting points for pacific and atlantic oceans
        pac = collections.deque()
        pac_visited = [[False]*COLS for _ in range(ROWS)]
        for c in range(COLS):
            pac.append([0, c])
            pac_visited[0][c] = True

        for r in range(ROWS):
            pac.append([r, 0])
            pac_visited[r][0] = True

        atl = collections.deque()
        atl_visited = [[False]*COLS for _ in range(ROWS)]
        for c in range(COLS):
            atl.append([ROWS - 1, c])
            atl_visited[ROWS - 1][c] = True

        for r in range(ROWS):
            atl.append([r, COLS - 1])
            atl_visited[r][COLS - 1] = True
        
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        def bfs(q, visited):
            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    new_r, new_c = r + dr, c + dc
                    if 0 <= new_r < ROWS and 0 <= new_c < COLS and heights[new_r][new_c] >= heights[r][c] and not visited[new_r][new_c]:
                        q.append([new_r, new_c])
                        visited[new_r][new_c] = True
        
        bfs(pac, pac_visited)
        bfs(atl, atl_visited)

        result = []
        for r in range(ROWS):
            for c in range(COLS):
                if pac_visited[r][c] and atl_visited[r][c]:
                    result.append([r, c])
        
        return result


        

            



