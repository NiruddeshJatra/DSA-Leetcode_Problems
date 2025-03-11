# Time Complexity:
# - O(N), where N is the number of nodes in the linked list.
# - We traverse the linked list exactly once, performing constant work for each node.

# Space Complexity:
# - O(1), as we only use a constant amount of extra space regardless of the input size.
# - We create a few new nodes but don't allocate space proportional to the input size.

# INTUITION:
# The problem asks us to partition a linked list such that all nodes with values less than x come before nodes with values >= x,
# while preserving the relative order within each partition.
# 
# Instead of trying to perform complex in-place manipulations, a simpler approach is to:
# 1. Create two separate lists: one for nodes with values < x and one for nodes with values >= x
# 2. Traverse the original list once, appending each node to the appropriate list
# 3. Connect the two lists at the end
# 
# For example, if we have [1,4,3,2,5,2] with x = 3:
# - Less than x list: [1,2,2]
# - Greater than or equal to x list: [4,3,5]
# - Final result after connecting: [1,2,2,4,3,5]

# ALGO:
# 1. Create two dummy nodes as heads for our two separate lists.
# 2. Traverse the original list, appending each node to either the "less than x" list or the "greater than or equal to x" list.
# 3. Set the next pointer of the last node in the second list to None to avoid cycles.
# 4. Connect the end of the first list to the beginning of the second list.
# 5. Return the head of the merged list (excluding the dummy node).

from typing import Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # Create dummy heads for two separated lists
        lessHead = lessTail = ListNode(0)  # For nodes with values < x
        greaterHead = greaterTail = ListNode(0)  # For nodes with values >= x
        
        # Traverse the original list
        current = head
        while current:
            # Determine which list to append the current node to
            if current.val < x:
                # Append to the "less than x" list
                lessTail.next = current
                lessTail = lessTail.next
            else:
                # Append to the "greater than or equal to x" list
                greaterTail.next = current
                greaterTail = greaterTail.next
                
            # Move to the next node
            current = current.next
        
        # Terminate the "greater than or equal to x" list to avoid cycles
        greaterTail.next = None
        
        # Connect the "less than x" list with the "greater than or equal to x" list
        lessTail.next = greaterHead.next
        
        # Return the head of the merged list (excluding the dummy node)
        return lessHead.next
