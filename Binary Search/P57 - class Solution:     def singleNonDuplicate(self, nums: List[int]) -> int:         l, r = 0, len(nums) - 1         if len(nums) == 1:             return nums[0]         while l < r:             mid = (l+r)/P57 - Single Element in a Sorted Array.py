# Time Complexity: O(log n)
# Space Complexity: O(1)

# INTUITION:
# The problem requires finding the single non-duplicate element in a sorted array where every other element appears exactly twice. 
# The goal is to use binary search to efficiently locate this unique element. The property of the array (being sorted and having pairs) allows us to use the position (even or odd index) to determine the direction of the search.

# ALGO:
# 1. INITIALIZE search boundaries:
#    - `l` (left) to 0
#    - `r` (right) to len(nums) - 1
# 2. CHECK for single element array:
#    - IF `len(nums)` is 1:
#        - RETURN `nums[0]` (only one element, which is the unique one)
# 3. PERFORM binary search:
#    - WHILE `l` is less than `r`:
#        - CALCULATE `mid` as the midpoint between `l` and `r`.
#        - DETERMINE if the unique element is in the left or right half:
#            - IF `mid` is even and `nums[mid]` equals `nums[mid+1]`:
#                - MOVE `l` to `mid + 1` (the unique element is in the right half).
#            - ELSE IF `mid` is odd and `nums[mid]` equals `nums[mid-1]`:
#                - MOVE `l` to `mid + 1` (the unique element is in the right half).
#            - ELSE:
#                - MOVE `r` to `mid` (the unique element is in the left half).
# 4. RETURN the unique element:
#    - RETURN `nums[l]` (after the loop, `l` will point to the unique element).

# CODE:
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        if len(nums) == 1:
            return nums[0]
        while l < r:
            mid = (l+r)//2
            if (mid % 2 == 0 and nums[mid] == nums[mid+1]) or (mid % 2 == 1 and nums[mid] == nums[mid-1]):
                l = mid + 1
            else:
                r = mid
        return nums[l]
