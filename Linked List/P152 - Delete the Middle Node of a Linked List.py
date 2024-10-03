# Time Complexity: O(n), where n is the number of nodes in the linked list. 
# We traverse the list once with the fast and slow pointers.

# Space Complexity: O(1), as we only use a constant amount of extra space 
# for the two pointers (`slow` and `fast`).

# INTUITION:
# The problem asks to delete the middle node of a singly linked list. 
# To achieve this in one pass, we use the two-pointer technique: 
# a `slow` pointer that moves one step at a time and a `fast` pointer 
# that moves two steps at a time. When the `fast` pointer reaches the end, 
# the `slow` pointer will be at the middle node. We then skip the middle node.

# ALGO:
# 1. Initialize `slow` and `fast` pointers.
# 2. Move the `fast` pointer two steps at a time and the `slow` pointer 
#    one step at a time.
# 3. When the `fast` pointer reaches the end, `slow` will be at the middle node.
# 4. Skip the middle node by updating the `next` pointer of the `slow` node.
# 5. If the list has only one node, return `None` because there is no middle node.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # If there's only one node, return None (no middle node)
        if not head.next:
            return None
        
        # Initialize slow and fast pointers
        slow, fast = head, head.next
        
        # Move the fast pointer two steps and slow pointer one step at a time
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        # Skip the middle node
        slow.next = slow.next.next
        
        return head
