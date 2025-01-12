# Time Complexity:
# - O(N), where N is the number of nodes in the binary tree
# - Each node is visited exactly once during the level-order traversal

# Space Complexity:
# - O(W), where W is the maximum width of any level in the tree
# - The queue stores at most W nodes at any given level
# - Note: The indices can grow exponentially but we only store O(W) nodes

# INTUITION:
# The width of a binary tree is the maximum number of nodes at any level between
# the leftmost and rightmost nodes (including null nodes). We can:
# 1. Use level-order traversal to process nodes level by level
# 2. Assign indices to nodes (2i+1 for left child, 2i+2 for right child)
# 3. Track the leftmost and rightmost indices at each level
# The indices follow a pattern where a node at index i has children at 2i+1 and 2i+2,
# which maps perfectly to how a binary tree would be stored in an array.

# ALGORITHM:
# 1. Use BFS with a queue storing tuples of (node, index)
# 2. For each level:
#    - Store the start index (leftmost node's index)
#    - Process all nodes at current level
#    - For each node:
#      * Calculate indices for children (2*i+1, 2*i+2)
#      * Add non-null children to queue with their indices
#    - Update max width using last node's index - start index + 1
# 3. Return maximum width found

from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
   def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
       # Handle empty tree
       if not root:
           return 0
           
       # Initialize queue with root node and its index (0)
       queue = deque([(root, 0)])
       max_width = 0
       
       # Process level by level
       while queue:
           level_size = len(queue)
           level_start_index = queue[0][1]  # Leftmost node's index
           
           # Process all nodes at current level
           for _ in range(level_size):
               current_node, current_index = queue.popleft()
               
               # Add non-null children to queue with calculated indices
               if current_node.left:
                   queue.append((current_node.left, 2 * current_index + 1))
               if current_node.right:
                   queue.append((current_node.right, 2 * current_index + 2))
                   
           # Update max width using rightmost node's index
           current_width = current_index - level_start_index + 1
           max_width = max(max_width, current_width)
       
       return max_width
