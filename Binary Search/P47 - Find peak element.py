# Time Complexity: O(log n), where n is the number of elements in the 'nums' list.
# Space Complexity: O(1), as the algorithm uses a constant amount of extra space.

# INTUITION:
# The problem asks to find a peak element in an array. A peak element is an element that is greater than its neighbors. 
# We can use binary search to efficiently find a peak element.

# ALGO:
# 1. Check if the first or last element is a peak, if so, return its index.
# 2. Initialize pointers 'l' and 'r' to the start and end of the 'nums' list, respectively.
# 3. Perform binary search:
#     3.1 If the middle element is greater than its neighbors, return its index.
#     3.2 If the middle element is smaller than its right neighbor, set 'l' to mid + 1.
#     3.3 If the middle element is smaller than its left neighbor, set 'r' to mid - 1.

# RETURN -1 if no peak is found.

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1 or nums[0] > nums[1]:
            return 0
        if nums[len(nums) - 1] > nums[len(nums) - 2]:
            return len(nums) - 1
            
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                return mid
            elif nums[mid] < nums[mid + 1]:
                l = mid + 1
            else:
                r = mid - 1
        
        return -1
