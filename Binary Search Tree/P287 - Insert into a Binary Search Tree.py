# Time Complexity:
# - O(H), where H is the height of the BST
# - Best case O(logN) for balanced BST
# - Worst case O(N) for skewed BST
# - We traverse single path from root to insertion point

# Space Complexity:
# - O(H) due to recursion stack
# - Best case O(logN) for balanced BST 
# - Worst case O(N) for skewed BST
# - Only one new node is created O(1)

# INTUITION:
# In a BST, a new value should be inserted where it maintains BST properties:
# 1. All nodes in left subtree are smaller than current node
# 2. All nodes in right subtree are larger than current node
# 3. We can find insertion point by comparing with current node and recursing
# 4. When we hit null, that's where the new node belongs

# ALGORITHM:
# 1. Base case: if current node is null
#    - Create and return new node with value
# 2. If value < current node's value:
#    - Recurse on left subtree
#    - Set result as left child
# 3. If value > current node's value:
#    - Recurse on right subtree
#    - Set result as right child
# 4. Return current node

class Solution:
   def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
       if not root:
           return TreeNode(val)
           
       if val < root.val:
           root.left = self.insertIntoBST(root.left, val)
       else:
           root.right = self.insertIntoBST(root.right, val)
           
       return root
