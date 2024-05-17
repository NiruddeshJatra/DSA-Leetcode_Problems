# Time Complexity: O(log n)
# Space Complexity: O(1)

# INTUITION:
# The goal is to find the starting and ending positions of a given target value within a sorted array `nums`.
# We need to find two indices: 
# 1. The first occurrence of the target (left boundary).
# 2. The last occurrence of the target (right boundary).
# Given that the array is sorted, binary search is an efficient method to locate these boundaries.

# ALGO:
# 1. INITIALIZE search boundaries `l` and `r` to 0 and len(nums)-1, respectively.
# 2. FIND the left boundary (first occurrence of target):
#    - WHILE `l` is less than `r`:
#        - CALCULATE `mid` as the midpoint between `l` and `r`.
#        - IF `nums[mid]` is less than `target`:
#            - MOVE `l` to `mid + 1`.
#        - ELSE:
#            - MOVE `r` to `mid`.
# 3. CHECK if the target exists in the array:
#    - IF `nums` is empty or `nums[r]` is not equal to `target`:
#        - RETURN [-1, -1] (target not found).
#    - ELSE:
#        - STORE `r` in `left` (left boundary found).
# 4. FIND the right boundary (last occurrence of target):
#    - RESET `r` to len(nums) - 1.
#    - WHILE `l` is less than `r`:
#        - CALCULATE `mid` as the midpoint between `l` and `r`, adjusted by adding 1 to favor the right half.
#        - IF `nums[mid]` is less than or equal to `target`:
#            - MOVE `l` to `mid`.
#        - ELSE:
#            - MOVE `r` to `mid - 1`.
#    - STORE `l` in `right` (right boundary found).
# 5. RETURN the found boundaries `[left, right]`.

# CODE:
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums)-1
        while l < r:
            mid = (l+r)//2
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid

        if len(nums) == 0 or nums[r] != target:
            return [-1, -1]

        left = r
        r = len(nums) - 1
        while l < r:
            mid = (l+r)//2 + 1
            if nums[mid] <= target:
                l = mid
            else:
                r = mid - 1

        right = l
        return [left, right]
