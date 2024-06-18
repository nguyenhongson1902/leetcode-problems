# Merge k Sorted Lists
# https://leetcode.com/problems/merge-k-sorted-lists/description/
from typing import List, Optional

import heapq

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Brute force
        # def helper(pointers): # O(k)
        #     for pointer in pointers:
        #         if pointer is not None:
        #             return True
        #     return False

        # if len(lists) == 0:
        #     return None
        
        # pointers = lists
        # head = curr = ListNode(val=0, next=None)

        # while helper(pointers):
        #     tmp = [(pointer.val, pointer, idx) for idx, pointer in enumerate(pointers) if pointer is not None] # O(k)
        #     # print("tmp", [i[0] for i in tmp])
        #     min_val = float('inf')
        #     min_idx = -1
        #     for triple in tmp: # O(k)
        #         if triple[0] <= min_val:
        #             min_val = triple[0]
        #             min_pointer = triple[1]
        #             min_idx = triple[2]
            
        #     curr.next = min_pointer
        #     curr = curr.next

        #     tmp_node = pointers[min_idx].next
        #     # print(tmp_node)
        #     pointers[min_idx].next = None
        #     pointers[min_idx] = tmp_node
        #     # print("pointers[min_idx]", pointers[min_idx])
        #     # print(head.next)

        # return head.next
        # Time: O(k^2), k = len(lists)

        def helper(pointers): # O(k)
            for pointer in pointers:
                if pointer is not None:
                    return True
            return False

        if len(lists) == 0:
            return None
        
        pointers = lists
        head = curr = ListNode(val=0, next=None)

        min_heap = []
        for idx, pointer in enumerate(pointers):
            if pointer is not None:
                min_heap.append((pointer.val, idx))
        
        heapq.heapify(min_heap) # O(k)

        while min_heap: # O(Ck), C <= 500
            # print("min_heap", min_heap)
            val, min_idx = heapq.heappop(min_heap) # O(logk)

            curr.next = pointers[min_idx]
            curr = curr.next

            # print("pointers[min_idx]", pointers[min_idx])
            tmp_node = pointers[min_idx].next
            # print(tmp_node)
            pointers[min_idx].next = None
            pointers[min_idx] = tmp_node
            
            # print("tmp_node", tmp_node)
            if tmp_node is not None:
                heapq.heappush(min_heap, (tmp_node.val, min_idx))
            # print("pointers[min_idx]", pointers[min_idx])
            # print(head.next)

        return head.next
        # Time: O(klogk), k=len(lists)
        # Space: O(k)


        
