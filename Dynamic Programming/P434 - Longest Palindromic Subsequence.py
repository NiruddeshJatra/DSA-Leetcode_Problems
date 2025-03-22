# Time Complexity:
# - O(N²), where N is the length of string s.
# - In all implementations, we fill a table of size N*N.

# Space Complexity:
# - Recursive (Memoization): O(N²) for the dp array + O(N) for the recursion stack
# - Iterative (Tabulation): O(N²) for the dp array
# - Space-optimized: O(N) as we only keep track of the previous row

# INTUITION:
# The key insight is that the longest palindromic subsequence (LPS) is the same as the longest common subsequence (LCS)
# between the string and its reverse! This works because:
# 1. A palindrome reads the same forward and backward
# 2. If we find characters that are common between the string and its reverse, they must form a palindrome
#
# Example:
# For string "bbbab", the reverse is "babbb".
# The LCS between these two strings is "bbbb", which is indeed the longest palindromic subsequence of "bbbab".
#
# Why this works:
# If a character is part of the LPS, it must match with its corresponding character from the other end in the original string.
# This is exactly what we're finding when we compute the LCS between the string and its reverse.

# ALGO:
# The solution is presented in three different implementations:
#
# 1. Top-down (Memoization):
#    a. Reverse the input string to get text2
#    b. Find the LCS between the original string (text1) and its reverse (text2) using recursion with memoization
#
# 2. Bottom-up (Tabulation):
#    a. Reverse the input string to get text2
#    b. Build a 2D table for the LCS between text1 and text2
#    c. Fill the table iteratively
#
# 3. Space-optimized:
#    a. Same approach as #2, but using only two rows (prev and cur) instead of the entire 2D table
#    b. After processing each row, update prev = cur

class Solution:
   # Top-down approach using memoization
   def longestPalindromeSubseq(self, s: str) -> int:
       def findLCS(i, j):
           # Base case: if we've gone beyond the beginning of either string
           if i < 0 or j < 0:
               return 0

           # If result already computed, return from memo
           if dp[i][j] != -1:
               return dp[i][j]

           # If characters match, include this character in LCS
           if text1[i] == text2[j]:
               dp[i][j] = 1 + findLCS(i-1, j-1)
           else:
               # Characters don't match, take max of two possible subproblems
               dp[i][j] = max(findLCS(i-1, j), findLCS(i, j-1))

           return dp[i][j]

       # Original string and its reverse
       text1, text2 = s, s[::-1]
       m, n = len(text1), len(text2)
       dp = [[-1] * n for _ in range(m)]  # Initialize memoization table
       return findLCS(m-1, n-1)

   # Bottom-up approach using tabulation
   def longestPalindromeSubseq(self, s: str) -> int:
       # Original string and its reverse
       text1, text2 = s, s[::-1]
       m, n = len(text1), len(text2)
       dp = [[0] * (n + 1) for _ in range(m + 1)]

       for i in range(1, m+1):
           for j in range(1, n+1):
               # Characters match (note the index adjustment)
               if text1[i-1] == text2[j-1]:
                   dp[i][j] = 1 + dp[i-1][j-1]
               else:
                   # Characters don't match, take max of two possible subproblems
                   dp[i][j] = max(dp[i-1][j], dp[i][j-1])

       return dp[m][n]  # Bottom-right cell contains the length of LCS which is our LPS

   # Space-optimized approach
   def longestPalindromeSubseq(self, s: str) -> int:
       # Original string and its reverse
       text1, text2 = s, s[::-1]
       m, n = len(text1), len(text2)
       prevRow = [0] * (n + 1)

       for i in range(1, m+1):
           currentRow = [0] * (n + 1)
           for j in range(1, n+1):
               if text1[i-1] == text2[j-1]:
                   currentRow[j] = 1 + prevRow[j-1]
               else:
                   currentRow[j] = max(prevRow[j], currentRow[j-1])
           
           # Update previous row for next iteration
           prevRow = currentRow

       return prevRow[n]  # Last element of the final row contains our answer
