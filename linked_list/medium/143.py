from typing import Optional
# Reorder List
# https://leetcode.com/problems/reorder-list/description/


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # If there is only one node in the list
        if not head.next:
            return head

        # Use fast, slow pointers to find the second half of the list
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second_head = slow.next
        slow.next = None # end of the first half points to null
        # print(second_head)
        # print(head)

        # Reverse the second half of the list
        prev, curr = None, second_head
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        # print(prev)

        curr_first, curr_second = head, prev # prev is the head of the reversed second half
        while curr_first and curr_second:
            tmp_second = curr_second.next
            curr_second.next = curr_first.next
            curr_first.next = curr_second
            curr_first = curr_first.next.next
            curr_second = tmp_second