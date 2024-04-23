from typing import Optional
# Same Tree
# https://leetcode.com/problems/same-tree/description/


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # def dfs(node1, node2):
        #     if not node1 and not node2:
        #         return True
            
        #     if not node1 and node2:
        #         return False
            
        #     if node1 and not node2:
        #         return False
            
        #     if node1.val != node2.val:
        #         return False
            
        #     left = dfs(node1.left, node2.left)
        #     right = dfs(node1.right, node2.right)
        #     return left and right
        # return dfs(p, q)

        # Time: O(n), n = #nodes
        # Space: O(h), h = tree height
        def dfs(p, q):
            if not p and not q:
                return True
            if not p and q:
                return False
            if p and not q:
                return False
            if p.val != q.val:
                return False
            
            check_left = dfs(p.left, q.left)
            check_right = dfs(p.right, q.right)

            return check_left and check_right
        return dfs(p, q)