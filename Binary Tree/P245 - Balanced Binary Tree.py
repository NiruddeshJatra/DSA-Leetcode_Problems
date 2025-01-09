# Time Complexity:
# - O(N), where N is the number of nodes in the binary tree
# - We visit each node exactly once and perform O(1) work at each node
# - The height calculation and balance check are done during the same traversal

# Space Complexity:
# - O(H), where H is the height of the tree, used by the recursive call stack
# - In worst case (skewed tree), H = N, making it O(N)
# - No additional data structures are used beyond the call stack

# INTUITION:
# A binary tree is balanced if the heights of left and right subtrees differ by at most 1 
# for every node. We need both height and balance information at each step.
# Using bottom-up DFS is ideal because:
# 1. We can compute heights as we return up the tree
# 2. We can check balance criteria at each node in the same pass
# 3. We avoid recalculating heights multiple times (which would happen in a top-down approach)
# 4. Return tuple/list to carry both pieces of information (is_balanced and height)

# ALGO:
# 1. Define DFS helper function that returns [is_balanced, height]
# 2. Base case: empty node (None) returns [True, 0]
# 3. For each node:
#    - Recursively get [is_balanced, height] for left and right subtrees
#    - Current node is balanced if:
#      * Both subtrees are balanced
#      * Height difference between subtrees ≤ 1
#    - Return [current_node_balanced, 1 + max(left_height, right_height)]
# 4. Return only the is_balanced component of the result

class Solution:
   def isBalanced(self, root: Optional[TreeNode]) -> bool:
       def dfs(node) -> List[bool, int]:
           # Base case: empty node is balanced with height 0
           if not node:
               return [True, 0]
           
           # Get balance status and height of left and right subtrees
           left_status, right_status = dfs(node.left), dfs(node.right)
           
           # Unpack the results
           left_balanced, left_height = left_status
           right_balanced, right_height = right_status
           
           # Current node is balanced if:
           # 1. Both subtrees are balanced
           # 2. Height difference is at most 1
           current_balanced = (
               left_balanced and 
               right_balanced and 
               abs(left_height - right_height) <= 1
           )
           
           # Current height is 1 + max of subtree heights
           current_height = 1 + max(left_height, right_height)
           
           return [current_balanced, current_height]

       # Return only the balance status from the result
       return dfs(root)[0]
