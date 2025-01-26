# Time Complexity: 
# - O(min(N1, N2)), where N1 and N2 are number of nodes in each tree
# - Each node is visited once during recursive merge

# Space Complexity:
# - O(min(H1, H2)), where H1 and H2 are heights of trees
# - Recursive call stack uses space proportional to the smaller tree's height

# INTUITION:
# Recursively merge two binary trees by adding corresponding node values 
# and constructing a new tree with merged nodes

# ALGO:
# 1. Handle base cases: return the other tree if one is None
# 2. Create new node with sum of current nodes' values
# 3. Recursively merge left and right subtrees
# 4. Return merged tree

class Solution:
   def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
       if not root1:
           return root2
       if not root2:
           return root1

       mergedNode = TreeNode(root1.val + root2.val)
       mergedNode.left = self.mergeTrees(root1.left, root2.left)
       mergedNode.right = self.mergeTrees(root1.right, root2.right)

       return mergedNode
