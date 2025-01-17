# Time Complexity:
# - O(N), where N is the number of nodes in the binary tree
# - Each node is visited exactly once during the recursive traversal
# - Setting next pointers is O(1) per node

# Space Complexity:
# - O(H), where H is the height of the tree
# - In a perfect binary tree, H = log N
# - Space used by recursion stack for DFS traversal

# INTUITION:
# For a perfect binary tree, we need to:
# 1. Connect each node's left child to its right child
# 2. Connect each node's right child to next node's left child
# The recursive approach works because:
# - We can use the parent's next pointer to find the neighbor node
# - Once a level is connected, we can use these links for next level

# ALGORITHM:
# 1. Base case: if root is null, return null
# 2. For each node:
#    - Connect its left child to right child
#    - If node has next pointer:
#      * Connect right child to next node's left child
#    - Recursively process left and right subtrees
# 3. Return the root node

class Solution:
   def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
       if not root:
           return None
           
       leftChild = root.left
       rightChild = root.right
       nextNode = root.next
       
       if leftChild:
           leftChild.next = rightChild
           if nextNode:
               rightChild.next = nextNode.left
           self.connect(leftChild)
           self.connect(rightChild)
           
       return root
