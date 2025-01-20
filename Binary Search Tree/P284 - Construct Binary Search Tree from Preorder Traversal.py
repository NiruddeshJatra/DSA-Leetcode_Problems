# Time Complexity:
# - O(N), where N is the length of preorder array
# - Each node is pushed and popped at most once
# - Each value is processed exactly once

# Space Complexity:
# - O(H), where H is the height of the tree
# - Stack stores nodes along rightmost path
# - Worst case O(N) for skewed tree
# - Best case O(logN) for balanced tree

# INTUITION:
# In preorder traversal of BST:
# 1. First element is always root
# 2. Next smaller elements form left subtree
# 3. Next larger elements form right subtree
# We can use a stack to:
# - Track potential parent nodes
# - Pop nodes when we find a larger value
# - Append new nodes in correct position

# ALGORITHM:
# 1. Create root from first value
# 2. For each remaining value:
#    - If smaller than stack top:
#      * Make it left child of stack top
#      * Push to stack
#    - If larger:
#      * Pop stack until finding first smaller value
#      * Make new node right child of last popped
#      * Push new node to stack

class Solution:
   def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
       if not preorder:
           return None
           
       rootNode = TreeNode(preorder[0])
       nodeStack = [rootNode]
       
       for value in preorder[1:]:
           if value < nodeStack[-1].val:
               nodeStack[-1].left = TreeNode(value)
               nodeStack.append(nodeStack[-1].left)
           else:
               lastNode = None
               while nodeStack and nodeStack[-1].val < value:
                   lastNode = nodeStack.pop()
               lastNode.right = TreeNode(value)
               nodeStack.append(lastNode.right)
               
       return rootNode
