# Time Complexity:
# - O(N) where N is number of nodes in the binary tree
# - We perform one complete inorder traversal of the tree

# Space Complexity:
# - O(H) where H is height of tree for recursion stack
# - In balanced BST: O(log N)
# - In skewed BST: O(N) worst case
# - Only 3 extra pointers (first, prev, second) used otherwise

# INTUITION:
# In a valid BST, inorder traversal gives nodes in strictly increasing order.
# When two nodes are swapped, this order is violated at two positions:
# 1. First violation: bigger value where smaller should be
# 2. Second violation: smaller value where bigger should be
# By tracking these violations during inorder traversal, we can identify and fix the swapped nodes.

# ALGO:
# 1. Perform inorder traversal with tracking:
#    - prev: previously visited node
#    - first: first node violating BST property
#    - second: last node violating BST property
# 2. During traversal:
#    - If prev.val >= current.val (violation found):
#      - If first violation (first=None): mark prev as first
#      - If second violation: mark current as second
#    - Update prev to current node
# 3. After traversal:
#    - Swap values of first and second nodes

class Solution:
   def recoverTree(self, root: Optional[TreeNode]) -> None:
       def inorderTraversal(currentNode: TreeNode) -> None:
           nonlocal firstNode, previousNode, secondNode
           
           if not currentNode:
               return
               
           # Process left subtree
           inorderTraversal(currentNode.left)
           
           # Process current node
           # Check for BST violation
           if not firstNode and previousNode.val >= currentNode.val:
               firstNode = previousNode
           if firstNode and previousNode.val >= currentNode.val:
               secondNode = currentNode
               
           previousNode = currentNode
           
           # Process right subtree
           inorderTraversal(currentNode.right)
       
       # Initialize pointers
       firstNode = None            # First node violating BST property
       previousNode = TreeNode(float('-inf'))  # Previous node in inorder traversal
       secondNode = None           # Second node violating BST property
       
       # Find the swapped nodes
       inorderTraversal(root)
       
       # Swap values to fix the BST
       firstNode.val, secondNode.val = secondNode.val, firstNode.val
