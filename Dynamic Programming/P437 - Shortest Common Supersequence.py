# Time Complexity:
# - O(M * N), where M is the length of s1 and N is the length of s2.
# - Computing the LCS with the dp table takes O(M * N).
# - Reconstructing the shortest common supersequence also takes O(M + N) which is dominated by O(M * N).

# Space Complexity:
# - O(M * N) for the dp table.
# - O(M + N) for the output string in the worst case.

# INTUITION:
# The shortest common supersequence (SCS) is a string that contains both s1 and s2 as subsequences and has minimal length.
# We can leverage the longest common subsequence (LCS) to find the SCS efficiently.
#
# The key insight is:
# 1. Characters in the LCS need to appear only once in the SCS.
# 2. All other characters from both strings need to be included.
#
# For example, if s1="abac" and s2="cab":
# - The LCS is "ab"
# - When building the SCS, we include each character from the LCS once.
# - We also include all other characters from both strings.
# - The SCS would be "cabac"
#
# We can build the SCS by backtracking through the LCS dp table:
# - When the characters match (part of LCS), include it once.
# - When they don't match, include the character from the string we're moving away from.

# ALGO:
# 1. Find the LCS between s1 and s2 using dynamic programming.
# 2. Backtrack through the dp table to construct the SCS:
#    a. If s1[i-1] == s2[j-1], include this character once and move diagonally (i-1, j-1).
#    b. Otherwise, choose the direction with the larger LCS value:
#       - If dp[i-1][j] > dp[i][j-1], include s1[i-1] and move up (i-1, j).
#       - Else, include s2[j-1] and move left (i, j-1).
# 3. Handle leftover characters from either string.
# 4. Reverse the resulting string (since we built it backward).

class Solution:
   def shortestCommonSupersequence(self, s1: str, s2: str) -> str:
       # Get lengths of both strings
       len1, len2 = len(s1), len(s2)
       
       # Build LCS dp table
       dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]
       
       # Fill the dp table for LCS
       for i in range(1, len1 + 1):
           for j in range(1, len2 + 1):
               if s1[i-1] == s2[j-1]:
                   dp[i][j] = 1 + dp[i-1][j-1]
               else:
                   dp[i][j] = max(dp[i-1][j], dp[i][j-1])
       
       # Build the shortest common supersequence by backtracking
       result = []
       i, j = len1, len2
       
       # While both strings have characters left
       while i > 0 and j > 0:
           # If current characters are the same (part of LCS)
           if s1[i-1] == s2[j-1]:
               # Add the character once
               result.append(s1[i-1])
               i -= 1
               j -= 1
           # Follow the direction of larger LCS value
           elif dp[i-1][j] > dp[i][j-1]:
               # Include character from s1
               result.append(s1[i-1])
               i -= 1
           else:
               # Include character from s2
               result.append(s2[j-1])
               j -= 1
       
       # Add any remaining characters from s1
       while i > 0:
           result.append(s1[i-1])
           i -= 1
       
       # Add any remaining characters from s2
       while j > 0:
           result.append(s2[j-1])
           j -= 1
       
       # Reverse the result (since we built it backward)
       return ''.join(result[::-1])
