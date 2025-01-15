# Time Complexity:
# - O(N) for building graph from tree where N is number of nodes
# - O(N) for BFS traversal
# - Total: O(N)

# Space Complexity:
# - O(N) for adjacency list graph representation
# - O(N) for queue in BFS
# - O(N) for visited set
# - Total: O(N)

# INTUITION:
# To find minimum time to burn tree, we need to:
# 1. Convert tree to undirected graph to enable movement in all directions
# 2. Use BFS to simulate fire spreading level by level
# This approach is optimal because:
# - BFS gives shortest paths to all nodes from start
# - Each level in BFS represents one unit of time
# - Graph allows easy traversal to parent/children

# ALGORITHM:
# Part 1 - Convert Tree to Graph:
# 1. Use DFS with parent tracking to build undirected graph
# 2. Add edges both ways for parent-child relationships
#
# Part 2 - BFS to Simulate Fire:
# 1. Start BFS from given start node
# 2. Each level of BFS represents one time unit
# 3. Track visited nodes to avoid cycles
# 4. Count levels until all nodes visited

class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
       # Build adjacency list representation
       adjList = defaultdict(list)
       stack = [(root, None)]  # (node, parent) pairs
       
       # Convert tree to undirected graph
       while stack:
           currentNode, parentNode = stack.pop()
           
           # Add bidirectional edge with parent
           if parentNode:
               adjList[parentNode.val].append(currentNode.val)
               adjList[currentNode.val].append(parentNode.val)
               
           # Add children to stack
           if currentNode.left:
               stack.append((currentNode.left, currentNode))
           if currentNode.right:
               stack.append((currentNode.right, currentNode))
       
       # BFS to simulate fire spread
       queue = deque([start])
       visitedNodes = {start}
       timeElapsed = -1  # Start at -1 to account for initial state
       
       # Process each level (representing one time unit)
       while queue:
           levelSize = len(queue)
           
           # Process all nodes at current level
           for _ in range(levelSize):
               currentNode = queue.popleft()
               
               # Spread fire to unburnt neighbors
               for neighbor in adjList[currentNode]:
                   if neighbor not in visitedNodes:
                       queue.append(neighbor)
                       visitedNodes.add(neighbor)
           
           timeElapsed += 1
           
       return timeElapsed
