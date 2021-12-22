# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Time complexity: O(n)
    def increasingBST(root: TreeNode) -> TreeNode:
        def traverse(root_node, tmp=[]):
            if root_node != None:
                tmp = traverse(root_node.left, tmp)
                tmp.append(root_node.val)
                # print(tmp)
                tmp = traverse(root_node.right, tmp)
            return tmp
        result = traverse(root)
        
        new = TreeNode(val=result[0])
        tree_index = new
        for i in range(1, len(result)):
            tree_index.right = TreeNode(val=result[i])
            tree_index = tree_index.right
        return new