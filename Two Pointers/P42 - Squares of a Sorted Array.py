# Time Complexity: O(n)
# Space Complexity: O(n)

# INTUITION:
# This function calculates the squares of the numbers in the input list 'nums' and returns them in sorted order.
# It utilizes a two-pointer approach where the two pointers start from the two ends of the list, comparing the 
# absolute values of the numbers at the two pointers. The larger absolute value is squared and added to the result 
# list, and the respective pointer is moved inward. Finally, the result list is reversed to obtain the sorted order.

# ALGORITHM:
# 1. Initialize two pointers 'l' and 'r' at the start and end of the list 'nums' respectively.
# 2. Initialize an empty list 'ans' to store the squared numbers in sorted order.
# 3. Iterate while 'l' is less than or equal to 'r':
#    3.1 If the absolute value of the number at 'nums[l]' is greater than the absolute value of the number at 'nums[r]':
#        3.1.1 Square the number at 'nums[l]' and append it to 'ans'.
#        3.1.2 Increment 'l'.
#    3.2 Else, square the number at 'nums[r]' and append it to 'ans'.
#        3.2.1 Decrement 'r'.
# 4. Return the reversed 'ans' list to obtain the squared numbers in sorted order.

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l, r = 0, len(nums) - 1
        ans = []
        
        while l <= r:
            if abs(nums[l]) > abs(nums[r]):
                ans.append(nums[l] * nums[l])
                l += 1
            else:
                ans.append(nums[r] * nums[r])
                r -= 1
        
        return ans[::-1]
