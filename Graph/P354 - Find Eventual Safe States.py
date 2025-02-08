# Time Complexity:
# - O(V + E) where V is vertices and E is edges
# - Each node visited once in DFS
# - Final sorting takes O(V log V)

# Space Complexity:
# - O(V) for visited and path sets
# - O(V) for recursion stack
# - O(V) for result array

# INTUITION:
# Safe nodes are those that aren't part of/don't lead to cycles
# Use DFS with path tracking to:
# - Detect cycles 
# - Mark nodes as safe if no cycles found
# Example: graph = [[1,2],[2,3],[5],[0],[5],[]]
# Node 5 is safe (terminal)
# Nodes 0,1,2,3 form cycle -> unsafe
# Node 4 leads to safe node -> safe
# Result: [4,5]

# ALGO:
# 1. For each unvisited node:
#    - Track visited nodes and current path
#    - If cycle found, mark nodes as unsafe
#    - If no cycle, add to safe nodes
# 2. Return sorted list of safe nodes

class Solution:
   def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
       def dfs(currentNode: int) -> bool:
           visitedNodes.add(currentNode)
           currentPath.add(currentNode)
           
           for nextNode in graph[currentNode]:
               if nextNode not in visitedNodes:
                   if dfs(nextNode):
                       return True
               elif nextNode in currentPath:
                   return True
                   
           currentPath.remove(currentNode)
           safeNodes.append(currentNode)
           return False
           
       visitedNodes = set()
       currentPath = set()
       safeNodes = []
       
       for node in range(len(graph)):
           if node not in visitedNodes:
               dfs(node)
               
       return sorted(safeNodes)
