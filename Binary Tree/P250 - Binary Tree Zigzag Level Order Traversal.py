# Time Complexity:
# - O(N), where N is the number of nodes in the binary tree
# - Each node is processed exactly once and added/removed from queue once
# - Reversing level arrays takes O(L) where L is level size, but total is still O(N)

# Space Complexity:
# - O(W), where W is the maximum width of the tree
# - Queue will hold at most all nodes at the widest level
# - In worst case (perfect binary tree), W = N/2 making it O(N)

# INTUITION:
# Zigzag level order is a variation of level order traversal where alternate levels
# are processed in reverse order. Using BFS with a level toggle is ideal because:
# 1. BFS naturally processes tree level by level
# 2. Queue allows us to track level boundaries
# 3. We can collect nodes normally and reverse alternate levels
# 4. Level size gives us clear separation between levels

# ALGO:
# 1. Initialize result list and check for empty tree
# 2. Use queue for BFS, starting with root
# 3. For each level:
#    - Get current level size from queue
#    - Process that many nodes:
#      * Add node value to current level list
#      * Add children to queue for next level
#    - Reverse current level list if even level
#    - Toggle level parity
# 4. Return result list of all levels

from collections import deque
from typing import List, Optional

class Solution:
   def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
       # Return empty list for empty tree
       result = []
       if not root:
           return result
           
       # Initialize queue with root node
       node_queue = deque([root])
       is_even_level = False
       
       while node_queue:
           level_size = len(node_queue)
           level_values = []
           
           # Process all nodes at current level
           for _ in range(level_size):
               current_node = node_queue.popleft()
               level_values.append(current_node.val)
               
               # Add children to queue for next level
               if current_node.left:
                   node_queue.append(current_node.left)
               if current_node.right:
                   node_queue.append(current_node.right)
           
           # Append level values (reversed if even level)
           if is_even_level:
               result.append(level_values[::-1])
           else:
               result.append(level_values)
           
           # Toggle level parity for next level
           is_even_level = not is_even_level
       
       return result
