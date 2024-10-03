# Time Complexity: O(n), where n is the number of nodes in the linked list.
# We traverse the list once to rearrange nodes.

# Space Complexity: O(1), as we only use constant extra space for pointers.

# INTUITION:
# The idea is to split the linked list into two separate lists: one for nodes 
# at odd indices and one for nodes at even indices. After that, we combine the 
# odd and even lists. This allows us to keep the odd-indexed nodes followed by 
# the even-indexed nodes while maintaining their relative order.

# ALGO:
# 1. We start by keeping two pointers: one for odd-indexed nodes and one for 
#    even-indexed nodes.
# 2. Traverse the list, rearranging the pointers to build separate lists of 
#    odd and even indexed nodes.
# 3. After rearranging, append the even list to the end of the odd list.
# 4. Return the modified linked list.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        
        # Initialize odd and even pointers
        odd, even = head, head.next
        evenHead = even  # Store the head of the even list
        
        # Traverse the list
        while even and even.next:
            odd.next = odd.next.next  # Move odd pointer to the next odd node
            even.next = even.next.next  # Move even pointer to the next even node
            odd = odd.next  # Move odd pointer forward
            even = even.next  # Move even pointer forward
        
        # Append the even list to the end of the odd list
        odd.next = evenHead
        
        return head
