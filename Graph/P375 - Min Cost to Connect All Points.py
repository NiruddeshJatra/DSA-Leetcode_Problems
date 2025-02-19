# Time Complexity:
# - O(N^2 log N) where N is the number of points
# - O(N^2) to generate all edges between points
# - O(N^2 log N^2) = O(N^2 log N) for sorting edges
# - O(N) for union-find operations after sorting

# Space Complexity:
# - O(N^2) for storing all possible edges between points
# - O(N) for the DisjointSet data structure

# INTUITION:
# This is a Minimum Spanning Tree (MST) problem where:
# - Vertices are the given points
# - Edges are Manhattan distances between points
# - Weight of each edge is the Manhattan distance
#
# Example:
# points = [[0,0], [2,2], [3,10], [5,2]]
# First calculate all distances:
# (0,0)->(2,2): 4
# (0,0)->(3,10): 13
# (0,0)->(5,2): 7
# (2,2)->(3,10): 9
# (2,2)->(5,2): 3
# (3,10)->(5,2): 10
#
# After sorting distances and applying Kruskal's:
# 1. Add (2,2)->(5,2) = 3
# 2. Add (0,0)->(2,2) = 4
# 3. Add (2,2)->(3,10) = 9
# Total = 16

# ALGO:
# 1. Generate all edges with Manhattan distances between points
# 2. Sort edges by distance
# 3. Use Kruskal's algorithm with Union-Find to build MST:
#    - Take edges in ascending order of weight
#    - Add edge if it doesn't create cycle
#    - Stop when we have N-1 edges
# 4. Return total weight of MST

class DisjointSet:
   def __init__(self, n):
       self.parent = list(range(n))  # Each node is its own parent initially
   
   def findParent(self, node):
       # Path compression
       if node != self.parent[node]:
           self.parent[node] = self.findParent(self.parent[node])
       return self.parent[node]
       
   def union(self, i, j):
       parentOfI = self.findParent(i)
       parentOfJ = self.findParent(j)
       
       # If already in same component
       if parentOfI == parentOfJ:
           return False
           
       # Merge components
       self.parent[parentOfI] = parentOfJ
       return True


class Solution:
   def minCostConnectPoints(self, points: List[List[int]]) -> int:
       # Generate all edges with Manhattan distances
       edges = []
       n = len(points)
       
       for i in range(n):
           for j in range(i+1, n):
               # Calculate Manhattan distance
               manhattanDistance = abs(points[i][0] - points[j][0]) + \
                                 abs(points[i][1] - points[j][1])
               edges.append([manhattanDistance, i, j])
       
       # Sort edges by distance
       edges.sort()
       
       # Initialize result and edge counter
       totalCost = 0
       edgesUsed = 0
       disjointSet = DisjointSet(n)
       
       # Process edges in sorted order (Kruskal's algorithm)
       for weight, point1, point2 in edges:
           # If adding this edge doesn't create cycle
           if disjointSet.union(point1, point2):
               totalCost += weight
               edgesUsed += 1
               
               # Early exit when we have N-1 edges (MST complete)
               if edgesUsed == n - 1:
                   return totalCost
       
       return 0  # In case points can't be connected
