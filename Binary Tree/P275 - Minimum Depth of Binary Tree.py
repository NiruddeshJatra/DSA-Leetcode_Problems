# Time Complexity:
# - O(N), where N is the number of nodes in the binary tree
# - We need to visit each node at least once to find the minimum depth
# - For a balanced tree, we might stop early due to finding a leaf node

# Space Complexity:
# - O(H), where H is the height of the tree
# - In worst case (skewed tree), this becomes O(N)
# - Space is used by recursion stack for DFS traversal

# INTUITION:
# The minimum depth is the shortest path from root to a leaf node.
# Key insights:
# 1. For a leaf node, both children are null
# 2. If a node has only one child, we must continue on that path
# 3. If a node has both children, we can take the minimum of their depths
# This suggests a recursive solution that handles these cases differently

# ALGORITHM:
# 1. Base case: if root is null, return 0
# 2. If node has both children:
#    - Return 1 + minimum of left and right subtree depths
# 3. If node has only one child:
#    - Return 1 + depth of the existing child
#    - Use 'or' operator to select non-null child
# 4. Recursively process all nodes following these rules

class Solution:
   def minDepth(self, root: Optional[TreeNode]) -> int:
       if not root:
           return 0
           
       if root.left and root.right:
           return 1 + min(self.minDepth(root.left), 
                        self.minDepth(root.right))
       else:
           return 1 + self.minDepth(root.left or root.right)
