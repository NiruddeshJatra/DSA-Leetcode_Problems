# Time Complexity:
# - O(N²), where N is the length of string s.
# - We fill a table of size N*N (effectively) when computing the LCS between s and its reverse.

# Space Complexity:
# - O(N) due to the space-optimized dp approach using only two arrays (prev and cur).

# INTUITION:
# The key insight is to relate the minimum insertions needed to make a string palindromic with the longest palindromic subsequence.
# To make a string a palindrome, we want to preserve as many characters as possible in their original positions.
#
# The characters that are already part of the longest palindromic subsequence (LPS) don't need any insertions.
# Therefore, the minimum number of insertions needed is the total length of the string minus the length of the LPS.
#
# Example:
# For string "leetcode", the LPS is "ece" with length 3.
# To make it palindrome, we need to insert (8-3) = 5 characters: "leetcodocteel"
#
# Using LCS to find LPS:
# As we saw in the longestPalindromeSubseq problem, the LPS can be found by computing the LCS between the string 
# and its reverse. This is because a palindrome reads the same from both directions.

# ALGO:
# 1. Find the longest palindromic subsequence (LPS) by computing the LCS between the string and its reverse.
# 2. The minimum insertions needed = length of string - length of LPS.
#
# Steps for finding LCS using space-optimized approach:
# a. Initialize a 1D array prev of size n+1 with zeros.
# b. For each character in text1, create a new array cur.
# c. Fill cur based on matching characters between text1 and text2.
# d. After each row, update prev = cur.
# e. The final value in prev[n] is the length of the LCS (or LPS).

class Solution:
   def minInsertions(self, s: str) -> int:
       # Original string and its reverse
       originalString = s
       reversedString = s[::-1]
       stringLength = len(originalString)
       
       # Initialize previous row for dp calculation
       previousRow = [0] * (stringLength + 1)
       
       # Build LCS table row by row (space-optimized)
       for i in range(1, stringLength + 1):
           currentRow = [0] * (stringLength + 1)
           for j in range(1, stringLength + 1):
               # If characters match
               if originalString[i-1] == reversedString[j-1]:
                   currentRow[j] = 1 + previousRow[j-1]
               else:
                   # Take the maximum of excluding either character
                   currentRow[j] = max(previousRow[j], currentRow[j-1])
           
           # Update previous row for next iteration
           previousRow = currentRow
       
       # Length of longest palindromic subsequence is in previousRow[stringLength]
       lpsLength = previousRow[stringLength]
       
       # Minimum insertions needed = length of string - length of LPS
       return stringLength - lpsLength
