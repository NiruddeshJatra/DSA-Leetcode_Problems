# Time Complexity:
# - O(N log N), where N is the number of nodes in the binary tree
# - DFS traversal is O(N)
# - Sorting column keys is O(W log W) where W is width of tree
# - Sorting nodes within each column is O(H log H) where H is nodes in column
# - Overall worst case: O(N log N) when most nodes are in same column

# Space Complexity:
# - O(N) for storing all nodes in columns dictionary
# - O(H) for recursion stack where H is height of tree
# - Additional O(N) for result array
# - Overall: O(N)

# INTUITION:
# Vertical traversal requires grouping nodes by their horizontal distance from root,
# while maintaining vertical level ordering within each group.
# Using DFS with column tracking is ideal because:
# 1. Can track both column and level during traversal
# 2. Column distance naturally updates: left child = col-1, right child = col+1
# 3. Storing [level, val] pairs allows proper sorting within columns
# 4. Can sort columns and values after collection

# ALGO:
# 1. Use defaultdict to store nodes by column
# 2. DFS traversal:
#    - Store [level, value] for each node in its column
#    - Left child: decrease column by 1
#    - Right child: increase column by 1
# 3. Process results:
#    - Sort column keys for left-to-right order
#    - Sort nodes within each column by level and value
#    - Extract values in sorted order
# 4. Return final vertical order traversal

class Solution:
   def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
       # Dictionary to store nodes by column
       columnMap = defaultdict(list)
       finalResult = []
       
       def dfs(column: int, level: int, node: Optional[TreeNode]) -> None:
           if not node:
               return
               
           # Add current node info to its column
           columnMap[column].append([level, node.val])
           
           # Process children with updated column and level
           dfs(column - 1, level + 1, node.left)   # Left child is in prev column
           dfs(column + 1, level + 1, node.right)  # Right child is in next column
           
       # Perform DFS starting from root at column 0, level 0
       dfs(0, 0, root)
       
       # Process columns from left to right
       for col in sorted(columnMap.keys()):
           currentColumn = []
           
           # Sort nodes in current column by level and value
           for nodeInfo in sorted(columnMap[col]):
               currentColumn.append(nodeInfo[1])
               
           finalResult.append(currentColumn)
           
       return finalResult
