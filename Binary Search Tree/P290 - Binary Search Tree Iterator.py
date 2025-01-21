# Time Complexity:
# - Constructor: O(H) where H is height of tree to push leftmost path
# - next(): Amortized O(1). While each call might take O(H) to push all left nodes,
#   overall each node is pushed and popped exactly once
# - hasNext(): O(1) to check stack length

# Space Complexity:
# - O(H) where H is height of BST
# - Stack stores at most one path from root to leaf
# - In balanced BST: O(log N)
# - In skewed BST: O(N) worst case

# INTUITION:
# The key insight is that inorder traversal of BST gives nodes in sorted order.
# Instead of doing full traversal upfront, we can:
# 1. Store left path from root initially
# 2. When next() is called, pop top node and push left path of its right child
# This simulates inorder traversal one node at a time with optimal space usage.

# ALGO:
# Constructor:
# 1. Initialize empty stack
# 2. Push all nodes in leftmost path from root
#
# next():
# 1. Pop top node from stack (next smallest value)
# 2. Push all nodes in leftmost path from popped node's right child
# 3. Return popped node's value
#
# hasNext():
# 1. Return true if stack is non-empty

class TreeNode:
   def __init__(self, val=0, left=None, right=None):
       self.val = val
       self.left = left
       self.right = right

class BSTIterator:
   def __init__(self, root: Optional[TreeNode]):
       self.nodeStack = []
       self.pushLeftPath(root)

   def pushLeftPath(self, currentNode: Optional[TreeNode]) -> None:
       # Push all nodes in leftmost path starting from currentNode
       while currentNode:
           self.nodeStack.append(currentNode)
           currentNode = currentNode.left

   def next(self) -> int:
       # Pop the next smallest value
       nextNode = self.nodeStack.pop()
       
       # Push left path of right subtree
       self.pushLeftPath(nextNode.right)
       
       return nextNode.val

   def hasNext(self) -> bool:
       return len(self.nodeStack) > 0
