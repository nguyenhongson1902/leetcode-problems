from typing import Optional
# Remove Nth Node from End of List
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return None

        # Two pointers technique
        right = head
        dummy = ListNode(next=head) # Use a dummy node
        left = dummy
        for _ in range(n):
            right = right.next
        
        while right:
            left = left.next
            right = right.next
        
        left.next = left.next.next

        return dummy.next
        # One pass
        # Time: O(n)
        # Space: O(1)
