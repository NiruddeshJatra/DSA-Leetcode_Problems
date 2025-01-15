# Time Complexity:
# - O(N) for first BFS to build parent mapping
# - O(N) for second BFS to find nodes at distance k
# - Total: O(N) where N is number of nodes

# Space Complexity:
# - O(N) for parent mapping
# - O(N) for queue in BFS
# - O(N) for visited set
# - O(N) for result array in worst case
# - Total: O(N)

# INTUITION:
# To find nodes at distance k from target:
# 1. Need to traverse up (to parent) and down (to children)
# 2. First build parent pointers using BFS
# 3. Then use second BFS from target node to find nodes at distance k
# This approach is optimal because:
# - BFS naturally gives nodes at each distance level
# - Parent mapping enables upward traversal
# - Visited set prevents cycles

# ALGORITHM:
# Part 1 - Build Parent Mapping:
# 1. Use BFS to traverse entire tree
# 2. For each node, store its parent in hashmap
#
# Part 2 - Find Nodes at Distance K:
# 1. Start BFS from target node
# 2. At each node, consider three directions:
#    - Left child
#    - Right child
#    - Parent
# 3. Use distance counter to track levels
# 4. Collect nodes when distance = k

class Solution:
   def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
       def buildParentMap(root):
           """Build mapping of each node to its parent using BFS"""
           if not root:
               return
               
           queue = deque([root])
           
           while queue:
               levelSize = len(queue)
               
               for _ in range(levelSize):
                   currentNode = queue.popleft()
                   
                   # Process left child
                   if currentNode.left:
                       queue.append(currentNode.left)
                       parentMap[currentNode.left] = currentNode
                       
                   # Process right child
                   if currentNode.right:
                       queue.append(currentNode.right)
                       parentMap[currentNode.right] = currentNode
       
       # Initialize data structures
       parentMap = {}  # Maps node -> parent
       buildParentMap(root)
       
       # Find nodes at distance k using BFS
       result = []
       queue = deque([target])
       visitedNodes = {target}  # Track visited nodes to avoid cycles
       currentDistance = k
       
       # BFS until we reach distance k
       while queue and currentDistance > 0:
           levelSize = len(queue)
           
           for _ in range(levelSize):
               currentNode = queue.popleft()
               
               # Consider all three possible directions
               
               # 1. Left child
               if currentNode.left and currentNode.left not in visitedNodes:
                   queue.append(currentNode.left)
                   visitedNodes.add(currentNode.left)
               
               # 2. Right child
               if currentNode.right and currentNode.right not in visitedNodes:
                   queue.append(currentNode.right)
                   visitedNodes.add(currentNode.right)
               
               # 3. Parent
               if currentNode in parentMap and parentMap[currentNode] not in visitedNodes:
                   queue.append(parentMap[currentNode])
                   visitedNodes.add(parentMap[currentNode])
           
           currentDistance -= 1
       
       # Collect all nodes at distance k
       while queue:
           result.append(queue.pop().val)
           
       return result
