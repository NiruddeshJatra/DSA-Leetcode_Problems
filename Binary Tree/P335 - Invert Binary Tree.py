# Time Complexity:
# - O(N) where N is number of nodes in tree
# - Each node is visited exactly once
# - Swapping operation at each node is O(1)

# Space Complexity:
# - O(H) where H is height of tree for recursion stack
# - Best case O(logN) for balanced tree
# - Worst case O(N) for skewed tree

# INTUITION:
# Invert binary tree by recursively:
# 1. Inverting left subtree
# 2. Inverting right subtree 
# 3. Swapping left and right children
# Example:
#     4                  4
#   /   \     ->      /   \  
#  2     7          7     2
# / \   / \        / \   / \
#1   3 6   9      9   6 3   1

# ALGO:
# 1. Base case: empty tree returns null
# 2. Recursively invert:
#    - Left subtree
#    - Right subtree  
# 3. Swap left and right children
# 4. Return root

def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
   # Base case: empty tree
   if not root:
       return root
       
   # Recursively invert subtrees
   self.invertTree(root.left)
   self.invertTree(root.right)
   
   # Swap left and right children
   root.left, root.right = root.right, root.left
   
   return root
