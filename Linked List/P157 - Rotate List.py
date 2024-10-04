# Time Complexity: O(n), where n is the number of nodes in the linked list.
# We traverse the entire linked list twice—first to calculate the length and then to find the rotation point.

# Space Complexity: O(1), as we only use a constant amount of extra space (pointers and variables),
# independent of the input size.

# INTUITION:
# The problem is to rotate a linked list to the right by k positions.
# This involves moving the last k nodes to the front of the list. To do this, we need to find the rotation
# point and reconnect the end to the head.

# ALGO:
# 1. Find the length of the linked list.
# 2. Determine the effective rotation by taking k % length, as rotating by the list length results in the same list.
# 3. If k % length == 0, return the head as no rotation is needed.
# 4. Traverse the list to find the node just before the new head, where the list will be rotated.
# 5. Reconnect the end of the list to the head, set the new head, and break the connection to form the rotated list.
# 6. Return the rotated list.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Step 1: Edge cases: return the head if there's only one node, no rotation, or k is 0
        if not head or not head.next or not k:
            return head
            
        # Step 2: Calculate the length of the list
        length = 0
        cur = head
        while cur:
            length += 1
            cur = cur.next

        # Step 3: Optimize k by taking k % length to avoid unnecessary rotations
        k %= length
        if k == 0:
            return head

        # Step 4: Find the node just before the new head after rotation
        cur = head
        cnt = 1
        temp = head
        while cur.next:
            if cnt == length - k:
                temp = cur
            cur = cur.next
            cnt += 1

        # Step 5: Rotate the list by reconnecting the end to the head and setting the new head
        cur.next = head  # Connect the end of the list to the head
        head = temp.next  # Set the new head
        temp.next = None  # Break the connection to finalize the rotation
        
        # Step 6: Return the rotated list
        return head
