# Time Complexity:
# - O(N * K) where N is number of nodes and K is max stops allowed
# - Each node can be processed K times (once for each stop count)
# - Using BFS means we process all paths with same number of stops before moving to next level

# Space Complexity:
# - O(N + E) where N is number of nodes and E is number of edges (flights)
# - O(N) for the distance array and queue
# - O(E) for the adjacency list representation

# INTUITION:
# Unlike standard shortest path, we need to consider paths with at most K stops.
# BFS is perfect here as it processes paths level by level, where each level represents number of stops.
# Why not Dijkstra? Because cheaper paths might have more stops, and we need to explore all possibilities
# within K stops.
# Example: For flights [(0,1,100), (0,2,500), (1,2,100)] from 0->2 with K=1:
# Direct path costs 500, but path 0->1->2 costs 200 with 1 stop.

# ALGO:
# 1. Build adjacency list where adj[u] stores (v, price) for flight u->v
# 2. Use queue to store (stops, node, currentCost)
# 3. Initialize distances with infinity except source = 0
# 4. For each state from queue:
#    - If stops <= K, explore neighbors
#    - For each neighbor:
#      * Calculate new cost = currentCost + flightCost
#      * If new cost is cheaper, update distance and add to queue
# 5. Return final distance to destination if reachable, else -1

from typing import List
from collections import defaultdict, deque

class Solution:
   def findCheapestPrice(self, numCities: int, flights: List[List[int]], source: int, 
                        destination: int, maxStops: int) -> int:
       # Build adjacency list representation
       flightConnections = defaultdict(list)
       for fromCity, toCity, price in flights:
           flightConnections[fromCity].append((toCity, price))
       
       # Initialize queue with (stops, city, totalCost)
       flightQueue = deque([(0, source, 0)])
       
       # Track minimum cost to reach each city
       minCostToCity = [float('inf')] * numCities
       minCostToCity[source] = 0
       
       # Process cities level by level (BFS)
       while flightQueue:
           currentStops, currentCity, currentCost = flightQueue.popleft()
           
           # Only process if we haven't exceeded maxStops
           if currentStops <= maxStops:
               # Check all possible flights from current city
               for nextCity, flightPrice in flightConnections[currentCity]:
                   newCost = currentCost + flightPrice
                   
                   # If we found a cheaper route, update and explore
                   if newCost < minCostToCity[nextCity]:
                       minCostToCity[nextCity] = newCost
                       flightQueue.append((currentStops + 1, nextCity, newCost))
       
       # Return minimum cost to destination if reachable
       return minCostToCity[destination] if minCostToCity[destination] != float('inf') else -1
