# Time Complexity:
# - O(E + Q * (V + E)), where:
#   - E is the number of equations
#   - Q is the number of queries
#   - V is the number of distinct variables
# - Building the graph takes O(E) time
# - For each query, we potentially traverse the entire graph in the worst case O(V + E)

# Space Complexity:
# - O(V + E) for the graph representation
# - O(V) for the visited set in DFS
# - O(V) for the recursion stack in the worst case

# INTUITION:
# We can represent this problem as a graph where:
# - Each variable is a node
# - Each equation creates two directed edges with their respective weights
#   (e.g., a/b = 2 creates edges a→b with weight 2 and b→a with weight 1/2)
#
# For example, if we have a/b = 2 and b/c = 3, our graph would be:
# a → b (weight 2)
# b → a (weight 1/2)
# b → c (weight 3)
# c → b (weight 1/3)
#
# To evaluate a query like a/c, we need to find a path from a to c and multiply all weights along the path:
# a → b → c = 2 * 3 = 6
#
# DFS can be used to find such paths.

# ALGO:
# 1. Build a graph where each variable is a node and equations define weighted edges
# 2. For each query (a, b):
#    a. If either variable doesn't exist in our graph, return -1
#    b. Use DFS to find a path from a to b, multiplying values along the path
#    c. If no path exists, return -1
# 3. Return the results for all queries

from collections import defaultdict

class Solution:
   def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
       # Build the graph
       graph = defaultdict(list)
       
       # Add edges in both directions with appropriate weights
       for (numerator, denominator), value in zip(equations, values):
           graph[numerator].append((denominator, value))
           graph[denominator].append((numerator, 1.0 / value))
       
       def findPathValue(start, end, visited):
           """
           Use DFS to find a path from start to end and calculate the product of weights along the path.
           Returns the result of division or None if no path exists.
           """
           # Base case: if start node is the same as end node
           if start == end:
               return 1.0
           
           # Mark current node as visited
           visited.add(start)
           
           # Explore all neighbors
           for neighbor, weight in graph[start]:
               if neighbor not in visited:
                   # Recursively find path from neighbor to end
                   pathValue = findPathValue(neighbor, end, visited)
                   
                   # If a path is found, return the result
                   if pathValue is not None:
                       return weight * pathValue
           
           # No path found
           return None
       
       # Process each query
       results = []
       for numerator, denominator in queries:
           # If either variable doesn't exist in our graph, result is -1
           if numerator not in graph or denominator not in graph:
               results.append(-1.0)
           else:
               # Try to find a path using DFS
               result = findPathValue(numerator, denominator, set())
               results.append(result if result is not None else -1.0)
       
       return results
