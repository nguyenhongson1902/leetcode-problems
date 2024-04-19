from typing import Optional
# Maximum Depth of Binary Tree
# https://leetcode.com/problems/maximum-depth-of-binary-tree/description/


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Time: O(n)
# Space: O(h), worst case: O(n)
# Recursion
# class Solution:
#     def maxDepth(self, root: Optional[TreeNode]) -> int:
#         def traversal(root):
#             if not root:
#                 return 0
        
#             return 1 + max(traversal(root.left), traversal(root.right))
        
#         return traversal(root)
  
# Iterative BFS
# class Solution:
#     def maxDepth(self, root: Optional[TreeNode]) -> int:
#         if not root:
#             return 0
        
#         level = 0
#         q = deque([root])
#         while q:
#             for i in range(len(q)):
#                 node = q.popleft()
                
#                 if node.left:
#                     q.append(node.left)
                
#                 if node.right:
#                     q.append(node.right)
            
#             level += 1
        
#         return level

# Iterative DFS
# class Solution:
#     def maxDepth(self, root: Optional[TreeNode]) -> int:
#         if not root:
#             return 0
        
#         stack = [[root, 1]]
#         res = 1
#         while stack:
#             node, depth = stack.pop()
            
#             if node:
#                 res = max(res, depth)
#                 stack.append([node.left, depth + 1])
#                 stack.append([node.right, depth + 1])
            
        
#         return res

# April 19, 2024
import collections

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Solution 1: Recursive
        # Time: O(n), n = #nodes in tree
        # Space: O(h), h = height of tree, Worse case: O(n)
        # def dfs(node):
        #     if not node:
        #         return 0
        #     return 1 + max(dfs(node.left), dfs(node.right))

        # return dfs(root)

        # Solution 2: Iterative, level-order traversal
        # Using an additional queue
        # Time: O(n), popping every element once
        # Space: O(h), append nodes in each level
        # if not root:
        #     return 0
        # level = 0
        # q = collections.deque()
        # q.append(root)
        # while q:
        #     n = len(q)
        #     for _ in range(n):
        #         node = q.popleft()
        #         if node.left:
        #             q.append(node.left)
        #         if node.right:
        #             q.append(node.right)
        #     level += 1
        # return level

        # Solution 3: Pre-order DFS iteratively
        # Using an additional stack
        # Time: O(n), popping every node once
        # Space: O(h), append nodes in each level
        if not root:
            return 0
        
        stack = [[root, 1]]
        result = 1
        while stack:
            node, depth = stack.pop()
            result = max(result, depth)
            
            # To prevent from adding null
            if node.right:
                stack.append([node.right, depth + 1])
            if node.left:
                stack.append([node.left, depth + 1])
        return result


            
        
                
        
            
            