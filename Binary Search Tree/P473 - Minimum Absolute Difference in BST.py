# Time Complexity:
# - O(N), where N is the number of nodes in the BST.
# - We visit each node exactly once during the inorder traversal.

# Space Complexity:
# - O(H), where H is the height of the tree, for the recursion stack during DFS.
# - In the worst case (skewed tree), H = N, so space complexity is O(N).
# - In the best case (balanced tree), H = log(N), so space complexity is O(log N).

# INTUITION:
# In a Binary Search Tree, the minimum absolute difference between any two nodes will always be
# between two consecutive nodes in the inorder traversal. This is because inorder traversal of
# a BST visits nodes in sorted order.
# 
# For example, if we have BST with values [1, 3, 6, 8], the inorder traversal gives us the
# sorted sequence. The minimum difference must be between adjacent elements: min(3-1, 6-3, 8-6) = 2.
# 
# We use inorder traversal and keep track of the previous node's value. At each node, we calculate
# the difference with the previous node and update our minimum. Since we're traversing in sorted order,
# we only need to check adjacent nodes rather than all possible pairs.

# ALGO:
# 1. Initialize minDifference to infinity and previousValue to None
# 2. Perform inorder DFS traversal (left -> root -> right):
#    a. Recursively traverse left subtree
#    b. Process current node:
#       - If previousValue exists, calculate difference with current node
#       - Update minDifference if current difference is smaller
#       - Update previousValue to current node's value
#    c. Recursively traverse right subtree
# 3. Return the minimum difference found

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Optional

class Solution:
   def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
       self.minDifference = float('inf')
       self.previousValue = None

       def inorderTraversal(node):
           if node:
               # Traverse left subtree first
               inorderTraversal(node.left)
               
               # Process current node
               if self.previousValue is not None:
                   currentDifference = node.val - self.previousValue
                   self.minDifference = min(self.minDifference, currentDifference)
               
               self.previousValue = node.val
               
               # Traverse right subtree
               inorderTraversal(node.right)

       inorderTraversal(root)
       return self.minDifference
