# Time Complexity:
# - O(N), where N is number of nodes in the tree
#   - We visit each node exactly once during traversal
#   - Array append operation is O(1)
# Space Complexity:
# - O(H) for recursion stack, where H is height of tree
#   - Worst case (skewed tree): H = N
#   - Best case (balanced tree): H = log N
# - O(N) for result array to store all node values
# INTUITION:
# Postorder traversal follows Left->Right->Root pattern. Recursion is natural because:
# 1. Tree is inherently recursive structure
# 2. Each subtree follows same traversal pattern
# 3. Base case handles nulls and leaf nodes cleanly
# Passing array reference avoids creating new arrays in recursive calls
# ALGO:
# 1. Define helper function postOrder that takes:
#    - Current node
#    - Result array reference
# 2. In postOrder function:
#    - If node is null, return (base case)
#    - Recursively process left subtree (Left)
#    - Recursively process right subtree (Right)
#    - Append current node's value (Root)
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
   def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
       def postOrder(node: Optional[TreeNode], result: List[int]) -> None:
           if not node:
               return
               
           postOrder(node.left, result)  # Process left subtree
           postOrder(node.right, result) # Process right subtree
           result.append(node.val)       # Process root
       
       result = []
       postOrder(root, result)
       return result
