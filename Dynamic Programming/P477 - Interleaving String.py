# Time Complexity:
# - O(M * N), where M is the length of s1 and N is the length of s2.
# - We fill a 2D DP table of size (M+1) x (N+1), and each cell is computed in O(1) time.

# Space Complexity:
# - O(M * N), for the 2D DP table storing results for all possible (i, j) states.
# - Can be optimized to O(min(M, N)) using 1D DP, but current solution uses 2D for clarity.

# INTUITION:
# We need to check if s3 can be formed by interleaving characters from s1 and s2 while maintaining
# the relative order within each string. This is a classic dynamic programming problem.
# 
# The key insight is that at any position in s3, we can either take the next character from s1
# or from s2 (if they match the current character in s3). We use DP to avoid recomputing
# the same subproblems.
# 
# State definition: dp[i][j] = True if s3[0:i+j] can be formed by interleaving s1[0:i] and s2[0:j]
# Base case: dp[m][n] = True (empty strings can form empty result)
# Transition: dp[i][j] = True if either:
# - We can take s1[i] (if s1[i] == s3[i+j] and dp[i+1][j] is True)
# - We can take s2[j] (if s2[j] == s3[i+j] and dp[i][j+1] is True)
# 
# Example: s1="aab", s2="axy", s3="aaxaby"
# We build the DP table bottom-up to check all possible interleavings.

# ALGO:
# 1. Check if lengths match: len(s1) + len(s2) must equal len(s3)
# 2. Create 2D DP table of size (m+1) x (n+1) initialized to False
# 3. Set base case: dp[m][n] = True (both strings fully consumed)
# 4. Fill DP table from bottom-right to top-left:
#    a. If we can take character from s1: check if s1[i] == s3[i+j] and dp[i+1][j] is True
#    b. If we can take character from s2: check if s2[j] == s3[i+j] and dp[i][j+1] is True
#    c. Set dp[i][j] = True if either condition is satisfied
# 5. Return dp[0][0] (can we form entire s3 starting from beginning of s1 and s2)

class Solution:
   def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
       # Early termination: lengths must match
       if len(s1) + len(s2) != len(s3):
           return False
           
       lengthS1, lengthS2 = len(s1), len(s2)
       
       # dp[i][j] = True if s3[0:i+j] can be formed by interleaving s1[0:i] and s2[0:j]
       dp = [[False] * (lengthS2 + 1) for _ in range(lengthS1 + 1)]
       
       # Base case: both strings are fully consumed
       dp[lengthS1][lengthS2] = True

       # Fill DP table from bottom-right to top-left
       for i in range(lengthS1, -1, -1):
           for j in range(lengthS2, -1, -1):
               # Try taking character from s1
               if i < lengthS1 and s1[i] == s3[i + j] and dp[i + 1][j]:
                   dp[i][j] = True
               
               # Try taking character from s2
               if j < lengthS2 and s2[j] == s3[i + j] and dp[i][j + 1]:
                   dp[i][j] = True

       return dp[0][0]
