# Time Complexity: 
# - O(N), where N is the number of nodes in the binary tree
# - Each node is visited exactly once during the level-order traversal

# Space Complexity:
# - O(W), where W is the maximum width of the tree
# - The queue stores nodes level by level

# INTUITION:
# Perform a breadth-first search (BFS) traversal to calculate 
# the average value of nodes at each level of the binary tree.

# ALGO:
# 1. If root is None, return empty list
# 2. Use a queue for level-order traversal
# 3. For each level, calculate sum and count of nodes
# 4. Compute and store average for each level
# 5. Return list of level averages

from collections import deque
from typing import Optional, List

class Solution:
   def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
       if not root:
           return []

       nodeQueue = deque([root])
       levelAverages = []

       while nodeQueue:
           levelSize = len(nodeQueue)
           levelSum = 0

           for _ in range(levelSize):
               currentNode = nodeQueue.popleft()
               levelSum += currentNode.val

               if currentNode.left:
                   nodeQueue.append(currentNode.left)
               if currentNode.right:
                   nodeQueue.append(currentNode.right)

           levelAverage = levelSum / levelSize
           levelAverages.append(levelAverage)

       return levelAverages
