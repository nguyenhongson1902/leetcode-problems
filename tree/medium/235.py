# Lowest Common Ancestor of a Binary Search Tree
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Solution 1:
        # Time: O(h) = O(logn), only visit 1 node in one of the two splits
        # Space: O(1)
        # curr = root
        # while curr:
        #     if curr.val > p.val and curr.val > q.val:
        #         curr = curr.left
        #     elif curr.val < p.val and curr.val < q.val:
        #         curr = curr.right
        #     else:
        #         return curr
        
        # Solution 2: Depth-first search
        # Time: O(n), n = #nodes
        # Space: O(h), h = height of tree
        def dfs(node, p, q):
            if not node:
                return None
            
            if node.val == p.val or node.val == q.val:
                return node

            left = dfs(node.left, p, q)
            right = dfs(node.right, p, q)
            if left and right:
                return node
            if not left and right:
                return right
            if left and not right:
                return left
            
        return dfs(root, p, q)