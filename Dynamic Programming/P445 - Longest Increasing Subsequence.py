from sys import *
from collections import *
from math import *
from bisect import bisect_left
from typing import List

class Solution:
   def lengthOfLIS(self, nums: List[int]) -> int:
       # Time Complexity:
       # - O(n²) where n is the length of the input array
       # - We use nested loops, with the outer loop running n times and inner loop running up to i times
       
       # Space Complexity:
       # - O(n) for the dp array that stores the length of LIS ending at each index
       
       # INTUITION:
       # This recursive solution uses memoization to avoid redundant calculations. The function f(i, prev)
       # computes the length of the LIS starting from index i, with prev being the index of the
       # previously selected element (or -1 if no element has been selected yet).
       #
       # For each element at index i, we have two choices:
       # 1. Skip the current element (notTake)
       # 2. Take the current element if it's greater than the previous element (take)
       #
       # The maximum of these two options gives us the optimal solution.
       #
       # ALGO:
       # 1. Define a recursive function f(i, prev) that returns the length of LIS starting from index i
       # 2. Base case: If i reaches the end of the array, return 0
       # 3. Check if the result for the current state is already calculated
       # 4. Compute the result for not taking the current element
       # 5. If the current element is greater than the previous element, compute the result for taking it
       # 6. Store and return the maximum of take and notTake options
       # 7. The answer is f(0, -1) which represents starting from the beginning with no previous element
       
       def f(i, prev):
           # Base case: reached the end of the array
           if i == n:
               return 0

           # Check if result is already calculated
           if dp[prev + 1] != -1:
               return dp[prev + 1]

           # Don't take the current element
           notTake = f(i + 1, prev)
           
           # Take the current element if it's greater than the previous element
           take = 0
           if prev == -1 or nums[i] > nums[prev]:
               take = 1 + f(i + 1, i)

           # Memoize and return the result
           dp[prev + 1] = max(take, notTake)
           return dp[prev + 1]

       n = len(nums)
       # dp[prev+1] represents the length of LIS starting from index 0 with previous element at index prev
       dp = [-1] * (n + 1)
       return f(0, -1)

   def lengthOfLIS(self, nums: List[int]) -> int:
       # Time Complexity:
       # - O(n²) where n is the length of the input array
       # - We use nested loops, with the outer loop running n times and inner loop running up to i times
       
       # Space Complexity:
       # - O(n) for the dp array that stores the length of LIS ending at each index
       
       # INTUITION:
       # This is a bottom-up dynamic programming approach. For each position i, we consider all previous
       # positions j < i and check if the element at position i can extend the subsequence ending at j.
       #
       # For example, with array [10, 9, 2, 5, 3, 7, 101, 18]:
       # - dp[0] = 1 (just the element 10)
       # - dp[1] = 1 (just the element 9, can't extend from 10 since 9 < 10)
       # - dp[2] = 1 (just the element 2, can't extend from previous elements)
       # - dp[3] = 2 (can extend from index 2: [2, 5])
       # And so on...
       
       # ALGO:
       # 1. Initialize a dp array where dp[i] represents the length of LIS ending at index i
       # 2. Set all values in dp to 1 (each element by itself forms an LIS of length 1)
       # 3. For each position i, check all previous positions j:
       #    a. If nums[i] > nums[j], we can extend the LIS ending at j
       #    b. Update dp[i] to max(dp[i], dp[j] + 1)
       # 4. Keep track of the maximum LIS length found
       # 5. Return the maximum length
       
       n = len(nums)
       # Initialize maximum LIS length
       maxLength = 1
       # dp[i] represents the length of LIS ending at index i
       dp = [1] * n

       for i in range(n):
           for j in range(i):
               if nums[i] > nums[j]:
                   dp[i] = max(dp[i], dp[j] + 1)
                   maxLength = max(maxLength, dp[i])

       return maxLength

   def lengthOfLIS(self, nums: List[int]) -> int:
       # Time Complexity:
       # - O(n log n) where n is the length of the input array
       # - We iterate through the array once, and each binary search operation takes O(log n) time
       
       # Space Complexity:
       # - O(n) for the sub array that stores the elements of the subsequence
       
       # INTUITION:
       # This optimized approach uses a technique called "patience sort". We maintain a sorted array 'sub'
       # where sub[i] represents the smallest tail element of all increasing subsequences of length i+1.
       #
       # For example, with array [10, 9, 2, 5, 3, 7, 101, 18]:
       # - Start with empty sub []
       # - Process 10: sub = [10]
       # - Process 9: sub = [9] (replace 10 with 9 as it's smaller)
       # - Process 2: sub = [2] (replace 9 with 2)
       # - Process 5: sub = [2, 5] (append 5 as it's larger than 2)
       # - Process 3: sub = [2, 3] (replace 5 with 3 as it's smaller)
       # - Process 7: sub = [2, 3, 7] (append 7)
       # - Process 101: sub = [2, 3, 7, 101] (append 101)
       # - Process 18: sub = [2, 3, 7, 18] (replace 101 with 18)
       # The length of sub (4) is the length of the LIS.
       
       # ALGO:
       # 1. Initialize an empty array 'sub' to store the subsequence
       # 2. For each number in the input array:
       #    a. If sub is empty or num is greater than the last element in sub, append num to sub
       #    b. Otherwise, find the position where num would be inserted to maintain the sorted order
       #       and replace the element at that position with num
       # 3. The length of 'sub' at the end is the length of the LIS
       
       n = len(nums)
       sub = []

       for num in nums:
           if not sub or sub[-1] < num:
               # If the current number is greater than all elements in sub,
               # it extends the longest subsequence
               sub.append(num)
           else:
               # Find the position where num would be inserted in sub
               # and replace the element at that position
               i = bisect_left(sub, num)
               sub[i] = num

       return len(sub)
