# Time Complexity:
# - O(N) to build inorder map
# - O(N) to construct tree where N is number of nodes
# - Each node processed exactly once

# Space Complexity:
# - O(N) for inorder index map
# - O(H) for recursion stack (H is height of tree)
# - O(N) worst case for skewed tree
# - O(log N) for balanced tree

# INTUITION:
# To build tree from inorder and postorder:
# 1. Last element of postorder is root
# 2. Inorder shows left/right subtrees around root
# 3. Process postorder right-to-left to get roots
# This works because:
# - Postorder visits root last after both subtrees
# - Inorder splits nodes into left and right subtrees
# - Recursively building right before left matches postorder

# ALGORITHM:
# 1. Create map of inorder values to indices for O(1) lookup
# 2. Pop from postorder to get roots (process right-to-left)
# 3. For each root:
#    - Find its position in inorder using map
#    - Recursively build right subtree (elements after root)
#    - Recursively build left subtree (elements before root)
#    - Return completed subtree

class Solution:
   def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
       # Map inorder values to indices for O(1) lookup
       inorderIndexMap = {val: i for i, val in enumerate(inorder)}
       
       def constructTree(inorderStart: int, inorderEnd: int) -> Optional[TreeNode]:
           # Base case: invalid range
           if inorderStart > inorderEnd:
               return None
               
           # Create root from last postorder element
           rootValue = postorder.pop()
           root = TreeNode(rootValue)
           
           # Find position of root in inorder
           rootIndex = inorderIndexMap[rootValue]
           
           # Build right subtree first (matches postorder)
           root.right = constructTree(rootIndex + 1, inorderEnd)
           # Build left subtree
           root.left = constructTree(inorderStart, rootIndex - 1)
           
           return root
           
       return constructTree(0, len(inorder) - 1)
