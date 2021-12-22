# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def rangeSumBST(root: TreeNode, low: int, high: int) -> int:
    def traverse(node, s=0):
        if node != None:
            s = traverse(node.left, s)
            if node.val >= low and node.val <= high:
                # print(node.val)
                s += node.val
            # print(node.val)
            s = traverse(node.right, s)
        # print(s)
        return s
    result = traverse(root)
    return result

# Solution: Using in-order traversal
            
        