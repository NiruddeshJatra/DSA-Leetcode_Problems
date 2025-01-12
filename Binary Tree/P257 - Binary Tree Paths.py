# Time Complexity:
# - O(N), where N is the number of nodes in the binary tree
# - We need to visit each node exactly once 
# - String concatenation takes additional time but is dominated by the traversal

# Space Complexity:
# - O(H), where H is the height of the tree, for the recursion stack
# - In worst case (skewed tree), H = N, making it O(N)
# - Additional O(N) space needed to store the final paths

# INTUITION:
# We can find all root-to-leaf paths using DFS with backtracking. At each node:
# 1. Add current node value to the current path
# 2. If it's a leaf node, we've found a complete path to add to our result
# 3. Otherwise, continue DFS on left and right children
# 4. Backtrack by removing current node from path before returning
# This ensures we build all possible paths while maintaining the correct state.

# ALGORITHM:
# 1. Use DFS helper function that takes current node and current path
# 2. For each node:
#    - Add node value to current path
#    - If leaf node: convert path to string with -> separator and add to results
#    - Else: recursively process left and right children
#    - Backtrack by removing current node value from path
# 3. Call DFS with root and empty path
# 4. Return list of all paths

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
   def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
       all_paths = []
       
       def dfs(node: TreeNode, current_path: List[str]) -> None:
           # Base case: null node
           if not node:
               return
               
           # Add current node value to path
           current_path.append(str(node.val))
           
           # If leaf node, we've found a complete path
           if not node.left and not node.right:
               all_paths.append('->'.join(current_path))
           else:
               # Continue DFS on children
               dfs(node.left, current_path)
               dfs(node.right, current_path)
               
           # Backtrack by removing current node from path
           current_path.pop()
       
       # Start DFS from root with empty path
       dfs(root, [])
       return all_paths
