# Time Complexity: O(n), where n is the length of the input list `nums`. 
# This is because we may have to traverse the list twice: once to find the first decreasing element and once to reverse part of the list.
# Space Complexity: O(1), as we are performing the operations in place and using only a constant amount of extra space.

# INTUITION:
# The goal of the "Next Permutation" problem is to rearrange numbers into the lexicographically next greater permutation. If no such permutation exists, we rearrange the numbers in ascending order (which is the smallest possible permutation). This can be done in a few steps:
# 1. Traverse the list from right to left and find the first element that breaks the descending order (this element is the one to be swapped).
# 2. Find the smallest element that is larger than the element found in step 1 and swap them.
# 3. Reverse the sublist to the right of the element found in step 1 to get the smallest possible arrangement.

# ALGO:
# 1. Start from the right end of the list and look for the first element (`nums[i-1]`) that is smaller than its next element (`nums[i]`). This marks the position where we need to swap to get the next permutation.
# 2. If no such element exists (i.e., the entire list is in descending order), reverse the list and return.
# 3. Find the element (`nums[j]`) that is the smallest element larger than `nums[i-1]` and swap these two elements.
# 4. Reverse the sublist starting from `i` to the end of the list to get the next smallest permutation.

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Step 1: Find the first decreasing element from the right
        i = j = len(nums) - 1
        while i > 0 and nums[i-1] >= nums[i]:
            i -= 1
        
        # Step 2: If no such element exists, reverse the list
        if i == 0:
            nums.reverse()
            return
        
        # Step 3: Find the element just larger than nums[i-1]
        while nums[j] <= nums[i-1]:
            j -= 1
        
        # Step 4: Swap nums[i-1] with nums[j]
        nums[i-1], nums[j] = nums[j], nums[i-1]
        
        # Step 5: Reverse the sublist starting from i to the end
        nums[i:] = nums[len(nums)-1:i-1:-1]
