# Time Complexity:
# - O(M * N), where M is the length of text1 and N is the length of text2.
# - In all implementations, we need to fill a table of size M*N in the worst case.

# Space Complexity:
# - Recursive (Memoization): O(M * N) for the dp array + O(M + N) for the recursion stack
# - Iterative (Tabulation): O(M * N) for the dp array
# - Space-optimized: O(N) as we only keep track of the previous row

# INTUITION:
# The longest common subsequence (LCS) is a classic dynamic programming problem. We need to find the longest
# sequence of characters that appear in the same order (not necessarily consecutive) in both strings.
#
# For any two characters at positions i in text1 and j in text2, we have two possibilities:
# 1. If the characters match, the LCS extends by 1 from the LCS of the substrings without these characters.
# 2. If they don't match, the LCS is the maximum of either:
#    - The LCS excluding the current character from text1
#    - The LCS excluding the current character from text2
#
# Example:
# For "abcde" and "ace", the LCS is "ace" with length 3:
# - 'a' matches at the beginning
# - 'c' matches (not consecutively, but in order)
# - 'e' matches at the end

# ALGO:
# The solution is presented in three different implementations:
#
# 1. Top-down (Memoization):
#    a. Use recursion with memoization
#    b. For each position (i,j), check if characters match
#    c. If they match, add 1 to LCS of (i-1,j-1)
#    d. If not, take max of LCS for (i-1,j) and (i,j-1)
#
# 2. Bottom-up (Tabulation):
#    a. Build a 2D table where dp[i][j] represents LCS of text1[0...i-1] and text2[0...j-1]
#    b. Fill the table row by row
#    c. Apply the same logic as in the recursive approach
#
# 3. Space-optimized:
#    a. Observe that we only need the previous row to calculate the current row
#    b. Use two 1D arrays (prev and cur) instead of a 2D array
#    c. After each row calculation, set prev = cur and create a new cur array

class Solution:
   # Top-down approach using memoization
   def longestCommonSubsequence(self, text1: str, text2: str) -> int:
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

       m, n = len(text1), len(text2)
       dp = [[-1] * n for _ in range(m)]  # Initialize memoization table
       return findLCS(m-1, n-1)
       
   # Bottom-up approach using tabulation
   def longestCommonSubsequence(self, text1: str, text2: str) -> int:
       m, n = len(text1), len(text2)
       dp = [[0] * (n + 1) for _ in range(m + 1)]

       for i in range(1, m+1):
           for j in range(1, n+1):
               # Characters match (note the index adjustment: dp[i][j] refers to text1[i-1] and text2[j-1])
               if text1[i-1] == text2[j-1]:
                   dp[i][j] = 1 + dp[i-1][j-1]
               else:
                   # Characters don't match, take max of two possible subproblems
                   dp[i][j] = max(dp[i-1][j], dp[i][j-1])

       return dp[m][n]  # Bottom-right cell contains the length of LCS

   # Space-optimized approach
   def longestCommonSubsequence(self, text1: str, text2: str) -> int:
       m, n = len(text1), len(text2)
       # We only need to keep track of the previous row
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

       return prevRow[n]  # Last element of the final row contains the length of LCS
