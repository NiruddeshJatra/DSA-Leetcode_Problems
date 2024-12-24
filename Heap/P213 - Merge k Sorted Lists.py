# Time Complexity:
# - O(N log K), where N is the total number of nodes in all linked lists, and K is the number of linked lists.
#   - Each node is pushed and popped from the heap exactly once, and each heap operation takes O(log K).

# Space Complexity:
# - O(K), for the heap that stores one node from each of the K linked lists at any time.

# INTUITION:
# The goal is to merge K sorted linked lists into a single sorted linked list. By using a min-heap, we can efficiently track 
# the smallest node among the heads of all the linked lists. This allows us to build the resulting merged list in a sorted order.

# ALGO:
# 1. Initialize an empty min-heap.
# 2. Add the head of each linked list (along with its value and index to differentiate nodes with the same value) to the heap.
# 3. Extract the smallest node from the heap, append it to the result list, and push its next node (if it exists) into the heap.
# 4. Repeat the process until the heap is empty.
# 5. Return the merged sorted list.

import heapq
from typing import List, Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []

        # Add the first node of each list to the heap
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))

        # Dummy node to form the resulting list
        ans = ListNode()
        cur = ans

        # Process nodes from the heap
        while heap:
            value, i, node = heapq.heappop(heap)
            cur.next = node
            cur = cur.next
            node = node.next
            if node:
                heapq.heappush(heap, (node.val, i, node))

        return ans.next
