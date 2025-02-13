# Time Complexity:
# - O((V + E) * log V) where V is vertices and E is edges
# - Each vertex extracted from heap once: O(V * log V)
# - Each edge relaxation requires heap operation: O(E * log V)
# - Overall: O((V + E) * log V)

# Space Complexity:
# - O(V) for distance array, ways array and heap
# - O(E) for adjacency list
# - Overall space: O(V + E)

# INTUITION:
# Like planning road trips between cities where:
# - Need to find shortest total distance
# - Also count how many different routes give that distance
# - Like GPS showing multiple routes with same ETA
#
# Example:
# [0]--2--[1]--1--[2]
#  \       |
#   3      2
#    \     |
#     ----[3]
#
# To reach node 3:
# 1. Path 0->1->3: distance 4
# 2. Path 0->3: distance 3 (shortest)
# So only 1 shortest path exists

# ALGORITHM:
# Modified Dijkstra's algorithm that:
# 1. Tracks shortest distance to each node (like regular Dijkstra)
# 2. Also counts number of ways to reach each node with minimum distance
# 3. When finding path with equal distance:
#    - Don't update distance
#    - Add number of ways to reach previous node
# 4. Use modulo to handle large numbers

from collections import defaultdict
import heapq

class Solution:
   def countPaths(self, n: int, roads: List[List[int]]) -> int:
       # Build adjacency list for undirected weighted graph
       adjacencyList = defaultdict(list)
       for sourceNode, targetNode, weight in roads:
           adjacencyList[sourceNode].append((targetNode, weight))
           adjacencyList[targetNode].append((sourceNode, weight))
       
       # Initialize distance and ways arrays
       shortestDistance = [float('inf')] * n
       shortestDistance[0] = 0
       numberOfWays = [0] * n
       numberOfWays[0] = 1
       MOD = 1000000007
       
       # Priority queue for path selection
       # Format: (total_cost, node)
       priorityQueue = [(0, 0)]
       
       while priorityQueue:
           currentCost, currentNode = heapq.heappop(priorityQueue)
           
           # Process all neighbors
           for neighborNode, edgeCost in adjacencyList[currentNode]:
               newTotalCost = currentCost + edgeCost
               
               # Found shorter path
               if newTotalCost < shortestDistance[neighborNode]:
                   shortestDistance[neighborNode] = newTotalCost
                   numberOfWays[neighborNode] = numberOfWays[currentNode]
                   heapq.heappush(priorityQueue, (newTotalCost, neighborNode))
                   
               # Found another path with same distance
               elif newTotalCost == shortestDistance[neighborNode]:
                   numberOfWays[neighborNode] = (numberOfWays[neighborNode] + 
                                               numberOfWays[currentNode]) % MOD
       
       return numberOfWays[n-1]
