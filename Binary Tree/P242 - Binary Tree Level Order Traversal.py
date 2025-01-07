# Time Complexity:
# - O(N), where N is number of nodes in the tree
#   - Each node is processed exactly once
#   - Queue operations (append/popleft) are O(1)
# Space Complexity:
# - O(W) for queue, where W is max width of tree
#   - In worst case (complete binary tree), W = N/2
#   - Queue stores at most one level at a time
# - O(N) for result list storing all node values
# INTUITION:
# BFS with queue is perfect for level-order traversal because:
# 1. Queue naturally processes nodes level by level
# 2. Size of queue at start of iteration = nodes in current level
# 3. Can track level boundaries by processing queue in chunks
# 4. Easy to handle null nodes and empty levels
# ALGO:
# 1. Initialize empty result list and queue with root
# 2. While queue not empty:
#    - Get current level size
#    - Process that many nodes from queue:
#      * Pop node from front
#      * If node exists:
#        > Add value to current level
#        > Add children to queue
#    - If level has nodes, add to result
# 3. Return result list
from typing import List, Optional
from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
   def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
       result = []
       if not root:
           return result
           
       queue = deque([root])
       
       while queue:
           levelSize = len(queue)
           currentLevel = []
           
           # Process all nodes at current level
           for _ in range(levelSize):
               node = queue.popleft()
               currentLevel.append(node.val)
               
               # Add children to queue
               if node.left:
                   queue.append(node.left)
               if node.right:
                   queue.append(node.right)
           
           result.append(currentLevel)
       
       return result
