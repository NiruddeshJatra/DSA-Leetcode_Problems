# Time Complexity: 
# - O(N^2) in the worst case, where N is the length of the input array
# - Finding the maximum element takes O(N) time
# - Recursively creating subarrays also contributes to quadratic time complexity

# Space Complexity:
# - O(N) for the recursion stack in the worst case of a skewed tree
# - O(log N) average case for a balanced tree

# INTUITION:
# The problem requires constructing a maximum binary tree where:
# - The root is the maximum element in the array
# - Left subtree is constructed from elements to the left of the max element
# - Right subtree is constructed from elements to the right of the max element
# This creates a unique tree where each node represents the maximum of its subarray

# ALGO:
# 1. If the input array is empty, return None
# 2. Find the maximum element in the current array
# 3. Create a new tree node with the maximum element
# 4. Recursively construct left subtree with elements before the max
# 5. Recursively construct right subtree with elements after the max
# 6. Return the root node

class Solution:
   def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
       # Base case: empty array returns None
       if not nums:
           return None

       # Find the maximum value and its index
       maxValue = max(nums)
       maxIndex = nums.index(maxValue)

       # Create root node with maximum value
       root = TreeNode(maxValue)

       # Recursively construct left and right subtrees
       root.left = self.constructMaximumBinaryTree(nums[:maxIndex])
       root.right = self.constructMaximumBinaryTree(nums[maxIndex+1:])

       return root
