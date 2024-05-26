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
directions = ((-1, 0), (1, 0), (0, -1), (0, 1)) # up, down, left, right
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
    directions = ((-1, 0), (1, 0), (0, -1), (0, 1)) # up, down, left, right

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

# When the matrix is a hash table of hash tables
def dfs(matrix, start_row, start_col):
    def is_valid(row, col):
        # Check if the cell is within the bounds of the matrix
        return row in matrix and col in matrix[row]
    
    def dfs_util(row, col, visited):
        if not is_valid(row, col) or (row, col) in visited:
            return
        
        # Mark the current cell as visited
        visited.add((row, col))
        print(matrix[row][col], end=' ')  # Process the current cell (e.g., print it)
        
        # Explore the neighbors (up, down, left, right)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            dfs_util(new_row, new_col, visited)
    
    visited = set()  # Set to keep track of visited nodes
    dfs_util(start_row, start_col, visited)

# Example usage:
matrix = {
    0: {0: 1, 1: 2, 2: 3},
    1: {0: 4, 1: 5, 2: 6},
    2: {0: 7, 1: 8, 2: 9}
}
print()
dfs(matrix, 0, 0)  # Start DFS from the top-left corner



