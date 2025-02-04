# Time Complexity:
# - O(M*N) where M is number of nodes in root tree
#   and N is number of nodes in subRoot tree
# - Worst case: check subtree at every node
# - For each node, identical check is O(N)

# Space Complexity:
# - O(H) where H is height of main tree for recursion stack
# - Best case O(logM) for balanced tree
# - Worst case O(M) for skewed tree

# INTUITION:
# Check if subRoot is a subtree of root by:
# 1. Checking current node for exact match
# 2. If not match, recursively check left and right subtrees
# Example:
#     3          1
#    / \        / \
#   4   5      0   1
#  / \
# 1   2
# Subroot doesn't match 3, but matches subtree under 4

# ALGO:
# 1. Identical check helper function:
#    - Recursively compare tree structures
#    - Match values and structure exactly
# 2. Main method:
#    - Check if current node matches
#    - If not, check left and right subtrees
# 3. Recurse until match found or tree ends

def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
   # Helper to check if trees are identical
   def checkIdentical(node1: Optional[TreeNode], node2: Optional[TreeNode]) -> bool:
       # Base case: both null or both not null with same value
       if not node1 or not node2:
           return node1 == node2
       
       # Check current node value and recursively check left and right
       return (node1.val == node2.val and 
               checkIdentical(node1.left, node2.left) and 
               checkIdentical(node1.right, node2.right))
   
   # Base case: if either tree is null
   if not root or not subRoot:
       return root == subRoot
   
   # Check three possibilities:
   # 1. Current subtree matches
   # 2. Subtree exists in left subtree
   # 3. Subtree exists in right subtree
   return (checkIdentical(root, subRoot) or 
           self.isSubtree(root.left, subRoot) or 
           self.isSubtree(root.right, subRoot))
