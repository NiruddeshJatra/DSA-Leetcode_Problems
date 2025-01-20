# Time Complexity:
# - O(H), where H is the height of the BST
# - Best case O(logN) for balanced BST
# - Worst case O(N) for skewed BST
# - We traverse down at most one path from root to target

# Space Complexity:
# - O(1), using only constant extra space
# - Iterative approach avoids recursion stack
# - Only storing current node pointer

# INTUITION:
# In a BST, the LCA of two nodes must be:
# 1. The first node that lies between p and q values
# 2. Or equal to either p or q if one is ancestor of other
# We can find this by:
# - Going left if both nodes are smaller than current
# - Going right if both are larger than current
# - Otherwise current node is the LCA

# ALGORITHM:
# 1. Start from root node
# 2. While current node exists:
#    - If both p,q smaller than current: go left
#    - If both p,q larger than current: go right
#    - Otherwise current node is LCA
# 3. Return current node as LCA

class Solution:
   def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', 
                           q: 'TreeNode') -> 'TreeNode':
       currentNode = root
       
       while currentNode:
           if currentNode.val > p.val and currentNode.val > q.val:
               currentNode = currentNode.left
           elif currentNode.val < p.val and currentNode.val < q.val:
               currentNode = currentNode.right
           else:
               return currentNode
