# Time Complexity:
# - O(V³) where V is number of vertices (cities)
# - Floyd-Warshall algorithm uses 3 nested loops to find all-pairs shortest paths
# - Additional O(V²) to count reachable cities for each vertex

# Space Complexity:
# - O(V²) for the distance matrix storing shortest paths between all pairs of cities
# - O(1) additional space for variables tracking minimum city count

# INTUITION:
# Need to find city that can reach minimum number of other cities within threshold distance.
# Use Floyd-Warshall to find shortest paths between all pairs of cities, then count
# reachable cities for each city.
# Example: With edges [(0,1,2), (1,2,1), (2,3,3)] and threshold 3:
# - City 0 can reach cities {0,1,2} within 3 units
# - City 1 can reach {0,1,2,3} within 3 units 
# - City 2 can reach {0,1,2,3} within 3 units
# - City 3 can reach {1,2,3} within 3 units
# City 3 wins (ties broken by highest number)

# ALGO:
# 1. Initialize distance matrix:
#    - Set diagonal to 0 (distance to self)
#    - Set direct edges to their weights (undirected graph)
#    - Set other distances to infinity
# 2. Run Floyd-Warshall to find all shortest paths:
#    - For each intermediate vertex k
#    - Update distances if path through k is shorter
# 3. For each city:
#    - Count cities reachable within threshold
#    - Update answer if count is smaller (or equal but city number larger)
# 4. Return city with minimum reachable cities

from typing import List

class Solution:
   def findTheCity(self, numCities: int, edges: List[List[int]], 
                  distanceThreshold: int) -> int:
       # Initialize distance matrix with infinity
       INF = int(1e9)
       shortestPaths = [[INF] * numCities for _ in range(numCities)]
       
       # Set distance to self = 0
       for city in range(numCities):
           shortestPaths[city][city] = 0
       
       # Set initial distances from edges (undirected graph)
       for city1, city2, weight in edges:
           shortestPaths[city1][city2] = weight
           shortestPaths[city2][city1] = weight
       
       # Floyd-Warshall algorithm
       for intermediate in range(numCities):
           for start in range(numCities):
               for end in range(numCities):
                   if (shortestPaths[start][intermediate] != INF and 
                       shortestPaths[intermediate][end] != INF and 
                       shortestPaths[start][end] > 
                       shortestPaths[start][intermediate] + shortestPaths[intermediate][end]):
                       shortestPaths[start][end] = (shortestPaths[start][intermediate] + 
                                                  shortestPaths[intermediate][end])
       
       # Find city with minimum reachable cities
       resultCity = 0
       minReachableCities = numCities
       
       for currentCity in range(numCities):
           reachableCities = 0
           # Count cities within threshold distance
           for otherCity in range(numCities):
               if shortestPaths[currentCity][otherCity] <= distanceThreshold:
                   reachableCities += 1
           
           # Update result if we found fewer reachable cities
           # or same number but higher city number
           if reachableCities <= minReachableCities:
               resultCity = currentCity
               minReachableCities = reachableCities
       
       return resultCity
