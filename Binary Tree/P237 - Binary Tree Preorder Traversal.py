# Time Complexity:
# - O(N), where N is number of nodes in the tree
#   - We visit each node exactly once during traversal
#   - Array append operation is O(1)
# Space Complexity:
# - O(H) for recursion stack, where H is height of tree
#   - In worst case (skewed tree), H = N
#   - In balanced tree, H = log N
# - O(N) for result array to store all node values
# INTUITION:
# Preorder traversal follows Root->Left->Right pattern. Using recursion is intuitive because:
# 1. Tree itself is a recursive data structure
# 2. Each subtree follows same traversal pattern
# 3. Base case (null node) naturally handles leaf nodes
# Using array parameter avoids creating new arrays at each recursion step
# ALGO:
# 1. Define helper function preOrder that takes:
#    - Current node
#    - Array to store results
# 2. In preOrder function:
#    - If node is null, return (base case)
#    - Append current node's value (Root)
#    - Recursively process left subtree (Left)
#    - Recursively process right subtree (Right)
# 3. In main function:
#    - Initialize empty result array
#    - Call helper function with root and array
#    - Return result array
from typing import List, Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
   def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
       def preOrder(node: Optional[TreeNode], result: List[int]) -> None:
           if not node:
               return
               
           result.append(node.val)      # Process root
           preOrder(node.left, result)  # Process left subtree
           preOrder(node.right, result) # Process right subtree
       
       result = []
       preOrder(root, result)
       return result
