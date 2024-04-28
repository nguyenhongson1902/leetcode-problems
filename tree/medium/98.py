from typing import Optional
# Validate Binary Search Tree
# https://leetcode.com/problems/validate-binary-search-tree/description/


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, left_bound, right_bound):
            if not node:
                return True
            
            if node.val <= left_bound or node.val >= right_bound:
                return False
            
            left_valid = dfs(node.left, left_bound, node.val)
            right_valid = dfs(node.right, node.val, right_bound)
            return left_valid and right_valid

        return dfs(root, -2**31 - 1, 2**31)
        # Time: O(n), n = #nodes
        # Space: O(h), recursive calls, h = height of tree
            