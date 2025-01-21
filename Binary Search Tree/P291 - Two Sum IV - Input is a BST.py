# Time Complexity:
# - O(N) where N is number of nodes in BST
# - Each node is pushed/popped at most twice (once in each stack)
# - Building initial stacks takes O(H) where H is height of tree

# Space Complexity:
# - O(H) where H is height of BST for the two stacks
# - Each stack stores at most one path from root to leaf
# - In balanced BST: O(log N)
# - In skewed BST: O(N) worst case

# INTUITION:
# Using two-pointer technique with BST iterator pattern:
# - One iterator from left (ascending)
# - One iterator from right (descending)
# This allows us to efficiently search for pairs summing to target
# without storing all values in memory.

# ALGO:
# 1. Initialize two stacks:
#    - minStack for ascending iterator (leftmost path)
#    - maxStack for descending iterator (rightmost path)
# 2. Get initial values (smallest and largest)
# 3. While left < right:
#    - If sum equals target: return True
#    - If sum < target: move left pointer up (get next larger)
#    - If sum > target: move right pointer down (get next smaller)
# 4. Return False if no pair found

class Solution:
   def findTarget(self, root: Optional[TreeNode], targetSum: int) -> bool:
       def pushLeftPath(node: TreeNode) -> None:
           while node:
               ascendingStack.append(node)
               node = node.left
               
       def pushRightPath(node: TreeNode) -> None:
           while node:
               descendingStack.append(node)
               node = node.right
               
       def getNextSmaller() -> int:
           node = descendingStack.pop()
           pushRightPath(node.left)
           return node.val
           
       def getNextLarger() -> int:
           node = ascendingStack.pop()
           pushLeftPath(node.right)
           return node.val
           
       # Initialize stacks for two-pointer approach
       ascendingStack = []   # For getting values in ascending order
       descendingStack = []  # For getting values in descending order
       
       # Build initial stacks
       pushLeftPath(root)
       pushRightPath(root)
       
       # Get initial values
       leftValue = getNextLarger()
       rightValue = getNextSmaller()
       
       # Two-pointer search
       while leftValue < rightValue:
           currentSum = leftValue + rightValue
           
           if currentSum == targetSum:
               return True
           elif currentSum < targetSum:
               if not ascendingStack:  # No more larger values
                   break
               leftValue = getNextLarger()
           else:
               if not descendingStack:  # No more smaller values
                   break
               rightValue = getNextSmaller()
               
       return False
