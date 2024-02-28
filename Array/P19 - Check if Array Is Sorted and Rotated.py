# Time Complexity: O(n)
# Space Complexity: O(n)

# INTUITION:
# The algorithm checks if the given list can be sorted by rotating it. It first finds the rotation index where the list is not in ascending order. Then, it rotates the list so that the rotation index becomes the beginning of the list. Finally, it checks if the rotated list is sorted in ascending order.

# ALGO:
# 1. Initialize rotationIndex to 0.
# 2. Find the rotation index:
#    2.1 Iterate through the list starting from the second element.
#        2.1.1 If the current element is less than the previous element,
#              set rotationIndex to the current index and break the loop.
# 3. Rotate the list:
#    3.1 Create a new list by concatenating the sublist from rotationIndex to the end of the list
#        with the sublist from the beginning of the list to rotationIndex.
# 4. Check if the rotated list is sorted:
#    4.1 Iterate through the rotated list starting from the second element.
#        4.1.1 If the current element is less than the previous element,
#              return False.
# 5. Return True if the rotated list is sorted.

# RETURN: True if the given list can be sorted by rotating it, False otherwise.


class Solution:
    def check(self, nums: List[int]) -> bool:
        rotationIndex = 0
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                rotationIndex = i
                break
        
        nums = nums[rotationIndex:]+nums[:rotationIndex]
        
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                return False
            
        return True
                
