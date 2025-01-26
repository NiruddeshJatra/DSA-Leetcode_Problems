# Time Complexity: 
# - O(N), where N is the number of nodes in the binary tree
# - Each node is visited exactly once during the level-order traversal

# Space Complexity:
# - O(W), where W is the maximum width of the tree
# - The queue and result list store nodes level by level

# INTUITION:
# Perform a breadth-first search (BFS) traversal of the binary tree, 
# collecting node values level by level. Use a deque to efficiently 
# add levels to the front of the result list.

# ALGO:
# 1. If root is None, return empty list
# 2. Use a queue for BFS traversal
# 3. For each level, collect node values 
# 4. Add each level to the front of the result list
# 5. Return the result as a list of lists

from collections import deque
from typing import Optional, List

class Solution:
   def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
       if not root:
           return []

       nodeQueue = deque([root])
       levelResults = deque()

       while nodeQueue:
           currentLevelNodes = []
           levelSize = len(nodeQueue)

           for _ in range(levelSize):
               currentNode = nodeQueue.popleft()
               currentLevelNodes.append(currentNode.val)

               if currentNode.left:
                   nodeQueue.append(currentNode.left)
               if currentNode.right:
                   nodeQueue.append(currentNode.right)

           levelResults.appendleft(currentLevelNodes)

       return list(levelResults)
