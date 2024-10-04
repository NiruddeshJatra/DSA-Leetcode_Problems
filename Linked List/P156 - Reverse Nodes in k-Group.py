# Time Complexity: O(n), where n is the number of nodes in the linked list.
# We traverse the entire linked list, reversing each group of k nodes in linear time.

# Space Complexity: O(1), as the algorithm only uses a constant amount of extra space 
# (for pointers and variables), not dependent on the input size.

# INTUITION:
# The problem requires reversing nodes in groups of k within a singly linked list.
# This involves identifying each group, reversing the nodes within it, and connecting the groups properly.
# We accomplish this by using a dummy node and pointers to keep track of each group’s start and end.

# ALGO:
# 1. Create a dummy node to simplify handling edge cases, and set it to point to the head of the list.
# 2. Traverse the linked list with a pointer. For each group of k nodes:
#    - Check if there are k nodes available.
#    - Reverse the k nodes in place.
#    - Reconnect the reversed group with the rest of the list.
# 3. Continue moving through the list, repeating the above steps for each k-group.
# 4. Return the list, skipping the dummy node.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Helper function to reverse k nodes in the list
        def reverse(head: Optional[ListNode]) -> (Optional[ListNode], Optional[ListNode]):
            prev = None
            cur = head
            # Step 1: Reverse k nodes in the linked list
            for _ in range(k):
                front = cur.next
                cur.next = prev
                prev = cur
                cur = front
            return prev, cur  # Return the new head and the node after the reversed group

        # Step 2: Initialize a dummy node to simplify edge cases
        dummy = ListNode(0)
        dummy.next = head
        ptr = dummy  # Pointer for connecting groups
        
        # Step 3: Traverse the linked list and reverse each group of k nodes
        while ptr:
            # Check if there are k nodes available to reverse
            tracker = ptr
            for _ in range(k):
                tracker = tracker.next
                if not tracker:  # If fewer than k nodes remain, return result
                    return dummy.next
            
            # Step 4: Reverse the current k-group and connect it to the rest of the list
            prev, cur = reverse(ptr.next)  # prev is the new head of the reversed k-group
            last_node_of_reversed_group = ptr.next
            last_node_of_reversed_group.next = cur  # Connect the end of the reversed group to the remaining nodes
            ptr.next = prev  # Connect the start of the previous part to the new head of the reversed group
            ptr = last_node_of_reversed_group  # Move the pointer to the end of the reversed group

        # Step 5: Return the modified list (skipping the dummy node)
        return dummy.next
