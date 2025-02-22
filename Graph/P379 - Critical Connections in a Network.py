# Time Complexity:
# - O(V + E) where V is number of vertices and E is number of edges
# - Each vertex is visited once and each edge is traversed once during DFS

# Space Complexity:
# - O(V + E) for adjacency list representation of graph
# - O(V) for recursion stack in worst case
# - O(V) for lows array to track lowest discovery times

# INTUITION:
# A critical connection (bridge) is an edge that, when removed, would disconnect the graph.
# We can find these using DFS by tracking:
# 1. Discovery time: When we first visit a node
# 2. Lowest reachable time: Lowest discovery time we can reach from a node
#
# Example:
# Graph: 0 -- 1 -- 2
#        |     |
#        3 --- 4
#
# During DFS:
# - If we can reach a node through multiple paths (like 0->1->4->3 and 0->3), 
#   that means removing any single edge won't disconnect it
# - Edge (1,2) has no alternate path, so it's critical

# ALGO:
# 1. Build undirected graph using adjacency list
# 2. DFS traversal keeping track of:
#    - Expected discovery time for each node
#    - Actual lowest reachable time from each node
#    - Parent node to avoid going backwards
# 3. For each node:
#    - If actual discovery time of neighbor is >= expected
#      * No back edge exists
#      * Current edge is critical
#    - Update node's lowest reachable time
# 4. Return list of critical connections

class Solution:
   def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
       # Build undirected graph
       graph = defaultdict(set)
       for node1, node2 in connections:
           graph[node1].add(node2)
           graph[node2].add(node1)
       
       # Array to store lowest reachable discovery time
       lowestReachable = [n] * n  # Initialize with max possible value
       criticalEdges = []
       
       def dfs(node: int, expectedTime: int, parent: int) -> int:
           # If node not visited yet
           if lowestReachable[node] == n:
               # Set initial discovery time
               lowestReachable[node] = expectedTime
               
               # Visit all neighbors
               for neighbor in graph[node]:
                   # Skip parent to avoid going backwards
                   if neighbor != parent:
                       # Get lowest reachable time from neighbor
                       actualTime = dfs(neighbor, expectedTime + 1, node)
                       
                       # If no back edge exists, this is a critical connection
                       if actualTime >= expectedTime + 1:
                           criticalEdges.append([node, neighbor])
                       
                       # Update current node's lowest reachable time
                       lowestReachable[node] = min(lowestReachable[node], actualTime)
           
           return lowestReachable[node]
       
       # Start DFS from any node (using n-1 here)
       dfs(n-1, 0, -1)
       return criticalEdges
