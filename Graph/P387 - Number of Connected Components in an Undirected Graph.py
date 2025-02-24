# Time Complexity:
# - O(V + E) where V is number of vertices and E is number of edges
# - Each vertex is visited once in DFS
# - Each edge is explored once
# - Building adjacency list takes O(E)

# Space Complexity: 
# - O(V + E) for adjacency list representation of graph
# - O(V) for visited set
# - O(V) for recursion stack in worst case of linear graph 

# INTUITION:
# The number of connected components equals the number of DFS calls needed
# to visit all nodes. When we do DFS from a node, we mark all reachable nodes
# as visited. Any unvisited nodes must be in a different component.
#
# Example:
# n = 5, edges = [[0,1], [1,2], [3,4]]
# This creates two components:
# Component 1: 0-1-2
# Component 2: 3-4
# DFS from 0 visits {0,1,2}
# DFS from 3 visits {3,4}
# Total: 2 components

# ALGO:
# 1. Build undirected graph using adjacency list
# 2. Keep track of visited nodes
# 3. For each unvisited node:
#    - Do DFS to mark all reachable nodes
#    - Increment component count
# 4. Return component count

class Solution:
   def countComponents(self, n: int, edges: List[List[int]]) -> int:
       def dfsExplore(currentNode: int) -> None:
           """
           Explore all nodes reachable from current node using DFS
           """
           visited.add(currentNode)
           
           # Visit all unvisited neighbors
           for nextNode in graph[currentNode]:
               if nextNode not in visited:
                   dfsExplore(nextNode)
       
       # Build undirected graph
       graph = defaultdict(set)
       for source, target in edges:
           graph[source].add(target)
           graph[target].add(source)
           
       visited = set()
       componentCount = 0
       
       # Count connected components
       for node in range(n):
           if node not in visited:
               dfsExplore(node)
               componentCount += 1
               
       return componentCount
