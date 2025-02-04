# Time Complexity:
# - O(N) where N is number of nodes in tree
# - Each node visited exactly once
# - Constant time operations at each node

# Space Complexity:
# - O(H) where H is height of tree for recursion stack
# - Best case O(logN) for balanced tree
# - Worst case O(N) for skewed tree

# INTUITION:
# Calculate root-to-leaf numbers by:
# 1. Building number as we traverse down
# 2. Multiply current number by 10 and add node value
# 3. When leaf reached, return complete number
# Example:
#     1
#    / \
#   2   3
# Paths: 12, 13
# Total sum: 25

# ALGO:
# 1. Use DFS with current number as parameter
# 2. At each node:
#    - Multiply current number by 10
#    - Add current node's value
#    - If leaf node, return number
#    - If not leaf, recursively process left/right subtrees
# 3. Sum paths from left and right subtrees

def sumNumbers(self, root: Optional[TreeNode]) -> int:
   def dfs(node: TreeNode, currentNumber: int) -> int:
       if not node:
           return 0
       
       # Build current number
       currentNumber = currentNumber * 10 + node.val
       
       # If leaf node, return complete number
       if not node.left and not node.right:
           return currentNumber
       
       # Sum paths from left and right subtrees
       return dfs(node.left, currentNumber) + dfs(node.right, currentNumber)
   
   return dfs(root, 0)
