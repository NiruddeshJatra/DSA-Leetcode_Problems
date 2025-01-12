# Time Complexity:
# - O(N), where N is the number of nodes in the binary tree
# - We need to visit each node once to find the LCA

# Space Complexity:
# - O(H), where H is the height of the tree
# - In worst case (skewed tree), H = N, making it O(N)
# - Space is used by the recursive call stack

# INTUITION:
# We can solve this using a bottom-up recursive approach. For any node:
# 1. If it's either p or q, that node could be the LCA
# 2. If p and q are in different subtrees, current node is the LCA
# 3. If p and q are in the same subtree, the LCA will be in that subtree
# This naturally leads to a post-order traversal where we process left and right
# subtrees before making a decision about the current node.

# ALGORITHM:
# 1. Base case: if root is null or equals either p or q, return root
# 2. Recursively search in left and right subtrees
# 3. After getting results from both subtrees:
#    - If both left and right return non-null, current node is LCA
#    - If one side is null, return the non-null side
#    - If both sides are null, return null

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Base case: if we hit null or find p or q
        if not root or root == p or root == q:
            return root
        
        # Recursively search in left and right subtrees
        left_result = self.lowestCommonAncestor(root.left, p, q)
        right_result = self.lowestCommonAncestor(root.right, p, q)
        
        # If both subtrees return a node, current node is the LCA
        if left_result and right_result:
            return root
            
        # If one subtree returns null, return the non-null result
        # This handles cases where:
        # 1. Both p and q are in the left subtree
        # 2. Both p and q are in the right subtree
        # 3. Neither p nor q was found in either subtree
        return left_result or right_result
