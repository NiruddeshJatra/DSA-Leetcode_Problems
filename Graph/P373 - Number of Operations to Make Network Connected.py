# Time Complexity:
# - O(E × α(n)), where E is the number of edges (connections) and α is the inverse Ackermann function
# - For each connection, we perform union-find operations which take amortized O(α(n)) time
# - Since α(n) grows extremely slowly, it's effectively constant in practice

# Space Complexity:
# - O(n) for the DisjointSet data structure, storing parent and size arrays

# INTUITION:
# The problem asks for the minimum number of operations needed to connect all computers. 
# This is essentially asking: how many edges do we need to add to make the graph fully connected?
# 
# We can use Disjoint Set (Union-Find) to identify connected components in the network.
# Each component represents a group of computers that are already connected.
# To connect all components, we need (number of components - 1) new connections.
#
# Example:
# Consider 6 computers with connections [(0,1), (0,2), (3,4)]
# We have 3 connected components: {0,1,2}, {3,4}, and {5}
# We need (3-1) = 2 new connections to connect all components
#
# Additionally, if we don't have enough cables (connections) to begin with,
# it's impossible to connect all computers. We need at least (n-1) connections
# for n computers.

# ALGO:
# 1. Check if we have at least (n-1) connections - if not, return -1 as it's impossible
# 2. Initialize a DisjointSet with n elements
# 3. Process each connection by performing union operations
# 4. Count the number of connected components after processing all connections
# 5. Return (number of components - 1) as the answer

from typing import List

class DisjointSet:
   def __init__(self, n):
       self.size = [1] * (n)  # Size of each set
       self.parent = list(range(n))  # Each node is initially its own parent
       self.count = n  # Number of connected components
   
   def findParent(self, node):
       # Path compression: make each node point to its grandparent
       while node != self.parent[node]:
           self.parent[node] = self.parent[self.parent[node]]
           node = self.parent[node]
       return node
       
   def unionBySize(self, i, j):
       parentOfI = self.findParent(i)
       parentOfJ = self.findParent(j)
       
       # If already in the same component, do nothing
       if parentOfI == parentOfJ:
           return
       
       # Merge smaller component into larger one
       if self.size[parentOfI] > self.size[parentOfJ]:
           self.parent[parentOfJ] = parentOfI
           self.size[parentOfI] += self.size[parentOfJ]
       else:
           self.parent[parentOfI] = parentOfJ
           self.size[parentOfJ] += self.size[parentOfI]
       
       # Decrement component count as we've merged two components
       self.count -= 1


class Solution:
   def makeConnected(self, n: int, connections: List[List[int]]) -> int:
       # Check if we have enough cables to connect all computers
       # Need at least n-1 connections for n computers
       if len(connections) < n - 1:
           return -1
       
       # Initialize DisjointSet
       disjointSet = DisjointSet(n)
       
       # Process each connection
       for computer1, computer2 in connections:
           disjointSet.unionBySize(computer1, computer2)
       
       # Result is the number of components minus 1
       # (the number of new connections needed)
       return disjointSet.count - 1
