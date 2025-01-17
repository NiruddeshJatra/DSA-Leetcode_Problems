# Time Complexity:
# - Serialize: O(N), where N is the number of nodes in the tree
#   - We visit each node exactly once to append its value to the array
# - Deserialize: O(N), where N is the length of the input string
#   - We process each value in the string once to reconstruct the tree

# Space Complexity:
# - Serialize: O(N) for the array storing node values and the final string
# - Deserialize: O(H) where H is the height of the tree for recursion stack
#   - In worst case of unbalanced tree, this could be O(N)

# INTUITION:
# We can uniquely represent a binary tree using preorder traversal if we also 
# encode null pointers. This works because:
# 1. Preorder gives us the root first, followed by complete left and right subtrees
# 2. By marking null pointers explicitly ('None'), we know exactly where each subtree ends
# 3. When deserializing, we can recursively construct the tree by processing values
#    in the same order they were serialized

# ALGORITHM:
# Serialize:
# 1. Use DFS preorder traversal (root, left, right)
# 2. For each node:
#    - If null, append 'None' marker
#    - If not null, append value and recurse on left and right children
# 3. Join all values with spaces and return resulting string

# Deserialize:
# 1. Split input string and create iterator
# 2. Use recursive DFS:
#    - Get next value from iterator
#    - If 'None', return null
#    - Create new node with value
#    - Recursively construct left and right subtrees
#    - Return constructed node

class Codec:
   def serialize(self, root: TreeNode) -> str:
       serializedValues = []
       
       def serializeHelper(node: TreeNode) -> None:
           if not node:
               serializedValues.append('None')
               return
               
           serializedValues.append(str(node.val))
           serializeHelper(node.left)
           serializeHelper(node.right)

       serializeHelper(root)
       return ' '.join(serializedValues)

   def deserialize(self, data: str) -> TreeNode:
       nodeValues = iter(data.split())
       
       def deserializeHelper() -> TreeNode:
           currentValue = next(nodeValues)
           if currentValue == 'None':
               return None

           currentNode = TreeNode(int(currentValue))
           currentNode.left = deserializeHelper()
           currentNode.right = deserializeHelper()
           return currentNode

       return deserializeHelper()
