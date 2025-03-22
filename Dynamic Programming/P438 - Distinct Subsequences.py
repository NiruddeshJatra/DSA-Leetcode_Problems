# Time Complexity:
# - O(M * N), where M is the length of string s and N is the length of string t.
# - In all implementations, we fill a table of size M*N (or effectively process M*N subproblems).

# Space Complexity:
# - Recursive (Memoization): O(M * N) for the dp array + O(M+N) for the recursion stack
# - Iterative (Tabulation): O(M * N) for the dp array
# - Space-optimized: O(N) as we only keep track of the previous row

# INTUITION:
# The problem asks for the number of distinct subsequences of s that equal t.
# For each character in t, we need to find all possible ways it can be matched with characters in s.
#
# For each position (i,j) where i is index in s and j is index in t:
# 1. If s[i] == t[j], we have two options:
#    a. Match these characters and look for the rest of t in the rest of s (dp[i-1][j-1])
#    b. Skip this occurrence of the character in s and keep looking (dp[i-1][j])
# 2. If s[i] != t[j], we can only skip this character in s and keep looking (dp[i-1][j])
#
# Example:
# s = "rabbbit", t = "rabbit"
# There are 3 ways to form "rabbit" from "rabbbit":
# 1. ra(b)bbit - ra(b)bit - rabbit
# 2. rab(b)bit - rab(b)it - rabbit
# 3. rabb(b)it - rabb(b)t - rabbit

# ALGO:
# The solution is presented in three different implementations:
#
# 1. Top-down (Memoization):
#    a. Base cases: 
#       - If j < 0 (finished t), return 1 (found a valid subsequence)
#       - If i < 0 (finished s), return 0 (no valid subsequence)
#    b. Recursive case:
#       - If s[i] == t[j], add results from both matching and skipping
#       - Else, only consider skipping the current character in s
#
# 2. Bottom-up (Tabulation):
#    a. Initialize dp[i][0] = 1 for all i (there's one way to form empty t)
#    b. For each (i,j), apply the same logic as recursive approach
#    c. Return dp[m][n]
#
# 3. Space-optimized:
#    a. Use only two arrays (prev and cur) instead of the entire 2D array
#    b. Initialize prev[0] = 1 and cur[0] = 1 for each row
#    c. Update cur based on prev using the same logic
#    d. After each row, update prev = cur

class Solution:
   # Top-down approach using memoization
   def numDistinct(self, s: str, t: str) -> int:
       def countSubsequences(i, j):
           # Base cases
           if j < 0:  # Finished matching all characters in t
               return 1
           if i < 0:  # Ran out of characters in s
               return 0
               
           # If already computed, return from memo
           if dp[i][j] != -1:
               return dp[i][j]
               
           # If characters match, we have two choices
           if s[i] == t[j]:
               # Either use this match and move both pointers, or skip this match and try to match j with earlier characters
               dp[i][j] = countSubsequences(i-1, j-1) + countSubsequences(i-1, j)
           else:
               # If characters don't match, skip this character in s
               dp[i][j] = countSubsequences(i-1, j)
               
           return dp[i][j]
           
       m, n = len(s), len(t)
       dp = [[-1] * n for _ in range(m)]  # Initialize memoization table
       return countSubsequences(m-1, n-1)
       
   # Bottom-up approach using tabulation
   def numDistinct(self, s: str, t: str) -> int:
       m, n = len(s), len(t)
       dp = [[0] * (n + 1) for _ in range(m + 1)]
       
       # Base case: empty t string can be formed in one way
       for i in range(m + 1):
           dp[i][0] = 1
           
       for i in range(1, m + 1):
           for j in range(1, n + 1):
               if s[i-1] == t[j-1]:
                   # If characters match, add counts from both matching and skipping
                   dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
               else:
                   # If characters don't match, can only skip this character in s
                   dp[i][j] = dp[i-1][j]
                   
       return dp[m][n]

   # Space-optimized approach
   def numDistinct(self, s: str, t: str) -> int:
       m, n = len(s), len(t)
       # Initialize previous row with the base case
       prevRow = [0] * (n + 1)
       prevRow[0] = 1  # Empty t string can be formed in one way
       
       for i in range(1, m + 1):
           # Initialize current row with the base case
           currentRow = [0] * (n + 1)
           currentRow[0] = 1  # Empty t string can be formed in one way
           
           for j in range(1, n + 1):
               if s[i-1] == t[j-1]:
                   # If characters match, add counts from both matching and skipping
                   currentRow[j] = prevRow[j-1] + prevRow[j]
               else:
                   # If characters don't match, can only skip this character in s
                   currentRow[j] = prevRow[j]
           
           # Update previous row for next iteration
           prevRow = currentRow
           
       return prevRow[n]
