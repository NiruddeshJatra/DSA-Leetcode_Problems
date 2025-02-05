# Time Complexity:
# - O(N^2) where N is the number of cities
# - We must check each cell in the adjacency matrix once
# - For each unvisited node, DFS visits all connected nodes

# Space Complexity:
# - O(N) for the visited set storing at most N cities
# - O(N) for the recursion stack in worst case of a linear graph
# - The adjacency matrix is input so not counted in space complexity

# INTUITION:
# The problem is to find the number of connected components in an undirected graph
# where each city is a node and connections form edges.
# Using DFS, when we visit a node we mark all reachable nodes as visited.
# Each time we need to start a new DFS, we've found a new province.
# Example: For matrix: [[1,1,0],
#                      [1,1,0],
#                      [0,0,1]]
# Cities 0,1 form one province and city 2 forms another, so answer is 2

# ALGO:
# 1. Initialize visited set and province counter
# 2. For each unvisited city:
#    - Increment province counter
#    - Do DFS to mark all connected cities as visited
# 3. Return total number of provinces (connected components)

class Solution:
   def findCircleNum(self, isConnected: List[List[int]]) -> int:
       def dfsVisit(currentCity: int) -> None:
           """Visit all cities in current province using DFS"""
           for neighborCity, isConnectedTo in enumerate(isConnected[currentCity]):
               if isConnectedTo and neighborCity not in visitedCities:
                   visitedCities.add(neighborCity)
                   dfsVisit(neighborCity)
       
       numCities = len(isConnected)
       visitedCities = set()
       provinceCount = 0
       
       # Find each province using DFS
       for city in range(numCities):
           if city not in visitedCities:
               visitedCities.add(city)
               dfsVisit(city)
               provinceCount += 1
       
       return provinceCount
