# Time Complexity: O(V + E) where V is vertices and E is edges
# Space Complexity: O(V) for visited set, colors array and recursion stack

# INTUITION:
# A graph is bipartite if nodes can be colored using 2 colors where no adjacent 
# nodes have same color. Use DFS to:
# - Color nodes alternately (0/1)
# - Check if neighbors have opposite colors
# Example: [[1,2,3],[0,2],[0,1,3],[0,2]]
# Can color: 0->0, 1->1, 2->1, 3->1 so not bipartite

class Solution:
   def isBipartite(self, graph: List[List[int]]) -> bool:
       def dfs(node: int, color: int) -> bool:
           visitedNodes.add(node)
           nodeColors[node] = color
           
           for neighbor in graph[node]:
               if neighbor not in visitedNodes:
                   if not dfs(neighbor, 1 - color):  # Flip color (0->1, 1->0)
                       return False
               elif nodeColors[neighbor] == color:  # Same color conflict
                   return False
                   
           return True
           
       visitedNodes = set()
       nodeColors = [-1] * len(graph)  # -1: uncolored, 0/1: colors
       
       # Check each component
       for node in range(len(graph)):
           if node not in visitedNodes and not dfs(node, 0):
               return False
               
       return True
