# Time Complexity:
# - O(M * N), where M is the length of text1 and N is the length of text2.
# - We compute the LCS between the two strings by filling a table effectively of size M*N.

# Space Complexity:
# - O(N) because we use a space-optimized approach with only two arrays of length N+1.

# INTUITION:
# This problem asks for the minimum number of delete operations to make two strings equal.
# The key insight is that we want to keep the longest common subsequence (LCS) between the two strings,
# and delete everything else.
#
# To make two strings equal, we must:
# 1. Delete characters from text1 that aren't part of the LCS
# 2. Delete characters from text2 that aren't part of the LCS
#
# Therefore, the minimum number of deletions = (length of text1 - LCS) + (length of text2 - LCS)
# = length of text1 + length of text2 - 2*LCS
#
# Example:
# For "sea" and "eat":
# - The LCS is "ea" with length 2
# - We delete 's' from "sea" (1 deletion)
# - We delete 't' from "eat" (1 deletion)
# - Total: 2 deletions

# ALGO:
# 1. Find the longest common subsequence (LCS) between text1 and text2.
# 2. Calculate the minimum number of deletions as (length of text1 + length of text2 - 2*LCS).
#
# Steps for finding LCS using space-optimized approach:
# a. Initialize a 1D array prev of size n+1 with zeros.
# b. For each character in text1, create a new array cur.
# c. Fill cur based on matching characters between text1 and text2.
# d. After each row, update prev = cur.
# e. The final value in prev[n] is the length of the LCS.

class Solution:
   def minDistance(self, text1: str, text2: str) -> int:
       # Get lengths of both strings
       len1, len2 = len(text1), len(text2)
       
       # Initialize previous row for LCS calculation
       prevRow = [0] * (len2 + 1)
       
       # Build LCS table row by row (space-optimized)
       for i in range(1, len1 + 1):
           currentRow = [0] * (len2 + 1)
           for j in range(1, len2 + 1):
               # If characters match
               if text1[i-1] == text2[j-1]:
                   currentRow[j] = 1 + prevRow[j-1]
               else:
                   # Take the maximum of excluding either character
                   currentRow[j] = max(prevRow[j], currentRow[j-1])
           
           # Update previous row for next iteration
           prevRow = currentRow
       
       # Length of LCS is in prevRow[len2]
       lcsLength = prevRow[len2]
       
       # Minimum deletions needed = (length of text1 - LCS) + (length of text2 - LCS)
       # = length of text1 + length of text2 - 2*LCS
       return len1 + len2 - 2 * lcsLength
