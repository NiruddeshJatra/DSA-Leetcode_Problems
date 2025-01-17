# Time Complexity:
# - O(N), where N is the number of nodes in the binary tree
# - Each node is processed once to find the rightmost node of its left subtree
# - In worst case, finding rightmost node takes O(N), but amortized it's O(1)

# Space Complexity:
# - O(1), only uses a constant amount of extra space
# - Achieves tree flattening in-place without using recursion stack or queue

# INTUITION:
# To flatten a binary tree into a linked list, we can:
# 1. Process each node and rearrange its left subtree into right subtree
# 2. For each node with left child:
#    - Find rightmost node in left subtree
#    - This node should point to current node's right subtree
#    - Current node's right should point to its left subtree
#    - Remove left pointer (set to null)
# 3. This preserves preorder traversal sequence while flattening

# ALGORITHM:
# 1. Start from root and traverse right using a pointer
# 2. For each node with left child:
#    - Find rightmost node in left subtree (predecessor)
#    - Make predecessor's right point to current node's right
#    - Make current node's right point to its left subtree
#    - Set current node's left to null
# 3. Move to right child and continue until no more nodes

class Solution:
   def flatten(self, root: Optional[TreeNode]) -> None:
       currentNode = root
       
       while currentNode:
           if currentNode.left:
               predecessor = currentNode.left
               while predecessor.right:
                   predecessor = predecessor.right
                   
               predecessor.right = currentNode.right
               currentNode.right = currentNode.left
               currentNode.left = None
               
           currentNode = currentNode.right
