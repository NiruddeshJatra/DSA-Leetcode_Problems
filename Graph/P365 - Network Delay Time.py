# Time Complexity:
# - O(E * log V) where E is the number of edges and V is the number of vertices
# - Each edge can be processed at most once, and each heap operation takes O(log V)

# Space Complexity:
# - O(V + E) where V is the number of vertices and E is the number of edges
# - O(V) for the distance array and heap
# - O(E) for the adjacency list representation

# INTUITION:
# To find the minimum time for a signal to reach all nodes, we need to find the shortest path from source
# to every other node. Dijkstra's algorithm is perfect for this as it handles weighted graphs with non-negative
# weights efficiently.
# Example: Given edges [(2,1,1), (2,3,1), (3,4,1)] with source=2:
# We start from node 2, explore its neighbors (1,3) with costs 1, then explore node 4 from 3 with total cost 2.

# ALGO:
# 1. Build adjacency list where adj[u] stores list of (v, weight) pairs for edge u->v
# 2. Initialize distance array with infinity, except distance[source] = 0
# 3. Use min-heap to store (currentCost, node) pairs
# 4. While heap not empty:
#    - Pop node with minimum current cost
#    - For each neighbor:
#      * Calculate new cost = currentCost + edgeCost
#      * If new cost is less than known distance, update and add to heap
# 5. Return max distance if all reachable, else -1

from typing import List
from collections import defaultdict
import heapq

class Solution:
   def networkDelayTime(self, times: List[List[int]], numNodes: int, sourceNode: int) -> int:
       # Build adjacency list representation
       adjacencyList = defaultdict(list)
       for sourceVertex, targetVertex, weight in times:
           adjacencyList[sourceVertex].append((targetVertex, weight))
           
       # Initialize distances array with infinity
       shortestDistances = [float('inf')] * (numNodes + 1)
       shortestDistances[sourceNode] = 0
       
       # Initialize min heap with source node
       # Format: (currentCost, currentNode)
       minHeap = [(0, sourceNode)]
       
       # Process nodes using Dijkstra's algorithm
       while minHeap:
           currentCost, currentNode = heapq.heappop(minHeap)
           
           # Process all neighbors of current node
           for nextNode, edgeWeight in adjacencyList[currentNode]:
               newCost = currentCost + edgeWeight
               
               # If we found a shorter path, update distance
               if newCost < shortestDistances[nextNode]:
                   shortestDistances[nextNode] = newCost
                   heapq.heappush(minHeap, (newCost, nextNode))
       
       # Get maximum time needed (excluding 0th index)
       maxTime = max(shortestDistances[1:])
       
       # Return -1 if any node is unreachable
       return maxTime if maxTime != float('inf') else -1
