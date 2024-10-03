# Time Complexity: O(n log n), where n is the number of nodes in the linked list. 
# Merge sort recursively splits the list into two halves, 
# and merging two sorted halves takes linear time.

# Space Complexity: O(log n) due to the recursion stack during the splitting process.

# INTUITION:
# The problem is to sort a singly linked list in O(n log n) time. 
# Merge sort is well-suited for this problem because it has a time complexity of O(n log n) 
# and can be adapted to work on linked lists without extra space.

# ALGO:
# 1. Recursively split the list into two halves using the slow and fast pointer technique.
# 2. Recursively sort each half using merge sort.
# 3. Merge the two sorted halves.
# 4. Continue this process until the base case is reached (a single node or an empty list).

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base case: if the list is empty or contains only one node, it's already sorted
        if not head or not head.next:
            return head
        
        # Step 1: Split the list into two halves using slow and fast pointers
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Step 2: Split the list into 'left' and 'right' halves
        left, right = head, slow.next
        slow.next = None
        
        # Step 3: Recursively sort both halves
        sortedLeft = self.sortList(left)
        sortedRight = self.sortList(right)
        
        # Step 4: Merge the two sorted halves
        return self.merge(sortedLeft, sortedRight)
    
    # Helper function to merge two sorted lists
    def merge(self, l: Optional[ListNode], r: Optional[ListNode]) -> Optional[ListNode]:
        # If either list is empty, return the non-empty list
        if not l or not r:
            return l or r
        
        # Initialize a dummy node to build the merged sorted list
        tempHead = temp = ListNode(0)
        
        # Merge the two lists by comparing their node values
        while l and r:
            if l.val < r.val:
                temp.next = l
                l = l.next
            else:
                temp.next = r
                r = r.next
            temp = temp.next
        
        # Attach the remaining part of either list (if any)
        temp.next = l or r
        
        # Return the merged list, which starts at tempHead.next
        return tempHead.next
