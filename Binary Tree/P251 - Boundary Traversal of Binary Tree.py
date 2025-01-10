# Time Complexity:
# - O(N), where N is the number of nodes in the binary tree
# - We visit each node exactly once in one of the traversal functions
# - Left boundary: O(H), Right boundary: O(H), Leaves: O(N), where H is height
# - Right boundary reversal is O(H) in worst case

# Space Complexity:
# - O(N), where N is the number of nodes in the binary tree
# - Stack space for recursive leaf traversal: O(H) in worst case
# - Result array: O(N) to store boundary traversal
# - Temporary array for right boundary: O(H)

# INTUITION:
# Boundary traversal requires visiting nodes in specific order: root -> left boundary -> leaves -> right boundary (reversed).
# Breaking this into separate traversal functions is ideal because:
# 1. Each part has different traversal rules and directions
# 2. Left and right boundaries exclude leaves
# 3. Right boundary needs to be processed in reverse order
# 4. Leaf nodes need to be processed in left-to-right order

# ALGO:
# 1. Check for empty tree and add root if not leaf
# 2. Left boundary traversal:
#    - Start from root.left
#    - Keep going left if possible, else right
#    - Add non-leaf nodes
# 3. Leaf nodes traversal (recursive):
#    - DFS to find and add all leaf nodes
#    - Process in left-to-right order
# 4. Right boundary traversal:
#    - Start from root.right
#    - Keep going right if possible, else left
#    - Store non-leaf nodes in temp array
#    - Append in reverse order
# 5. Return combined result

def traverseBoundary(root):
   result = []
   
   def isLeaf(node):
       # Check if node is a leaf (no children)
       if node.left or node.right:
           return False
       return True
   
   def traverseLeft(node):
       currentNode = node.left
       
       # Process left boundary nodes (excluding leaves)
       while currentNode:
           if not isLeaf(currentNode):
               result.append(currentNode.data)
           if currentNode.left:
               currentNode = currentNode.left
           else:
               currentNode = currentNode.right
   
   def traverseRight(node):
       currentNode = node.right
       tempStack = []
       
       # Collect right boundary nodes in reverse order
       while currentNode:
           if not isLeaf(currentNode):
               tempStack.append(currentNode.data)
           if currentNode.right:
               currentNode = currentNode.right
           else:
               currentNode = currentNode.left
               
       # Add right boundary nodes in reverse order
       while tempStack:
           result.append(tempStack.pop())
   
   def traverseLeaves(node):
       # Base case: leaf node
       if isLeaf(node):
           result.append(node.data)
           return
       
       # Recurse on left and right subtrees
       if node.left:
           traverseLeaves(node.left)
       if node.right:
           traverseLeaves(node.right)
   
   # Handle empty tree
   if not root:
       return result
       
   # Add root if it's not a leaf
   if not isLeaf(root):
       result.append(root.data)
   
   # Process each part of boundary
   traverseLeft(root)
   traverseLeaves(root)
   traverseRight(root)
   
   return result
