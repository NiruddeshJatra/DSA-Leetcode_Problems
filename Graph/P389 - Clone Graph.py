# Time Complexity:
# - O(V + E), where V is the number of vertices (nodes) and E is the number of edges in the graph.
# - Each node is processed once when it's taken from the queue, and each edge is processed once when we iterate through neighbors.

# Space Complexity:
# - O(V) for the queue and the clones dictionary, which will store all vertices in the graph.

# INTUITION:
# To clone a graph, we need to create a copy of each node and recreate all the connections between them.
# The challenge is to handle cycles in the graph, ensuring we don't get stuck in an infinite loop.
# We use BFS to traverse the original graph and simultaneously build the clone graph.
# The key insight is to use a hash map to keep track of which nodes we've already cloned,
# so we don't create duplicate nodes for the same original node.

# ALGO:
# 1. Use a queue for BFS traversal starting from the input node.
# 2. Use a dictionary to map original nodes to their clones.
# 3. For each node we process:
#    a. Create clones for all its unvisited neighbors and add them to the queue.
#    b. Add connections from the current node's clone to all its neighbors' clones.
# 4. Return the clone of the starting node.

"""
# Definition for a Node.
class Node:
   def __init__(self, val = 0, neighbors = None):
       self.val = val
       self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
from collections import deque

class Solution:
   def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
       # Handle edge case: empty graph
       if not node:
           return None
           
       # Dictionary to map original nodes to their clones
       nodeToCloneMap = {}
       
       # BFS queue starting with the input node
       visitQueue = deque([node])
       
       # Create the clone of the starting node
       nodeToCloneMap[node] = Node(node.val)
       
       # Process nodes level by level (BFS)
       while visitQueue:
           # Get the next node to process
           currentNode = visitQueue.popleft()
           currentClone = nodeToCloneMap[currentNode]
           
           # Process all neighbors of the current node
           for neighborNode in currentNode.neighbors:
               # If we haven't seen this neighbor before
               if neighborNode not in nodeToCloneMap:
                   # Create a clone for this neighbor
                   nodeToCloneMap[neighborNode] = Node(neighborNode.val)
                   # Add neighbor to queue for processing
                   visitQueue.append(neighborNode)
               
               # Connect current clone to neighbor's clone
               currentClone.neighbors.append(nodeToCloneMap[neighborNode])
       
       # Return the clone of the starting node
       return nodeToCloneMap[node]
