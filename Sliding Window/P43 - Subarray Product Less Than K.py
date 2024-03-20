# Time Complexity: O(n)
# Space Complexity: O(1)

# INTUITION:
# This function counts the number of contiguous subarrays in the array 'nums' where the product of all elements 
# is less than 'k'. It uses a sliding window approach to maintain a product less than 'k' while expanding 
# the window from left to right.

# ALGORITHM:
# 1. Initialize a left pointer 'l' at 0, answer 'ans' to 0, and product 'product' to 1.
# 2. Iterate through the array 'nums' using a right pointer 'r':
#    2.1 Multiply the product with the element at 'nums[r]'.
#    2.2 While the product is greater than or equal to 'k' and 'l' is less than or equal to 'r':
#        2.2.1 Divide the product by the element at 'nums[l]'.
#        2.2.2 Move the left pointer 'l' to the right.
#    2.3 Calculate the length of the current subarray as 'r - l + 1'.
#    2.4 Add the length of the current subarray to 'ans'.
# 3. Return 'ans', which represents the total count of contiguous subarrays with a product less than 'k'.

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        l, ans, product = 0, 0, 1
        for r in range(len(nums)):
            product *= nums[r]
            
            while product >= k and l <= r:
                product //= nums[l]
                l += 1
                
            subarrLen = (r - l + 1)
            ans += subarrLen
            
        return ans
