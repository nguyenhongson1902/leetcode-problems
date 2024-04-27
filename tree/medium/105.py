from typing import Optional, List
# Construct Binary Tree from Preorder and Inorder Traversal
# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # First intuition: The first node of preorder always tells us it is the root node
        # Second intuition: The node(s) on the left of the element with root value lie in the left subtree
        # Third intuition: The node(s) on the right of the element with root value lie i the right subtree
        # Using recursive solution

        if not preorder or not inorder:
            return None

        root = TreeNode(val=preorder[0])
        mid = inorder.index(root.val)
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])

        return root
        # Time: O(n), n = len(preorder)
        # Space: O(n), n = len(preorder)
