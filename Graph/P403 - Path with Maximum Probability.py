# Time Complexity:
# - O(E + V), where E is the number of edges and V is the number of vertices (nodes).
# - In worst case, we might visit each edge multiple times if we keep finding better probabilities.
# - This is essentially a modified BFS where nodes can be revisited, so it could be O(V·E) in the worst case.

# Space Complexity:
# - O(V + E) for the graph representation and the queue.
# - The graph adjacency list stores all edges and the queue can contain up to V nodes.

# INTUITION:
# This problem asks for the maximum probability path from start_node to end_node. While typical shortest path
# algorithms like Dijkstra's find the minimum path, we need to find the maximum probability path here.
#
# The key insight is that we can adapt BFS to find the maximum probability path by revisiting nodes when 
# we find a better (higher) probability. Since probabilities are multiplicative (we multiply probabilities
# along the path), we keep track of the highest probability to reach each node.
#
# An important difference from standard Dijkstra's algorithm is that we use a simple queue instead of a priority
# queue, which works for this specific problem but may not be optimal for all graphs.

# ALGO:
# 1. Build an adjacency list representation of the graph, where each edge stores the neighbor node and its index.
# 2. Initialize a distance array to track the maximum probability to reach each node (0 for all nodes except start_node).
# 3. Set the probability of reaching the start_node to 1.0 (100% chance).
# 4. Use a queue for BFS traversal, starting from the start_node.
# 5. For each node, consider all its neighbors:
#    a. Calculate the probability of reaching the neighbor through the current node.
#    b. If this new probability is higher than any previously found probability, update it and add the neighbor to the queue.
# 6. Return the maximum probability of reaching the end_node.

class Solution:
   def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], startNode: int, endNode: int) -> float:
       # Build adjacency list representation of the graph
       graph = defaultdict(list)
       for i, (source, destination) in enumerate(edges):
           # Store both the neighbor node and the edge index for probability lookup
           graph[source].append((destination, i))
           graph[destination].append((source, i))
       
       # Array to store maximum probability to reach each node
       maxProbabilities = [0.0] * n
       maxProbabilities[startNode] = 1.0  # 100% chance to reach the start node
       
       # Queue for BFS traversal
       queue = deque([startNode])
       
       while queue:
           currentNode = queue.popleft()
           
           # Explore all neighbors of the current node
           for neighborNode, edgeIndex in graph[currentNode]:
               # Calculate new probability via the current path
               newProbability = maxProbabilities[currentNode] * succProb[edgeIndex]
               
               # If we found a better probability to reach this neighbor
               if newProbability > maxProbabilities[neighborNode]:
                   # Update the maximum probability
                   maxProbabilities[neighborNode] = newProbability
                   # Add neighbor to queue for further exploration
                   queue.append(neighborNode)
       
       # Return the maximum probability of reaching the end node
       return maxProbabilities[endNode]
