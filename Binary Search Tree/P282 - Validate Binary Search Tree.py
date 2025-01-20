# Time Complexity:
# - O(N), where N is the number of nodes in the tree
# - We need to visit each node exactly once
# - Each node requires constant time comparisons

# Space Complexity:
# - O(H), where H is the height of the tree 
# - Space used by recursion stack
# - Best case O(logN) for balanced BST
# - Worst case O(N) for skewed BST

# INTUITION:
# A valid BST must satisfy these conditions at every node:
# 1. All values in left subtree must be less than node's value
# 2. All values in right subtree must be greater than node's value
# 3. Both left and right subtrees must be valid BSTs
# We can check this by passing valid ranges down the tree

# ALGORITHM:
# 1. Use helper function that tracks valid range for each node
# 2. Initially range is (-inf, inf) at root
# 3. For left child:
#    - Upper bound becomes parent's value
#    - Lower bound stays same
# 4. For right child:
#    - Lower bound becomes parent's value
#    - Upper bound stays same
# 5. Return false if any node violates its range

class Solution:
   def isValidBST(self, root: Optional[TreeNode]) -> bool:
       def validateBST(node: TreeNode, minVal: float, maxVal: float) -> bool:
           if not node:
               return True
               
           if not(minVal < node.val < maxVal):
               return False
               
           return (validateBST(node.left, minVal, node.val) and 
                  validateBST(node.right, node.val, maxVal))
       
       return validateBST(root, float('-inf'), float('inf'))
