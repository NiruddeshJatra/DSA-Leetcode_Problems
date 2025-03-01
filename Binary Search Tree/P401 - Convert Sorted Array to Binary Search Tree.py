# Time Complexity:
# - O(n), where n is the length of the input array.
# - We visit each element in the array exactly once to create a tree node.

# Space Complexity:
# - O(log n) for the recursion stack in a balanced tree.
# - The height of the balanced BST will be log n, which determines the maximum recursion depth.

# INTUITION:
# To create a height-balanced BST from a sorted array, we need to ensure that there are roughly
# equal numbers of elements in the left and right subtrees. The middle element of the array is the 
# perfect candidate for the root node, as it divides the array into two equal halves.
#
# This approach is similar to a binary search algorithm - we recursively find the middle element
# of each subarray to use as the root of each subtree. This naturally results in a balanced tree
# because we're always splitting the array at its midpoint.
#
# For example, with [1,2,3,4,5,6,7]:
# - The middle element 4 becomes the root
# - [1,2,3] forms the left subtree with 2 as its root
# - [5,6,7] forms the right subtree with 6 as its root
# - And so on recursively

# ALGO:
# 1. Define a recursive helper function that takes the left and right boundaries of the current subarray.
# 2. Find the middle element and create a new tree node with that value.
# 3. Recursively build the left subtree using the elements before the middle.
# 4. Recursively build the right subtree using the elements after the middle.
# 5. Return the node created in step 2, now with its left and right children set.
# 6. Handle the base case: if left > right, return None (empty subtree).

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
   def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
       def buildBST(leftIdx, rightIdx):
           # Base case: if the subarray is empty, return None
           if leftIdx > rightIdx:
               return None
           
           # Find the middle element to use as the root
           middleIdx = (leftIdx + rightIdx) // 2
           
           # Create a new node with the middle element's value
           currentNode = TreeNode(nums[middleIdx])
           
           # Recursively build left and right subtrees
           currentNode.left = buildBST(leftIdx, middleIdx - 1)
           currentNode.right = buildBST(middleIdx + 1, rightIdx)
           
           return currentNode

       # Start the recursive construction with the full array
       return buildBST(0, len(nums) - 1)
