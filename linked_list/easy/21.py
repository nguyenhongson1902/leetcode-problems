from typing import Optional

# Merge Two Sorted lists
# https://leetcode.com/problems/merge-two-sorted-lists/description/


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2

        if not list2:
            return list1

        curr1, curr2 = list1, list2
        new_head = ListNode() # Create a dummy node
        curr = new_head
        while curr1 and curr2:
            if curr1.val <= curr2.val:
                curr.next = curr1
                curr1 = curr1.next
            else:
                curr.next = curr2
                curr2 = curr2.next
            curr = curr.next

        while curr1:
            curr.next = curr1
            curr = curr.next
            curr1 = curr1.next
        
        while curr2:
            curr.next = curr2
            curr = curr.next
            curr2 = curr2.next
        
        return new_head.next
            
            