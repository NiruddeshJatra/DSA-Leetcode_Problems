# Time Complexity: O(log n), where n is the number of elements in the 'nums' list.
# Space Complexity: O(1), as the algorithm uses a constant amount of extra space.

# INTUITION:
# The problem requires finding the minimum element in a rotated sorted array. We can adapt binary search to efficiently 
# find the minimum element.
# 
# **Binary Search Approach**: Since the array is sorted (but possibly rotated), we can use binary search to efficiently 
# find the minimum element.
# 
# **Understanding Rotation**: The minimum element will be the point where the rotation starts. This element will be 
# smaller than its neighbors. By comparing the middle element with its adjacent elements, we can determine if the 
# rotation starts before or after the middle element.
# 
# **Updating the Minimum**: During the search, we update the minimum element encountered so far. At each step, we compare 
# the current element with the minimum element and update it if necessary.
# 
# **Determining Search Range**: Based on the comparison of the middle element with its neighbors, we adjust the search 
# range accordingly to continue the binary search process.
# 
# **Termination Condition**: Keep iterating until the search range is valid (i.e., until 'l <= r'). Once the search 
# range is exhausted, the minimum element will be stored in 'ans', which we return as the result.

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        ans = float('inf')
        while l <= r:
            mid = (l + r) // 2
            
            if nums[l] <= nums[mid]:
                ans = min(ans, nums[l])
                l = mid + 1
            else:
                ans = min(ans, nums[mid])
                r = mid - 1
        return ans
