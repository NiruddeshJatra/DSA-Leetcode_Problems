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
# Inorder traversal follows Left->Root->Right pattern. Recursion works well because:
# 1. Tree is inherently recursive
# 2. Each subtree needs same traversal pattern
# 3. Base case cleanly handles leaf nodes and empty subtrees
# Passing array as parameter avoids creating new arrays in recursive calls
# ALGO:
# 1. Define helper function inOrder that takes:
#    - Current node
#    - Result array reference
# 2. In inOrder function:
#    - If node is null, return (base case)
#    - Recursively process left subtree (Left)
#    - Append current node's value (Root)
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
   def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
       def inOrder(node: Optional[TreeNode], result: List[int]) -> None:
           if not node:
               return
               
           inOrder(node.left, result)  # Process left subtree
           result.append(node.val)      # Process root
           inOrder(node.right, result) # Process right subtree
       
       result = []
       inOrder(root, result)
       return result
