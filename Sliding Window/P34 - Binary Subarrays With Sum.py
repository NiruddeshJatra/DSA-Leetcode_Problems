# Time Complexity: O(n)
# Space Complexity: O(1)

# INTUITION:
# This function calculates the number of subarrays in 'arr' containing at most 'k' distinct odd numbers.

# ALGO:
# 1. Initialize variables: left pointer 'l', answer 'ans', and total count of odd numbers 'total' to 0.
# 2. Iterate through the array:
#    2.1 If the current element is odd, increment the count of odd numbers 'total'.
#    2.2 While the total count of odd numbers exceeds 'k':
#        2.2.1 If the leftmost element is odd, decrement the count of odd numbers 'total'.
#        2.2.2 Move the left pointer 'l' to the right.
#    2.3 Add the count of subarrays from 'l' to 'r' to the answer.
# 3. Return the difference between the count of subarrays with at most 'k' distinct odd numbers 
#    and the count of subarrays with at most 'k-1' distinct odd numbers.

from typing import List

def distinctSubKOdds(arr: List[int], k: int) -> int:
    def helper(k):
        if k < 0:
            return 0
        l, ans, total = 0, 0, 0
        for r in range(len(arr)):
            if arr[r] % 2 == 1:
                total += 1
        
            while total > k:
                if arr[l] % 2 == 1:
                    total -= 1
                l += 1
        
            ans += r - l + 1
        
        return ans


    return helper(k) - helper(k - 1)
