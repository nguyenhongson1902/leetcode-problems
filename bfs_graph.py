from collections import deque


matrix = [[1,2,3],[4,5,6],[7,8,9]]
'''
1 2 3
4 5 6
7 8 9
'''
# Assumption: The starting point is the top left one
# Again, my implementation is more flexible in terms of selecting the starting point for BFS
ROWS, COLS = len(matrix), len(matrix[0])
directions = ((0, -1), (0, 1), (-1, 0), (1, 0)) # left, right, up, down
visited = set()

def bfs(r, c, visited):
    if not matrix:
        return []
    
    q = deque([(r, c)])
    while q:
        curr_r, curr_c = q.popleft()
        if (curr_r, curr_c) not in visited:
            visited.add((curr_r, curr_c))
            print(matrix[curr_r][curr_c], end=' ')

            for direction in directions:
                next_r, next_c = curr_r + direction[0], curr_c + direction[1]
                if 0 <= next_r < ROWS and 0 <= next_c < COLS:
                    q.append((next_r, next_c))

bfs(0, 0, visited)
print()

# Another implementation
def bfs(matrix):
    # Check for an empty matrix/graph.
    if not matrix:
        return []

    rows, cols = len(matrix), len(matrix[0])
    visited = set()
    directions = ((0, 1), (0, -1), (1, 0), (-1, 0))

    def traverse(i, j):
        queue = deque([(i, j)])
        while queue:
            curr_i, curr_j = queue.popleft()
            if (curr_i, curr_j) not in visited:
                visited.add((curr_i, curr_j))
                print(matrix[curr_i][curr_j], end=" ")
                # Traverse neighbors.
                for direction in directions:
                    next_i, next_j = curr_i + direction[0], curr_j + direction[1]
                    if 0 <= next_i < rows and 0 <= next_j < cols:
                        # Add in question-specific checks, where relevant.
                        queue.append((next_i, next_j))

    for i in range(rows):
        for j in range(cols):
            traverse(i, j)

bfs(matrix)
