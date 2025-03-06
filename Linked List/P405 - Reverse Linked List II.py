# Time Complexity:
# - O(n), where n is the length of the linked list.
# - We traverse at most n nodes (specifically, we traverse up to the 'right' position in the list).

# Space Complexity:
# - O(1), as we only use a constant amount of extra space regardless of input size.
# - We only create a few pointers to keep track of nodes during the reversal.

# INTUITION:
# To reverse a portion of a linked list, we need to:
# 1. Locate the sublist by finding its start and end positions.
# 2. Reverse the connections within that sublist.
# 3. Reconnect the reversed sublist back to the original list.
#
# The key insight is to keep track of the node just before the reversal starts and
# the first node of the sublist (which will become the last after reversal). This allows
# us to properly reconnect everything after performing the reversal.
#
# For example, with list 1->2->3->4->5 and left=2, right=4:
# - We need to find node 1 (before reversal starts)
# - Reverse 2->3->4 to become 4->3->2
# - Reconnect to get 1->4->3->2->5

# ALGO:
# 1. Create a dummy node pointing to the head to handle the case where we need to reverse from the first node.
# 2. Move a 'pre' pointer to the node just before the reversal starts (left-1 position).
# 3. Set 'cur' to the first node to be reversed (left position).
# 4. Reverse the sublist from left to right using the standard reversal technique:
#    a. Save the next node.
#    b. Redirect current's next pointer to the previous node.
#    c. Move previous and current pointers forward.
# 5. Reconnect the reversed sublist to the original list:
#    a. The node that was originally at 'left' is now at the end of the reversed portion.
#    b. The node that was originally at 'right' is now at the beginning of the reversed portion.
# 6. Return the head of the modified list (dummy.next).

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
   def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
       # Edge case: if left equals right, no reversal needed
       if left == right:
           return head
       
       # Create a dummy node to handle edge case where left = 1
       dummyNode = ListNode(0)
       dummyNode.next = head
       
       # Find the node just before the reversal starts
       beforeReversalNode = dummyNode
       for i in range(left - 1):
           beforeReversalNode = beforeReversalNode.next
       
       # The first node to be reversed (will be the last after reversal)
       firstReversedNode = beforeReversalNode.next
       
       # Perform the reversal
       currentNode = firstReversedNode
       previousNode = None
       
       # Reverse 'right-left+1' nodes
       for i in range(right - left + 1):
           # Save next node before changing pointers
           nextNode = currentNode.next
           
           # Reverse the pointer
           currentNode.next = previousNode
           
           # Move pointers forward
           previousNode = currentNode
           currentNode = nextNode
       
       # Reconnect the reversed portion
       # previousNode now points to the last node that was reversed (originally at 'right' position)
       # currentNode now points to the node after the reversed portion
       
       # Connect the node before reversal to the new front
       beforeReversalNode.next = previousNode
       
       # Connect the original front (now the end of reversed portion) to the rest of the list
       firstReversedNode.next = currentNode
       
       return dummyNode.next
