# Time Complexity:
# - O(N) to visit every node in the tree
# - O(N) for path copying at each node
# - Overall O(N^2) in worst case (highly unbalanced tree)

# Space Complexity:
# - O(H) for recursion stack where H is tree height
# - O(N) for storing paths in result
# - Each path can be O(H) length
# - Overall O(N*H) in worst case

# INTUITION:
# Use DFS to track paths from root to leaf:
# 1. Add current node value to running sum
# 2. Add node value to current path
# 3. If leaf node and sum matches target, found valid path
# Example:
#     10
#    /  \
#   5   15
#  / \    \
# 3   7    18
# Target = 18
# Paths: [10,5,3], [10,8]

# ALGO:
# 1. Use DFS helper function tracking:
#    - Current node
#    - Running sum
#    - Current path
# 2. At each node:
#    - Add value to sum
#    - Add value to path
#    - If leaf node and sum matches target:
#      * Add path to results
#    - Recursively check left and right subtrees
# 3. Return all valid paths found

def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
   def dfs(node: TreeNode, currentSum: int, currentPath: List[int]) -> None:
       if not node:
           return
           
       # Update sum and path
       currentSum += node.val
       newPath = currentPath + [node.val]
       
       # Check if valid leaf path
       if not node.left and not node.right and currentSum == targetSum:
           validPaths.append(newPath)
           
       # Check subtrees
       dfs(node.left, currentSum, newPath)
       dfs(node.right, currentSum, newPath)
   
   validPaths = []
   dfs(root, 0, [])
   return validPaths
