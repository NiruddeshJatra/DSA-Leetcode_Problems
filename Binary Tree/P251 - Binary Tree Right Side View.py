# Time Complexity:
# - O(N), where N is the number of nodes in the binary tree
# - Each node is visited exactly once during DFS traversal
# - Operations at each node are O(1)

# Space Complexity:
# - O(H) for recursion stack, where H is height of tree
# - In worst case (skewed tree), H = N making it O(N)
# - O(H) additional space for result array to store rightmost nodes

# INTUITION:
# Right side view shows nodes that would be visible when viewing tree from right side.
# Using DFS with right-before-left traversal is ideal because:
# 1. First node at each level is rightmost visible node
# 2. Processing right subtree before left ensures rightmost nodes are seen first
# 3. Level tracking helps identify first node at each level
# 4. DFS naturally handles tree structure

# ALGO:
# 1. Use DFS helper function with level tracking
# 2. For each node:
#    - If current level not in result, this is rightmost node
#    - Process right subtree first (level + 1)
#    - Then process left subtree (level + 1)
# 3. Return array of rightmost nodes

from typing import List, Optional

class Solution:
   def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
       def dfsHelper(node: Optional[TreeNode], level: int) -> None:
           if node:
               # If this is first node at current level, it's rightmost
               if len(rightView) == level:
                   rightView.append(node.val)
               
               # Process right subtree first
               dfsHelper(node.right, level + 1)
               # Then process left subtree
               dfsHelper(node.left, level + 1)
       
       rightView = []
       dfsHelper(root, 0)
       return rightView
