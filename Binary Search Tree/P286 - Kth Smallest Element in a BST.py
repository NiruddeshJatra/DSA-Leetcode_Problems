# Time Complexity:
# - O(H + k), where H is height of tree and k is target position
# - For balanced BST: O(logN + k)
# - For skewed BST: O(N)
# - We need to reach kth node in inorder traversal

# Space Complexity: 
# - O(H) for recursion stack where H is height of tree
# - Best case O(logN) for balanced BST
# - Worst case O(N) for skewed BST
# - Two class variables use O(1) extra space

# INTUITION:
# In a BST, inorder traversal gives nodes in sorted order:
# 1. Traverse left subtree first to get smaller values
# 2. Process current node and increment count
# 3. When count equals k, we've found kth smallest
# 4. No need to continue traversal after finding kth element

# ALGORITHM:
# 1. Use class variables to track:
#    - count of nodes visited
#    - result value when kth node found
# 2. DFS helper function for inorder traversal:
#    - Base case: if null node or already found k
#    - Recurse on left subtree
#    - Process current node (increment count)
#    - If count = k, store result
#    - Recurse on right subtree
# 3. Return stored result

class Solution:
   def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
       def inorderTraversal(node: TreeNode) -> None:
           if not node or self.nodesVisited >= k:
               return
           
           inorderTraversal(node.left)
           
           self.nodesVisited += 1
           if self.nodesVisited == k:
               self.kthValue = node.val
               return
               
           inorderTraversal(node.right)
       
       self.nodesVisited = 0
       self.kthValue = 0
       inorderTraversal(root)
       return self.kthValue
