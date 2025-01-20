# Time Complexity:
# - O(H), where H is the height of the BST
# - Best case O(logN) for balanced BST
# - Worst case O(N) for skewed BST
# - Each iteration moves down one level of the tree

# Space Complexity:
# - O(1), only using constant extra space
# - Iterative approach avoids recursion stack space
# - Only storing current node pointer

# INTUITION:
# Binary Search Tree has the property that for any node:
# 1. Left subtree contains only values less than node
# 2. Right subtree contains only values greater than node
# This allows us to eliminate half the search space each step
# by comparing target value with current node

# ALGORITHM:
# 1. Start from root node
# 2. While current node exists:
#    - If target < current value, go left
#    - If target > current value, go right
#    - If target = current value, return node
# 3. If we exit loop, value not found, return null

class Solution:
   def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
       currentNode = root
       
       while currentNode:
           if val < currentNode.val:
               currentNode = currentNode.left
           elif val > currentNode.val:
               currentNode = currentNode.right
           else:
               return currentNode
               
       return None
