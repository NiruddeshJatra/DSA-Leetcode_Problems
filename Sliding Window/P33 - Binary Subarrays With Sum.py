# Time Complexity: O(n)
# Space Complexity: O(1)

# INTUITION:
# This algorithm aims to find the count of subarrays with a sum equal to a given target 'k'. 
# It utilizes a helper function to calculate the number of subarrays whose sum is less than or equal to 'k' 
# and subtracts from it the count of subarrays whose sum is less than or equal to 'k-1', effectively getting 
# the count of subarrays whose sum is exactly 'k'.

# ALGO:
# 1. Initialize variables: left pointer 'l', answer 'ans', and total sum 'total' to 0.
# 2. Iterate through the array:
#    2.1 Add the current element to the total sum.
#    2.2 While the total sum is greater than the target 'k':
#        2.2.1 Subtract the leftmost element from the total sum and move the left pointer 'l' to the right.
#    2.3 Add the count of subarrays from 'l' to 'r' to the answer.
# 3. Return the difference between the count of subarrays with sum less than or equal to 'k' and 
#    the count of subarrays with sum less than or equal to 'k-1'.


class Solution:
    def numSubarraysWithSum(self, arr: List[int], k: int) -> int:
        def helper(k):
            if k < 0:
                return 0
            l, ans, total = 0, 0, 0
            for r in range(len(arr)):
                total += arr[r]
        
                while total >  k:
                    total -= arr[l]
                    l += 1
        
                ans += r-l+1
        
            return ans


        return helper(k) - helper(k-1)
