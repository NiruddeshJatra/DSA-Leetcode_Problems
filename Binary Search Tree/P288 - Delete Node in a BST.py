# Time Complexity:
# - O(H), where H is the height of the BST
# - Best case O(logN) for balanced BST
# - Worst case O(N) for skewed BST
# - Need to traverse to target node and potentially find successor

# Space Complexity:
# - O(H) due to recursion stack
# - Best case O(logN) for balanced BST
# - Worst case O(N) for skewed BST
# - No extra space besides recursion stack

# INTUITION:
# Deleting a node from BST has three cases:
# 1. Leaf node: Simply remove it
# 2. Node with one child: Replace with that child
# 3. Node with two children:
#    - Find successor (smallest in right subtree)
#    - Copy successor's value to current node
#    - Delete successor from right subtree
# This maintains BST properties after deletion

# ALGORITHM:
# 1. Search for node to delete:
#    - Recurse left if key < current value
#    - Recurse right if key > current value
# 2. When node found, handle three cases:
#    - If no left child: return right child
#    - If no right child: return left child
#    - If both children:
#      * Find successor (leftmost in right subtree)
#      * Copy successor value to current node
#      * Delete successor from right subtree
# 3. Return root of modified tree

class Solution:
   def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
       if not root:
           return None
           
       if key < root.val:
           root.left = self.deleteNode(root.left, key)
       elif key > root.val:
           root.right = self.deleteNode(root.right, key)
       else:
           if not root.left:
               return root.right
           elif not root.right:
               return root.left
               
           # Node has two children
           successorNode = root.right
           while successorNode.left:
               successorNode = successorNode.left
               
           root.val = successorNode.val
           root.right = self.deleteNode(root.right, successorNode.val)
           
       return root
