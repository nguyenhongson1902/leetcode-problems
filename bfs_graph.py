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
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] # up, down, left, right
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
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] # up, down, left, right

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

# When the graph/matrix is represented as a hash table of hash tables
from collections import deque

def bfs(matrix, start_row, start_col):
    def is_valid(row, col):
        # Check if the cell is within the bounds of the matrix
        return row in matrix and col in matrix[row]

    # Initialize the queue with the starting node
    queue = deque([(start_row, start_col)])
    visited = set([(start_row, start_col)])  # Set to keep track of visited nodes

    while queue:
        row, col = queue.popleft()
        print(matrix[row][col], end=' ')  # Process the current cell (e.g., print it)

        # Explore the neighbors (up, down, left, right)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if is_valid(new_row, new_col) and (new_row, new_col) not in visited:
                queue.append((new_row, new_col))
                visited.add((new_row, new_col))

# Example usage:
matrix = {
    0: {0: 1, 1: 2, 2: 3},
    1: {0: 4, 1: 5, 2: 6},
    2: {0: 7, 1: 8, 2: 9}
}
print()
bfs(matrix, 0, 0)  # Start BFS from the top-left corner

