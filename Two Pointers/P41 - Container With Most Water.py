# Time Complexity: O(n)
# Space Complexity: O(1)

# INTUITION:
# This function calculates the maximum area of water that can be trapped between the vertical lines represented by the list 'height'.
# It utilizes a two-pointer approach where the two pointers start from the two ends of the list and move towards each other, 
# calculating the area at each step and updating the maximum area encountered so far.

# ALGORITHM:
# 1. Initialize 'ans' to 0 to store the maximum area.
# 2. Initialize two pointers 'l' and 'r' at the start and end of the list 'height' respectively.
# 3. Iterate until 'l' is less than 'r':
#    3.1 Calculate the area using the minimum height between 'height[l]' and 'height[r]' multiplied by the width 'r - l'.
#    3.2 Update 'ans' with the maximum of 'ans' and the calculated area.
#    3.3 Move the pointer with the smaller height towards the other pointer.
# 4. Return the maximum area 'ans'.

class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans = 0
        l, r = 0, len(height) - 1
        while l < r:
            if height[l] > height[r]:
                area = height[r] * (r - l)
                r -= 1
            else:
                area = height[l] * (r - l)
                l += 1
                
            ans = max(ans, area)
            
        return ans
