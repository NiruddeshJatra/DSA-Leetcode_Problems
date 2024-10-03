# Time Complexity: O(n), where n is the number of nodes in the linked list. 
# We reverse the list twice and traverse it once to handle the addition, 
# making the total time complexity linear.

# Space Complexity: O(1), since we are only using a constant amount of extra space 
# for pointers and nodes, regardless of the size of the input.

# INTUITION:
# The problem is to add one to a number represented by a singly linked list, 
# where each node contains a digit. The least significant digit is at the end of the list.
# Since adding one requires processing from the least significant digit first, 
# we reverse the linked list to process from the beginning.

# ALGO:
# 1. Reverse the linked list to make the least significant digit the head of the list.
# 2. Traverse the reversed list and add 1 to the first digit. Handle carry-over 
#    by setting nodes with a value of 9 to 0 until no carry remains.
# 3. If the last node in the reversed list is a 9, a new node with value 1 is added.
# 4. Reverse the list again to restore the original order.
# 5. Return the modified linked list as the result.

class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

# Don't change the code above.

def addOne(head: Node) -> Node:
    # Helper function to reverse the linked list
    def reverse(head):
        prev = None
        cur = head
        while cur:
            front = cur.next  # Keep track of the next node
            cur.next = prev   # Reverse the link
            prev = cur        # Move `prev` and `cur` forward
            cur = front
        return prev

    # Step 1: Reverse the linked list
    head = reverse(head)

    # Step 2: Traverse and add 1 to the reversed list
    cur = head
    while cur.next and cur.data == 9:
        cur.data = 0  # Set nodes with 9 to 0 and move to the next node
        cur = cur.next

    # Step 3: If the last node is 9, create a new node with 1
    if cur.data == 9:
        cur.data = 0
        node = Node(1)
        cur.next = node
    else:
        cur.data += 1  # Add 1 if it's not a 9

    # Step 4: Reverse the list again to restore the original order
    return reverse(head)
