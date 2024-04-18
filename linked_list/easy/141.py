from typing import Optional
# Linked List Cycle
# https://leetcode.com/problems/linked-list-cycle/description/


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Accepted but too slow
# Time: O(n^2) because the `in` operator takes linear time with a list
# Space: O(n)
# class Solution:
#     def hasCycle(self, head: Optional[ListNode]) -> bool:
#         if head == None or head.next == None:
#             return False
#         hash_map = {}
#         curr = head
#         while curr != None:
#             hash_map[curr] = hash_map.get(curr, 0) + 1
#             if 2 in hash_map.values():
#                 return True
#             curr = curr.next
#         return False
    
# Better, time: O(n), space: O(n)
# class Solution:
#     def hasCycle(self, head: Optional[ListNode]) -> bool:
#         if head == None or head.next == None:
#             return False
#         hash_map = {}
#         curr = head
#         while curr != None:
#             hash_map[curr] = hash_map.get(curr, 0) + 1
#             if hash_map[curr] == 2:
#                 return True
#             curr = curr.next
#         return False
    
# Time: O(n)
# Space: O(1)
# class Solution:
#     def hasCycle(self, head: Optional[ListNode]) -> bool:
#         slow, fast = head, head
#         while fast and fast.next:
#             slow = slow.next
#             fast = fast.next.next
#             if fast == slow:
#                 return True
#         return False

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False

        if head.next == head:
            return True

        prev, curr = head, head
        while curr and curr.next:
            curr = curr.next.next
            if prev == curr:
                return True
            prev = prev.next
        
        return False


            
    
    