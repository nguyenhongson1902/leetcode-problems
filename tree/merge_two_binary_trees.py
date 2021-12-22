# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def mergeTrees(root1: TreeNode, root2: TreeNode) -> TreeNode:
        # A recursive approach
        # Time complexity: O(n), n is the number of elements of 2 trees
        def merge(r1, r2):
            # the base case
            if r1 == None and r2 == None:
                return None
            elif r1 != None and r2 == None:
                return r1
            elif r1 == None and r2 != None:
                return r2

            new = TreeNode(r1.val + r2.val)
            new.left = merge(r1.left, r2.left)
            new.right = merge(r1.right, r2.right)
        
            return new
        
        return merge(root1, root2)
        