# Time Complexity:
# - O(N), where N is the number of nodes in the binary tree.
# - We visit each node exactly once during the DFS traversal.

# Space Complexity:
# - O(H), where H is the height of the tree, for the recursion stack.
# - In the worst case (skewed tree), H = N, so space complexity is O(N).
# - In the best case (balanced tree), H = log(N), so space complexity is O(log N).

# INTUITION:
# We need to find all root-to-leaf paths and interpret each path as a number, then sum all these numbers.
# For example, if we have paths 1->2->5 and 1->3, they represent numbers 125 and 13, so sum = 125 + 13 = 138.
# 
# The key insight is to use DFS and build the number incrementally as we traverse down each path.
# At each node, we update the current number by multiplying it by 10 and adding the current node's value.
# When we reach a leaf node, we return the complete number formed by that path.
# For internal nodes, we recursively get sums from left and right subtrees and add them together.
# 
# Example: Tree with root=1, left=2, right=3, where 2 has children 4,5
# - Path 1->2->4 forms number 124
# - Path 1->2->5 forms number 125  
# - Path 1->3 forms number 13
# - Total sum = 124 + 125 + 13 = 262

# ALGO:
# 1. Define a DFS function that takes current node and current number formed so far
# 2. Base case: if node is null, return 0 (no contribution to sum)
# 3. Update current number: currentNumber = currentNumber * 10 + node.val
# 4. If current node is a leaf (no left and right children):
#    - Return the current number (complete path number)
# 5. If current node is internal:
#    - Recursively get sum from left subtree
#    - Recursively get sum from right subtree  
#    - Return sum of both subtrees
# 6. Start DFS from root with initial number 0

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Optional

class Solution:
   def sumNumbers(self, root: Optional[TreeNode]) -> int:
       def dfsPathSum(node, currentPathNumber):
           if not node:
               return 0

           # Build the number by appending current digit
           currentPathNumber = currentPathNumber * 10 + node.val
           
           # If leaf node, return the complete path number
           if not node.left and not node.right:
               return currentPathNumber

           # For internal nodes, sum contributions from both subtrees
           leftSubtreeSum = dfsPathSum(node.left, currentPathNumber)
           rightSubtreeSum = dfsPathSum(node.right, currentPathNumber)
           
           return leftSubtreeSum + rightSubtreeSum

       return dfsPathSum(root, 0)
