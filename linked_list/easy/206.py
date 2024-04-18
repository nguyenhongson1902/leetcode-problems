# Reverse Linked List
# https://leetcode.com/problems/reverse-linked-list/description/


from typing import Optional
import copy

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Solution 1: Iterative (out of place)
        # Time complexity: O(n)
        # Space complexity: O(n)
        # if not head:
        #     return None

        # curr = head
        # while curr:
        #     if curr == head:
        #         curr_copy = copy.copy(curr) # must not use deepcopy because it recursively copies elements
        #         new_head = curr_copy
        #         curr_copy.next = None
        #     else:
        #         curr_copy = copy.copy(curr) # must not use deepcopy because it recursively copies elements
        #         curr_copy.next = new_head
        #         new_head = curr_copy

        #     curr = curr.next
        # return new_head

        # Solution 2: Recursive
        # Time: O(n)
        # Space: O(n), call stack size
        if not head:
            return None
        
        new_head = head
        if head.next:
            new_head = self.reverseList(head.next)
            head.next.next = head
            head.next = None

        return new_head

        # Solution 3: Iterative (in place, two pointers)
        # Time: O(n)
        # Space: O(1)
        # prev, curr = None, head
        # while curr:
        #     tmp = curr.next
        #     curr.next = prev
        #     prev = curr
        #     curr = tmp
        # return prev

        

        


