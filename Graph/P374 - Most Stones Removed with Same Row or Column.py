# Time Complexity:
# - O(N × α(N)) where N is the number of stones
# - Each union and find operation takes amortized O(α(N)) time, where α is the inverse Ackermann function
# - We perform N union operations and up to N find operations

# Space Complexity:
# - O(N) for the parent dictionary storing the disjoint set relationships

# INTUITION:
# The key insight is that any stones sharing the same row or column can be considered connected,
# and we can remove all but one stone from each connected component.
#
# To handle row and column connections efficiently, we use a trick: represent columns as negative
# numbers (~y) to avoid confusion with row numbers. This way we can use a single parent dictionary
# to track both row and column connections.
#
# Example:
# stones = [[0,0], [0,2], [1,1], [2,0], [2,2]]
# Components: {[0,0], [0,2]} and {[1,1]} and {[2,0], [2,2]}
# We can remove 2 stones, leaving one stone in each component
#
# The answer is total stones minus number of connected components, because:
# - Each component must have at least one stone remaining
# - All other stones in the component can be removed

# ALGO:
# 1. Initialize a parent dictionary for union-find
# 2. For each stone:
#    - Union its row number with negative of its column number (~y)
#    - This connects all stones sharing either same row or column
# 3. Count number of unique parents (connected components)
# 4. Return total stones minus number of components

class Solution:
   def removeStones(self, stones: List[List[int]]) -> int:
       # Parent dictionary for union-find
       parent = {}
       
       def findParent(x):
           # Path compression: point node directly to root
           if x != parent[x]:
               parent[x] = findParent(parent[x])
           return parent[x]
       
       def union(x, y):
           # Initialize if not in parent dictionary
           if x not in parent:
               parent[x] = x
           if y not in parent:
               parent[y] = y
           
           # Union by connecting roots
           xParent = findParent(x)
           yParent = findParent(y)
           parent[xParent] = yParent
       
       # Union rows with columns (using ~y for columns)
       for row, col in stones:
           union(row, ~col)  # Using bitwise NOT to distinguish columns
       
       # Count number of unique components
       connectedComponents = sum(1 for x in parent if findParent(x) == x)
       
       # Result is total stones minus number of components
       # (we must keep one stone per component)
       return len(stones) - connectedComponents
