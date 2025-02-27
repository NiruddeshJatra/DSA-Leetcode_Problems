# Time Complexity:
# - O(N), where N is the number of edges.
# - The union-find operations with path compression have an amortized time complexity that is nearly constant.
# - We process each edge once, and for each edge, we perform union-find operations.

# Space Complexity:
# - O(N) for the parent array to track the disjoint set.

# INTUITION:
# In a graph with N nodes, a tree should have exactly N-1 edges. If there are N edges, then one edge must be redundant
# and creates a cycle. The problem asks us to find this redundant edge that, when removed, would make the graph a tree.
#
# We can use the Union-Find (Disjoint Set) algorithm to detect cycles in the graph. As we process each edge:
# - If the two nodes of the edge are already in the same set (have the same root parent), it means adding this edge 
#   would create a cycle. This is our redundant edge.
# - Otherwise, we union the two nodes (merge their sets).
#
# Since we process edges in order and return the first edge that creates a cycle, if multiple edges could create cycles,
# we'll return the one that appears last in the input, which is what the problem requires.

# ALGO:
# 1. Initialize a parent array where each node is its own parent (disjoint sets).
# 2. For each edge (u, v):
#    a. Find the root parent of both u and v.
#    b. If they have the same root parent, this edge creates a cycle - return it.
#    c. Otherwise, union the sets of u and v (set one as the parent of the other).
# 3. Return the redundant edge.

class Solution:
   def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
       # Number of nodes
       n = len(edges)
       
       # Initialize parent array (0-indexed)
       parent = list(range(n + 1))
       
       def findParent(node):
           """Find the root parent of a node with path compression."""
           if parent[node] != node:
               parent[node] = findParent(parent[node])
           return parent[node]
       
       def union(u, v):
           """Union two sets. Returns False if they're already in the same set."""
           rootU = findParent(u)
           rootV = findParent(v)
           
           # If both nodes have the same root, adding this edge creates a cycle
           if rootU == rootV:
               return False
           
           # Union the sets by setting one root as the parent of the other
           parent[rootV] = rootU
           return True
       
       # Process each edge
       for u, v in edges:
           # If union fails, we found our redundant edge
           if not union(u, v):
               return [u, v]
       
       # This should not happen if the input is valid
       return []
