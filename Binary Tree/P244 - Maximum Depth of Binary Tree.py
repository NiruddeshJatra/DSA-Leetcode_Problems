# Time Complexity:
# - O(N), where N is the number of nodes in the binary tree
# - We visit each node exactly once during the recursive traversal

# Space Complexity: 
# - O(H), where H is the height of the tree
# - In the worst case (skewed tree), H = N, making it O(N)
# - The space is used by the recursive call stack

# INTUITION:
# The maximum depth of a binary tree is the longest path from root to leaf.
# Recursion is ideal for this problem because:
# 1. Trees are recursive structures by nature
# 2. The max depth of a tree = 1 + max(depth of left subtree, depth of right subtree)
# 3. Base case is an empty tree (null node) which has depth 0

# ALGO:
# 1. Base case: if root is null, return 0 (empty tree has depth 0)
# 2. Recursively calculate:
#    - Left subtree depth = maxDepth(root.left)
#    - Right subtree depth = maxDepth(root.right)
# 3. Return 1 (current level) + max(left depth, right depth)

class TreeNode:
   def __init__(self, val=0, left=None, right=None):
       self.val = val
       self.left = left
       self.right = right

class Solution:
   def maxDepth(self, root: Optional[TreeNode]) -> int:
       # Base case: empty tree has depth 0
       if not root:
           return 0
       
       # Recursively calculate depth of left and right subtrees
       left_depth = self.maxDepth(root.left)
       right_depth = self.maxDepth(root.right)
       
       # Return current level (1) + maximum of left and right depths
       return 1 + max(left_depth, right_depth)
