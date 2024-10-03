# Time Complexity: O(max(m, n)), where m and n are the lengths of the two linked lists.
# We traverse both linked lists once to compute the sum, making the time complexity linear.

# Space Complexity: O(max(m, n)), where m and n are the lengths of the two linked lists. 
# This is because the resulting linked list can be as long as the longer of the two lists, 
# plus one extra node if there is a carry at the end.

# INTUITION:
# The problem is to add two numbers represented by two linked lists, where each node contains a single digit. 
# The digits are stored in reverse order, and we need to return the sum as a linked list.
# We traverse the lists node by node, add the corresponding digits, and handle carry-over.

# ALGO:
# 1. Initialize a dummy head node to simplify handling edge cases. 
# 2. Traverse both linked lists, adding corresponding digits along with any carry from the previous addition.
# 3. If the sum of two digits is 10 or more, store the excess (sum - 10) in the current node and set the carry to 1.
# 4. If one list is longer than the other, continue processing the remaining nodes.
# 5. If there’s a carry after processing all the nodes, add a new node for the carry.
# 6. Return the result, skipping the dummy head node.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()  # Dummy node to serve as the head of the result list
        cur = head         # Pointer to the current node in the result list
        carry = 0          # Variable to keep track of the carry
        
        # Step 1: Traverse both linked lists while both l1 and l2 are not None
        while l1 and l2:
            sum = l1.val + l2.val + carry
            if sum >= 10:
                node = ListNode(sum - 10)  # Create new node with value (sum - 10)
                carry = 1  # Set carry to 1
            else:
                node = ListNode(sum)  # Create new node with value sum
                carry = 0  # Reset carry
            cur.next = node  # Link the current node to the result list
            l1 = l1.next     # Move to the next node in l1
            l2 = l2.next     # Move to the next node in l2
            cur = cur.next   # Move the current pointer in the result list
        
        # Step 2: Handle remaining nodes in l1, if any
        while l1 and carry:
            sum = l1.val + carry
            if sum >= 10:
                node = ListNode(sum - 10)
                carry = 1
            else:
                node = ListNode(sum)
                carry = 0
            cur.next = node
            l1 = l1.next
            cur = cur.next
        
        # Step 3: Attach any remaining part of l1 (if no carry remains)
        if l1:
            cur.next = l1

        # Step 4: Handle remaining nodes in l2, if any
        while l2 and carry:
            sum = l2.val + carry
            if sum >= 10:
                node = ListNode(sum - 10)
                carry = 1
            else:
                node = ListNode(sum)
                carry = 0
            cur.next = node
            l2 = l2.next
            cur = cur.next

        # Step 5: Attach any remaining part of l2 (if no carry remains)
        if l2:
            cur.next = l2

        # Step 6: Handle the final carry (if any)
        if carry:
            node = ListNode(1)
            cur.next = node

        # Step 7: Return the result list (skipping the dummy head node)
        return head.next
