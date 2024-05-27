# Clone Graph
# https://leetcode.com/problems/clone-graph/description/


from typing import Optional

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # If the graph is empty
        if not node:
            return node
        # If the node's neighbors are empty
        if not node.neighbors:
            return Node(val=node.val, neighbors=[])

        # Using DFS is more intuitive
        old_to_new = {} # map old node to new node
        def dfs(node):
            # If the node is already in the map, then return the new node in the map
            if node in old_to_new:
                return old_to_new[node]
            
            # Start creating a copy node
            new = Node(val=node.val, neighbors=[])
            old_to_new[node] = new

            # Using recursion to connect edges
            for neighbor in node.neighbors:
                old_to_new[node].neighbors.append(dfs(neighbor))
            
            return new
        
        return dfs(node)
        # Time: O(V + 2E) or O(V+E)
        # Space: O(V+2E) or O(V+E)