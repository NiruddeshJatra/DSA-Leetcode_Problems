# Time Complexity: O(n), where n is the length of the input list 'nums'.
# Space Complexity: O(1)

# INTUITION:
# The code aims to find the maximum product of a contiguous subarray within the input 
# list 'nums'. It uses three variables: 'prefix', 'suffix', and 'res'. 'prefix' and 
# 'suffix' keep track of the product of elements from the beginning and end of the array, 
# respectively. 'res' stores the maximum product found so far. It iterates through the 
# elements of 'nums', updating 'prefix' and 'suffix' for each element and updating 'res' 
# with the maximum of 'res', 'prefix', and 'suffix' in each iteration.

# ALGO:
# 1. Initialize variables: 'prefix' and 'suffix' to keep track of the product of 
#    elements from the beginning and end of the array, and 'res' to store the maximum 
#    product found so far. Set 'res' to a very small number to handle negative input values.
# 2. Iterate through each element 'i' in the input list 'nums':
#    2.1. If 'prefix' becomes zero, reset it to 1 to start a new subarray.
#    2.2. If 'suffix' becomes zero, reset it to 1 to start a new subarray.
#    2.3. Update 'prefix' by multiplying it with the current element.
#    2.4. Update 'suffix' by multiplying it with the element at position 'n - i - 1'.
#    2.5. Update 'res' with the maximum of 'res', 'prefix', and 'suffix'.
# 3. Return 'res' as the result, which represents the maximum product of a contiguous 
#    subarray within 'nums'.

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prefix, suffix, res = 1, 1, -10 ** 18  # Initialize variables.
        n = len(nums)
        for i in range(n):
            if prefix == 0:  # Reset prefix if it becomes zero.
                prefix = 1
            if suffix == 0:  # Reset suffix if it becomes zero.
                suffix = 1
            prefix *= nums[i]  # Update prefix by multiplying with the current element.
            suffix *= nums[n - i - 1]  # Update suffix by multiplying with the element at the end.
            res = max(res, prefix, suffix)  # Update maximum product.
        return res  # Return the maximum product found.
