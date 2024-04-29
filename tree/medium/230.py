from typing import Optional
# Kth Smallest Element in a BST
# https://leetcode.com/problems/kth-smallest-element-in-a-bst/


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # inorder traversal prints the values in an increasing order
        # Solution 1: Recursive solution
        # result = []
        # def dfs(node):
        #     if not node:
        #         return None
            
        #     dfs(node.left)
        #     result.append(node.val)
        #     dfs(node.right)

        # dfs(root)
        # return result[k-1]
        # Time: O(n), n = #nodes
        # Space: O(n), n = #nodes

        # Solution 2: Iterative solution
        n = 0 # when n == k, return
        curr = root
        stack = []
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            
            curr = stack.pop()
            n += 1
            if n == k:
                return curr.val
            curr = curr.right