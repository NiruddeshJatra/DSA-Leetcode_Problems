from sys import *
from collections import *
from math import *
from typing import List

class Solution:
   def findNumberOfLIS(self, nums: List[int]) -> int:
       # Time Complexity:
       # - O(n²) where n is the length of the input array
       # - We use nested loops, with the outer loop running n times and inner loop running up to i times
       
       # Space Complexity:
       # - O(n) for the dp array and count array that track lengths and counts of LIS
       
       # INTUITION:
       # This problem extends the classic Longest Increasing Subsequence (LIS) by asking for the count of 
       # such subsequences. We need to track both the length of the LIS ending at each position and the 
       # number of ways to form such subsequences.
       #
       # For example, with array [1, 3, 5, 4, 7]:
       # - For index 0 (value 1): dp[0] = 1, cnt[0] = 1 (just the single element)
       # - For index 1 (value 3): dp[1] = 2 (can extend from index 0), cnt[1] = 1 (only one way)
       # - For index 2 (value 5): dp[2] = 3 (can extend from index 1), cnt[2] = 1 (only one way)
       # - For index 3 (value 4): dp[3] = 3 (can extend from index 1), cnt[3] = 1 (only one way)
       # - For index 4 (value 7): dp[4] = 4 (can extend from index 2 or 3), cnt[4] = 2 (two ways)
       #
       # The maximum length is 4, and we have 2 subsequences of this length.
       
       # ALGO:
       # 1. Initialize two arrays:
       #    a. dp[i] represents the length of the LIS ending at index i
       #    b. cnt[i] represents the number of LIS of length dp[i] ending at index i
       # 2. Initialize maxLength to track the maximum LIS length found
       # 3. For each position i, check all previous positions j:
       #    a. If nums[i] > nums[j], we can potentially extend the LIS ending at j
       #    b. If extending gives a longer subsequence, update dp[i] and set cnt[i] to cnt[j]
       #    c. If extending gives a subsequence of the same length as current dp[i], add cnt[j] to cnt[i]
       # 4. Update maxLength to the maximum dp value found
       # 5. Sum the counts of all positions that have LIS equal to maxLength
       # 6. Return the total count
       
       n = len(nums)
       
       # dp[i] represents the length of the LIS ending at index i
       dp = [1] * n
       
       # cnt[i] represents the number of LIS of length dp[i] ending at index i
       count = [1] * n
       
       # Track the maximum LIS length
       maxLength = 1
       
       # Fill the dp and count arrays
       for i in range(n):
           for j in range(i):
               # If the current element can extend the LIS ending at index j
               if nums[i] > nums[j]:
                   # Case 1: We found a longer LIS ending at index i
                   if dp[j] + 1 > dp[i]:
                       dp[i] = dp[j] + 1
                       count[i] = count[j]  # Reset count to match the count at j
                       maxLength = max(maxLength, dp[i])  # Update max length if needed
                   
                   # Case 2: We found another way to form an LIS of the same length
                   elif dp[j] + 1 == dp[i]:
                       count[i] += count[j]  # Add the count from j to our current count
       
       # Sum the counts for all positions that have LIS equal to maxLength
       totalCount = 0
       for i in range(n):
           if dp[i] == maxLength:
               totalCount += count[i]
       
       return totalCount
