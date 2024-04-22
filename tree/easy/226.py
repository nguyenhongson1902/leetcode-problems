from typing import Optional
# Invert Binary Tree
# https://leetcode.com/problems/invert-binary-tree/description/


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    #     def invert(curr):
    #         if not curr:
    #             return curr

    #         if not curr.left and not curr.right:
    #             return curr


    #         curr.left = invert(curr.left)
    #         curr.right = invert(curr.right)
    #         curr.left, curr.right = curr.right, curr.left
    #         return curr
            
    #     root = invert(root)   
    #     return root

# Time: O(n), n is the number of nodes in a tree
# Space: O(h) with h is the height of the tree if considering the call stack, if not O(1)

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node):
            if not node:
                return None
            
            left = dfs(node.left)
            right = dfs(node.right)
            node.left, node.right = right, left
            
            return node
        
        return dfs(root)
        # Time: O(n), n = #nodes
        # Space: O(h), h = height of tree (because of the call stack)
