# Time Complexity: O(n log n), where n is the number of elements in the list 'nums'. Sorting dominates the time complexity, and sorting has a time complexity of O(n log n).
# Space Complexity: O(n), as we use extra space for the sorted list and the string representations of the numbers.

# INTUITION:
# The problem requires us to form the largest number possible by concatenating integers from the list. 
# To solve this, we treat the numbers as strings and sort them in a custom order to achieve the largest concatenation result.
#
# **Key Insight**: When concatenating two numbers as strings, the order in which they are combined can produce different results. 
# For example, for numbers 3 and 30, "330" is larger than "303", so 3 should come before 30 in the final result.
#
# **Custom Sorting**: The challenge is how to sort the string representations of the numbers in such a way that the resulting concatenated string is the largest possible. 
# To achieve this, we need to define a custom sorting function. In this case, we use `lambda x: x*10` as a custom sorting key to ensure that strings are extended for comparison.
# 
# **Handling Special Cases**: If the largest element is "0", then the entire result is "0" because numbers with leading zeros are not allowed in the output.

# ALGO:
# 1. **Convert Numbers to Strings**: 
#    - Convert the list of integers into strings so that we can sort them based on string concatenation behavior.
# 2. **Sort Strings with Custom Key**:
#    - Sort the string versions of the numbers using a custom key `lambda x: x*10` to ensure that numbers are compared in a meaningful way for concatenation.
#    - The reason for multiplying each string by 10 is to make it long enough for comparison, ensuring that we account for differences in length when comparing.
# 3. **Handle the Edge Case of Leading Zeros**:
#    - If the largest number is "0", return "0" because a number starting with multiple zeros should just be "0".
# 4. **Join and Return**:
#    - Join the sorted numbers into a single string and return it as the result.

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # Step 1: Convert numbers to strings
        strNums = map(str, nums)
        
        # Step 2: Sort the numbers using the custom lambda key
        ans = sorted(strNums, key=lambda x: x*10, reverse=True)
        
        # Step 3: Handle the case where the largest number is "0"
        if ans[0] == "0":
            return "0"
        
        # Step 4: Join the sorted numbers to form the largest number
        return "".join(ans)
