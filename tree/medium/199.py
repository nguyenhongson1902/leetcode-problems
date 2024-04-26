from typing import List, Optional
import collections
# Binary Tree Right Side View
# https://leetcode.com/problems/binary-tree-right-side-view/description/


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        result = []
        q = collections.deque([root])
        while q:
            n = len(q)
            for i in range(n):
                node = q.popleft()
                if i == 0:
                    result.append(node.val)
                if node.right:
                    q.append(node.right)
                if node.left:
                    q.append(node.left)
        return result
        # DFS is hard to implement so let's go with BFS (level-order traversal)
        # Time: O(n), n = #nodes
        # Space: O(n), n = The maximum number of leaf nodes = 2^(height of tree)
