# Time Complexity:
# - O(N), where N is the number of nodes in the binary tree
# - Each node is visited exactly once in the recursive traversal
# - Operations at each node are O(1)

# Space Complexity:
# - O(H) for recursion stack, where H is height of tree
# - In worst case (skewed tree), H = N making it O(N)
# - No additional space needed beyond recursion stack

# INTUITION:
# A binary tree is symmetric if left and right subtrees mirror each other.
# Using recursive comparison is ideal because:
# 1. Need to compare opposite pairs of nodes (left vs right)
# 2. Values must match and structure must mirror
# 3. Can check both structure and values simultaneously
# 4. Clean recursive structure matching tree's nature

# ALGO:
# 1. Define helper function to compare two subtrees
# 2. Base cases:
#    - Both nodes null: return True (empty subtrees match)
#    - One node null or values differ: return False
# 3. Recursive case:
#    - Compare outer pairs (left.left vs right.right)
#    - Compare inner pairs (left.right vs right.left)
#    - Both pairs must match for symmetry

class Solution:
   def isSymmetric(self, root: Optional[TreeNode]) -> bool:
       def compareNodes(leftNode: Optional[TreeNode], 
                       rightNode: Optional[TreeNode]) -> bool:
           # Base case: both nodes are null
           if not leftNode and not rightNode:
               return True
           
           # Base case: one node null or values differ
           if not leftNode or not rightNode or leftNode.val != rightNode.val:
               return False
           
           # Recursive case: compare opposite pairs
           return (compareNodes(leftNode.left, rightNode.right) and  # outer pair
                   compareNodes(leftNode.right, rightNode.left))     # inner pair
       
       # Handle empty tree case
       if not root:
           return True
           
       # Compare left and right subtrees
       return compareNodes(root.left, root.right)
