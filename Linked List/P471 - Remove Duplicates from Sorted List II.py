# Time Complexity:
# - O(N), where N is the number of nodes in the linked list.
# - We traverse each node at most twice: once in the main loop and once in the inner while loop for duplicates.

# Space Complexity:
# - O(1), we only use a constant amount of extra space for pointers (dummy, previousNode, currentNode).

# INTUITION:
# We need to remove ALL nodes that have duplicates, not just the extra copies. This means if we have
# 1->2->2->3, we remove both 2's completely, resulting in 1->3.
# 
# The key insight is to use a dummy node before the head to handle cases where the first nodes are duplicates.
# We maintain a "previousNode" pointer that points to the last node we're sure to keep, and use "currentNode"
# to scan ahead. When we find duplicates, we skip all nodes with that value and connect previousNode
# directly to the next distinct node.
# 
# Example: 1->2->2->3->4->4->5
# - Keep 1, find duplicates 2->2, skip both, connect 1->3
# - Keep 3, find duplicates 4->4, skip both, connect 3->5
# - Result: 1->3->5

# ALGO:
# 1. Create a dummy node pointing to head to handle edge cases
# 2. Initialize previousNode to dummy and currentNode to head
# 3. While currentNode and currentNode.next exist:
#    - If currentNode.val == currentNode.next.val (duplicates found):
#      a. Store the duplicate value
#      b. Skip all nodes with this duplicate value
#      c. Connect previousNode directly to the next distinct node
#    - Else (no duplicates):
#      a. Move previousNode forward to currentNode
#      b. Move currentNode forward
# 4. Return dummy.next as the new head

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import Optional

class Solution:
   def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
       # Dummy node to handle edge cases (e.g., head itself has duplicates)
       dummyNode = ListNode()
       dummyNode.next = head
       previousNode = dummyNode
       currentNode = head

       while currentNode and currentNode.next:
           if currentNode.val == currentNode.next.val:
               # Found duplicates - skip all nodes with this value
               duplicateValue = currentNode.val
               while currentNode and currentNode.val == duplicateValue:
                   currentNode = currentNode.next
               
               # Connect previous node to the next distinct node
               previousNode.next = currentNode
           else:
               # No duplicates found - move previous pointer forward
               previousNode = currentNode
               currentNode = currentNode.next

       return dummyNode.next
