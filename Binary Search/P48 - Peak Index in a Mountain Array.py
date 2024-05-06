# Time Complexity: O(log n), where n is the number of elements in the 'arr' list.
# Space Complexity: O(1), as the algorithm uses a constant amount of extra space.

# INTUITION:
# The problem asks to find the peak index in a mountain array. A mountain array is defined as an array that:
# - Has at least three elements.
# - Contains an index 'i' such that arr[0] < arr[1] < ... < arr[i-1] < arr[i] > arr[i+1] > ... > arr[n-1].
# We can use binary search to efficiently find the peak index.

# ALGO:
# 1. Initialize pointers 'l' and 'r' to the start and end of the 'arr' list, respectively.
# 2. Perform binary search:
#     2.1 If the middle element is greater than its neighbors, return its index.
#     2.2 If the middle element is smaller than its right neighbor, set 'l' to mid + 1.
#     2.3 If the middle element is smaller than its left neighbor, set 'r' to mid - 1.

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l, r = 0, len(arr) - 1
        while l <= r:
            mid = (l + r) // 2
            if arr[mid] > arr[mid - 1] and arr[mid] > arr[mid + 1]:
                return mid
            elif arr[mid] < arr[mid + 1]:
                l = mid + 1
            else:
                r = mid - 1
