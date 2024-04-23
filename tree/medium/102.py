import collections
from typing import Optional, List
# Binary Tree Level Order Traversal
# https://leetcode.com/problems/binary-tree-level-order-traversal/


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # # print("root:", root)
        # res = []
        # q = collections.deque() # queue
        # q.append(root)
        
        # while q:
        #     level = []
        #     q_len = len(q)
        #     for _ in range(q_len):
        #         node = q.popleft()
        #         # level.append(node.val)
        #         # if node.left:
        #         #     q.append(node.left)
        #         # if node.right:
        #         #     q.append(node.right)

        #         if node:
        #             level.append(node.val)
        #             q.append(node.left)
        #             q.append(node.right)
            
        #     # res.append(level)
        #     # print(res)
        #     if level:
        #         res.append(level)
        # return res

        result = []
        q = collections.deque([root])
        while q:
            tmp = []
            n = len(q)
            for _ in range(n):
                node = q.popleft()
                if node:
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
                    tmp.append(node.val)
            if tmp:
                result.append(tmp)
        return result
                    
        # Time: O(n), n = #nodes
        # Space: O(n), n = #nodes, because in the worse case, queue q contains all leaf nodes.
