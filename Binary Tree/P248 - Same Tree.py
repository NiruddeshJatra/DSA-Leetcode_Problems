# Time Complexity:
# - O(min(N, M)), where N and M are the number of nodes in trees p and q respectively
# - We traverse both trees simultaneously until we find a mismatch
# - In best case we find mismatch early, in worst case we check all nodes

# Space Complexity:
# - O(min(H1, H2)), where H1 and H2 are heights of trees p and q
# - Space used by the recursive call stack
# - In worst case (skewed trees), this becomes O(min(N, M))

# INTUITION:
# Two binary trees are identical if they have the same structure and same values.
# Using recursive DFS is ideal because:
# 1. We can compare both structure and values simultaneously
# 2. Trees are recursive structures by nature
# 3. Early termination when we find any mismatch
# 4. Clean and intuitive base cases for null nodes

# ALGO:
# 1. Base cases:
#    - Both nodes null: return True (empty trees are same)
#    - One node null or values different: return False (structure/value mismatch)
# 2. Recursive case:
#    - Both current nodes match
#    - Recursively check if left subtrees are same
#    - Recursively check if right subtrees are same
#    - Trees are same only if both subtrees are same

class Solution:
   def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
       # Base case 1: both nodes are null (empty trees are same)
       if not p and not q:
           return True
       
       # Base case 2: one node is null or values differ
       # (structure mismatch or value mismatch)
       if not p or not q or p.val != q.val:
           return False
       
       # Recursive case: current nodes match, check subtrees
       return (self.isSameTree(p.left, q.left) and  # Check left subtrees
               self.isSameTree(p.right, q.right))    # Check right subtrees
