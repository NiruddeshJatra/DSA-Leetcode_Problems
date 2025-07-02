"""
# Time Complexity: O(n), where n is the number of nodes in the linked list.
# We traverse the list twice: once to create new nodes and once to set the next and random pointers.

# Space Complexity: O(n), because we use a hashmap to store the mapping from original nodes to their copies.

# INTUITION:
# The problem is to create a deep copy of a linked list where each node has a `next` pointer 
# and an additional `random` pointer that can point to any node in the list or be None.
# Using a hashmap, we can map each node to its corresponding new node and handle both `next` 
# and `random` pointers in a second pass.
# Why do we need a second pass? Why not do everything in one pass?
# Imagine you’re walking through the original list for the first time, and you see a node A. You create its copy A'.
# Now suppose A has a random pointer to some node B — but you haven’t reached B yet in the list, so you haven’t created a copy B'. 
# Therefore, in the first pass you can't assign A'.random = B' yet, because B' doesn’t exist.
# That’s why we need:
# - First pass: Create all the copied nodes and store them in a hashmap.
# - Second pass: Set up the next and random pointers, using the hashmap (which now has all nodes copied).
# So, the second pass is needed because the targets of random pointers might not have been processed yet during the first pass.

# ALGO:
# 1. Edge case: if the head is None, return None.
# 2. Use a hashmap to store each node's copy, created by iterating through the original list.
# 3. In a second pass through the list, update the `next` and `random` pointers of each copied node 
#    using the hashmap to retrieve references.
# 4. Return the copied head node, which is mapped in the hashmap.
"""

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # Step 1: Edge case - if head is None, return None
        if not head:
            return None

        # Step 2: Create a hashmap to store copies of each node
        hashmap = {}
        
        # Step 3: First pass - create a copy of each node and store in hashmap
        cur = head
        while cur:
            hashmap[cur] = Node(cur.val)
            cur = cur.next

        # Step 4: Second pass - set the next and random pointers for each copied node
        cur = head
        while cur:
            hashmap[cur].next = hashmap.get(cur.next)
            hashmap[cur].random = hashmap.get(cur.random)
            cur = cur.next

        # Step 5: Return the copied head node
        return hashmap[head]
