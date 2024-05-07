# Time Complexity: O(log n), where n is the number of elements in the 'nums' list.
# Space Complexity: O(1), as the algorithm uses a constant amount of extra space.

# INTUITION:
# The problem involves searching for a target element in a rotated sorted array. The approach here is to adapt 
# binary search to handle the rotation aspect efficiently.
# 
# **Binary Search Approach**: Since the array is sorted (but possibly rotated), we can still utilize binary search.
# 
# **Handling Rotation**: Divide the array into halves. At least one half must be sorted. This helps determine 
# which half to search in based on the target and the middle element.
# 
# **Comparing with the Mid Element**: Compare the target with the middle element. There are three possibilities:
#     - If the mid element matches the target, return True, as we have found the target.
#     - If the left half of the array is sorted: Check if the target lies within the range of the left half.
#       If it does, adjust the search range accordingly; otherwise, search in the right half.
#     - If the right half of the array is sorted: Similar to the previous case, check if the target lies within 
#       the range of the right half. If it does, adjust the search range accordingly; otherwise, search in the left half.
# 
# **Updating the Search Range**: Based on the comparison of the target with the mid element and the sorted halves, 
# update the search range accordingly to continue the binary search process.
# 
# **Termination Condition**: Keep iterating until the search range is valid (i.e., until 'l <= r'). If the target 
# is found, return True; otherwise, return False indicating that the target is not in the array.

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return True
            elif nums[l] == nums[mid]:
                l += 1
            elif nums[l] < nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        return False
