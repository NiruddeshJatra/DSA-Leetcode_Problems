# Time Complexity: O(n), where n is the number of nodes in the linked list. 
# We traverse the list twice: once to find the midpoint and reverse the second half, 
# and another to compare the two halves.

# Space Complexity: O(1), since we only use a constant amount of extra space for pointers.

# ALGO:
# 1. Use two pointers, slow and fast, to find the midpoint of the list.
# 2. Reverse the second half of the list starting from the midpoint.
# 3. Compare the first half of the list with the reversed second half.
# 4. If all corresponding nodes match, the list is a palindrome.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Step 1: Use two pointers to find the midpoint (slow will point to the middle)
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Step 2: Reverse the second half of the list
        prev = None
        while slow:
            next_node = slow.next
            slow.next = prev
            prev = slow
            slow = next_node
        
        # Step 3: Compare the first half and the reversed second half
        first_half = head
        second_half = prev  # This is the head of the reversed second half
        while second_half:
            if first_half.val != second_half.val:
                return False
            first_half = first_half.next
            second_half = second_half.next
        
        return True
