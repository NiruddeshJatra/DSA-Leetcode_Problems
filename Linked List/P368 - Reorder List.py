# Time Complexity:
# - O(N) where N is the number of nodes in the linked list
# - We traverse the list 3 times: once to find middle, once to reverse second half, once to merge

# Space Complexity:
# - O(1) as we only use a few pointers and modify the list in-place
# - No extra data structures are used

# INTUITION:
# To reorder L0→L1→...→Ln-1→Ln into L0→Ln→L1→Ln-1→L2→Ln-2→..., we need to:
# 1. Find the middle of the list (using fast/slow pointers)
# 2. Reverse the second half
# 3. Merge first and reversed second half
# Example: 1->2->3->4 becomes:
# - Split into 1->2 and 3->4
# - Reverse second half: 1->2 and 4->3
# - Merge alternately: 1->4->2->3

# ALGO:
# 1. Find middle using slow/fast pointers:
#    - Fast moves twice as fast as slow
#    - When fast reaches end, slow is at middle
# 2. Reverse second half of list:
#    - Keep track of prev node
#    - For each node, change next pointer to prev
# 3. Merge two halves:
#    - Take one node from each half alternately
#    - Connect them together

from typing import Optional

class Solution:
   def reorderList(self, head: Optional[ListNode]) -> None:
       if not head or not head.next:
           return
       
       # Step 1: Find middle of list using slow/fast pointers
       slowPointer = fastPointer = head
       while fastPointer and fastPointer.next:
           slowPointer = slowPointer.next
           fastPointer = fastPointer.next.next
           
       # Step 2: Reverse second half of list
       previousNode = None
       currentNode = slowPointer.next
       while currentNode:
           nextNode = currentNode.next
           currentNode.next = previousNode
           previousNode = currentNode
           currentNode = nextNode
       slowPointer.next = None
       
       # Step 3: Merge first half with reversed second half
       firstHalf = head
       secondHalf = previousNode
       while secondHalf:
           # Save next nodes
           firstHalfNext = firstHalf.next
           secondHalfNext = secondHalf.next
           
           # Connect nodes from both halves
           firstHalf.next = secondHalf
           secondHalf.next = firstHalfNext
           
           # Move to next pair of nodes
           firstHalf = firstHalfNext
           secondHalf = secondHalfNext
