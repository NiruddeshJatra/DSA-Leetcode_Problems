# Time Complexity:
# - O(N), where N is the number of nodes in the binary tree
# - We visit each node exactly once and perform O(1) operations at each node
# - The height calculation and diameter update happen in the same traversal

# Space Complexity:
# - O(H), where H is the height of the tree, used by the recursive call stack
# - In worst case (skewed tree), H = N, making it O(N)
# - We use O(1) extra space for the diameter variable

# INTUITION:
# The diameter of a binary tree is the longest path between any two nodes.
# This path doesn't need to pass through the root.
# Using DFS with a shared diameter variable is ideal because:
# 1. For each node, diameter passing through it = left height + right height
# 2. Height calculation naturally fits with DFS post-order traversal
# 3. We can update global max diameter while calculating heights
# 4. Each path length is number of edges (not nodes), hence no +1 when updating diameter

# ALGO:
# 1. Initialize global diameter variable as [0] (list for mutable reference)
# 2. Define DFS helper function that returns height of current subtree
# 3. For each node:
#    - Get heights of left and right subtrees
#    - Update max diameter if current path (left + right) is longer
#    - Return height of current subtree (1 + max(left, right))
# 4. Return the final max diameter

class Solution:
   def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
       # List to store max diameter (using list for mutable reference)
       max_diameter = [0]
       
       def calculate_height(node) -> int:
           # Base case: empty node has height 0
           if not node:
               return 0
           
           # Get heights of left and right subtrees
           left_height = calculate_height(node.left)
           right_height = calculate_height(node.right)
           
           # Update max diameter if current path is longer
           # Current path length = left_height + right_height
           current_path = left_height + right_height
           max_diameter[0] = max(max_diameter[0], current_path)
           
           # Return height of current subtree
           return 1 + max(left_height, right_height)
       
       # Calculate heights and update diameter
       calculate_height(root)
       
       # Return the maximum diameter found
       return max_diameter[0]
