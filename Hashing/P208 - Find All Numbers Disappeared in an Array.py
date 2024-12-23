# Time Complexity: O(n), where n is the length of the input list `nums`.  
# - Counting the frequency of numbers takes O(n).  
# - Iterating through numbers from 1 to n takes O(n).  
# - Total time complexity is O(n).

# Space Complexity: O(n), where n is the length of `nums`.  
# - The `freq` Counter requires O(n) space.  
# - The output list `ans` also requires additional space proportional to the number of missing elements.

# INTUITION:  
# The task is to find all the numbers in the range [1, n] that are missing from the input array.  
# Using a frequency count helps us efficiently check which numbers are missing by comparing  
# the range [1, n] against the keys in the frequency dictionary.

# ALGO:  
# 1. Use a Counter to calculate the frequency of each number in `nums`.  
# 2. Iterate through the range [1, n] (inclusive).  
# 3. If a number is not present in the frequency dictionary, append it to the result list.  
# 4. Return the result list.

from collections import Counter
from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ans = []
        freq = Counter(nums)  # Count the frequency of each number in the array.
        
        # Iterate through numbers from 1 to n.
        for i in range(1, len(nums) + 1):
            if i not in freq:  # If a number is missing, add it to the result list.
                ans.append(i)
        
        return ans
