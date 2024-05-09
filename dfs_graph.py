matrix = [[1,2,3],[4,5,6],[7,8,9]]
'''
1 2 3
4 5 6
7 8 9
'''
# Assumption: The starting point is the top left one
# My implementation, more flexible in terms of choosing which is the starting point
ROWS, COLS = len(matrix), len(matrix[0])
result = []
visited = set() # only visit a node once
directions = ((0, -1), (0, 1), (-1, 0), (1, 0)) # left, right, up, down
def dfs(r, c, visited):
    if (r, c) in visited:
        return
    
    visited.add((r, c))
    print(matrix[r][c], end=" ")
    for direction in directions:
        next_r, next_c = r + direction[0], c + direction[1]
        if 0 <= next_r < ROWS and 0 <= next_c < COLS:
            dfs(next_r, next_c, visited)

dfs(0, 0, visited)

print()

# Another implementation
def dfs(matrix):
    # Check for an empty matrix/graph.
    if not matrix:
        return []

    rows, cols = len(matrix), len(matrix[0])
    visited = set()
    directions = ((0, 1), (0, -1), (1, 0), (-1, 0))

    def traverse(i, j):
        if (i, j) in visited:
            return

        visited.add((i, j))
        print(matrix[i][j], end=" ")
        # Traverse neighbors.
        for direction in directions:
            next_i, next_j = i + direction[0], j + direction[1]
            if 0 <= next_i < rows and 0 <= next_j < cols:
            # Add in question-specific checks, where relevant.
                traverse(next_i, next_j)

    for i in range(rows):
        for j in range(cols):
            traverse(i, j)

dfs(matrix)



