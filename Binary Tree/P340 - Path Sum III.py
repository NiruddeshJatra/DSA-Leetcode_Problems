# Time Complexity:
# - O(N) where N is the number of nodes in the tree
# - Each node is visited exactly once
# - Constant time operations at each node

# Space Complexity:
# - O(H) for recursion stack, where H is tree height
# - Best case O(logN) for balanced tree
# - Worst case O(N) for skewed tree
# - Additional O(N) space for prefix sum dictionary

# INTUITION:
# Find number of paths that sum to target using prefix sum technique
# Key concepts:
# 1. Track cumulative sum from root
# 2. Use hash map to count prefix sums
# 3. Check if current sum - target exists in prefix sums
# Example: [10,5,-3,3,2,null,11,3,-2,null,1], target = 8
# Paths: 
# 5 -> 3
# 5 -> 2 -> 1
# -3 -> 11

# ALGO:
# 1. Use DFS with prefix sum tracking
# 2. Maintain running sum from root
# 3. Check if (current sum - target) exists in prefix sums
# 4. Update prefix sum count
# 5. Recursively process left and right subtrees
# 6. Backtrack by removing current sum from prefix count

def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
   def dfs(node: TreeNode, currentSum: int, prefixSumCount: dict) -> None:
       nonlocal totalPaths
       if not node:
           return
       
       # Update current cumulative sum
       currentSum += node.val
       
       # Check if path exists with target sum
       if currentSum - targetSum in prefixSumCount:
           totalPaths += prefixSumCount[currentSum - targetSum]
       
       # Update prefix sum count
       prefixSumCount[currentSum] = prefixSumCount.get(currentSum, 0) + 1
       
       # Recursively process left and right subtrees
       dfs(node.left, currentSum, prefixSumCount)
       dfs(node.right, currentSum, prefixSumCount)
       
       # Backtrack: remove current sum from prefix count
       prefixSumCount[currentSum] -= 1
   
   # Initialize path count and start DFS
   totalPaths = 0
   # Start with {0:1} to handle paths from root
   dfs(root, 0, {0: 1})
   
   return totalPaths
