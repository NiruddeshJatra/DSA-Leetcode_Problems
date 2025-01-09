# Time Complexity:
# - O(N), where N is the number of nodes in the binary tree
# - We visit each node exactly once during the DFS traversal
# - At each node, we perform O(1) operations (comparisons and additions)

# Space Complexity:
# - O(H), where H is the height of the tree, used by the recursive call stack
# - In worst case (skewed tree), H = N, making it O(N)
# - We use O(1) extra space for the maxSum variable

# INTUITION:
# The maximum path sum in a binary tree could be any valid path, not necessarily through root.
# Using DFS with a global max tracker is ideal because:
# 1. At each node, we have two choices:
#    - Continue the path upward (return value)
#    - Complete the path at this node (update global max)
# 2. We can ignore negative paths by taking max with 0
# 3. Each node needs to return best "single" path while tracking complete paths globally
# 4. Bottom-up approach lets us build paths optimally

# ALGO:
# 1. Initialize global maxSum as negative infinity (to handle all negative values)
# 2. For each node in DFS:
#    - Get max path sums from left and right (take 0 if negative)
#    - Calculate current complete path: node.val + leftSum + rightSum
#    - Update global maxSum if current path is larger
#    - Return best single path: node.val + max(leftSum, rightSum)
# 3. Return final maxSum

class Solution:
   def maxPathSum(self, root: Optional[TreeNode]) -> int:
       # Use list for mutable reference to track maximum path sum
       global_max_sum = [float('-inf')]
       
       def calculate_path_sum(node: Optional[TreeNode]) -> int:
           # Base case: empty node contributes no sum
           if not node:
               return 0
           
           # Get maximum path sums from left and right subtrees
           # Take max with 0 to handle negative values
           left_max = max(calculate_path_sum(node.left), 0)
           right_max = max(calculate_path_sum(node.right), 0)
           
           # Current complete path includes node value and both subtrees
           current_path_sum = node.val + left_max + right_max
           
           # Update global maximum if current path is larger
           global_max_sum[0] = max(global_max_sum[0], current_path_sum)
           
           # Return maximum single path that can be used by parent
           # (can only include one subtree for a valid path)
           return node.val + max(left_max, right_max)
       
       calculate_path_sum(root)
       return global_max_sum[0]
