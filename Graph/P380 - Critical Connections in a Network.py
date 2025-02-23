# Time Complexity:
# - O(V + E) where V is number of vertices and E is number of edges
# - Each vertex is visited once and each edge is traversed once in DFS
# - Building adjacency list takes O(E)

# Space Complexity:
# - O(V + E) for adjacency list representation of graph
# - O(V) for lows array to track discovery times
# - O(V) for recursion stack in worst case
# - O(E) for storing critical connections in result

# INTUITION:
# A critical connection (bridge) is an edge whose removal disconnects the graph.
# Similar to articulation points, we can find bridges using DFS by tracking:
# 1. Discovery time of each vertex
# 2. Lowest vertex (by time) that can be reached from each vertex through back edges
#
# Example:
#     1 --- 2
#     |     |
#     4 --- 3
#     |
#     5
# Edge (4,5) is a bridge because removing it disconnects vertex 5 from the rest.
# When we DFS through this edge, vertex 5 can't reach back to vertex 4's ancestors.

# ALGO:
# 1. Build undirected graph using adjacency list
# 2. Do DFS traversal tracking for each vertex:
#    - Its discovery time 
#    - Lowest reachable vertex through back edges
# 3. An edge (u,v) is bridge if:
#    - Child v cannot reach any ancestor of u through back edges
#    - i.e., lowest reachable time of v > discovery time of u
# 4. Use back edges to update lowest reachable times

from typing import List, Set
from collections import defaultdict

class Solution:
   def criticalConnections(self, numNodes: int, connections: List[List[int]]) -> List[List[int]]:
       # Build undirected graph
       graph = defaultdict(set)
       for source, target in connections:
           graph[source].add(target)
           graph[target].add(source)

       # Track discovery times and bridges
       discoveryTimes = [numNodes] * numNodes  # Use numNodes as unvisited marker
       bridges = []

       def dfsTraversal(currentNode: int, currentTime: int, parentNode: int) -> int:
           if discoveryTimes[currentNode] == numNodes:  # Node not visited
               discoveryTimes[currentNode] = currentTime

               # Process all neighbors
               for neighborNode in graph[currentNode]:
                   if neighborNode == parentNode:  # Skip parent
                       continue

                   if discoveryTimes[neighborNode] == numNodes:  # Unvisited neighbor
                       lowestTime = dfsTraversal(neighborNode, currentTime + 1, currentNode)
                       discoveryTimes[currentNode] = min(discoveryTimes[currentNode], lowestTime)

                       # Check bridge condition
                       if lowestTime > currentTime:
                           bridges.append([currentNode, neighborNode])
                   else:  # Back edge - update with neighbor's discovery time
                       discoveryTimes[currentNode] = min(discoveryTimes[currentNode],
                                                       discoveryTimes[neighborNode])

           return discoveryTimes[currentNode]

       # Start DFS from node 0 since graph is connected
       dfsTraversal(0, 0, -1)
       return bridges
