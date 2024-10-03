# Time Complexity: O(n), where n is the number of nodes in the linked list.
# We traverse the list twice: once to move the `fast` pointer n steps ahead,
# and another to find the node to remove.

# Space Complexity: O(1), as we are using a constant amount of extra space.

# INTUITION:
# To remove the Nth node from the end of a singly linked list, we use the 
# two-pointer technique. We maintain two pointers, `slow` and `fast`. First, 
# move the `fast` pointer n steps ahead. Then, move both `slow` and `fast` 
# pointers at the same pace until `fast` reaches the end. At this point, 
# the `slow` pointer will be at the node before the Nth node from the end. 
# We then adjust the `next` pointer to remove the desired node.

# ALGO:
# 1. Move the `fast` pointer n steps ahead.
# 2. If `fast` becomes `None`, it means we need to remove the head node.
# 3. If not, move both `slow` and `fast` until `fast` reaches the last node.
# 4. Update the `next` pointer of the `slow` node to skip the Nth node from the end.
# 5. Return the modified linked list.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:  # If there is only one node, removing it leaves the list empty
            return None
        
        slow = fast = head
        
        # Move `fast` pointer n steps ahead
        for _ in range(n):
            fast = fast.next
        
        # If `fast` is None, we are removing the head node
        if not fast:
            return head.next
        
        # Move both `slow` and `fast` until `fast` reaches the end
        while fast.next:
            slow = slow.next
            fast = fast.next
        
        # Remove the Nth node from the end
        slow.next = slow.next.next
        
        return head
