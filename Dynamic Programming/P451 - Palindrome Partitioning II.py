# Time Complexity:
# - O(N³), where N is the length of the input string
# - Palindrome checking takes O(N)
# - Two nested loops for checking palindrome substrings
# - Filling palindrome table takes O(N²)

# Space Complexity:
# - O(N²) for the palindrome table
# - O(N) for the dynamic programming array
# - Total space complexity is O(N²)

# INTUITION:
# The problem requires finding the minimum number of cuts to partition a string 
# so that every substring is a palindrome
# Key strategy:
# - Precompute all possible palindrome substrings
# - Use dynamic programming to track minimum cuts
# Example:
# s = "aab"
# Cuts needed: 1 
# Partitions: "aa" | "b"
# This minimizes cuts while ensuring all substrings are palindromes

# ALGO:
# 1. Create a palindrome table to quickly check palindrome substrings
# 2. Initialize base cases in palindrome table
# 3. Fill palindrome table for longer substrings
# 4. Use dynamic programming to compute minimum cuts
# 5. Work backwards through the string
# 6. For each index, find minimum cuts for palindrome partitions

class Solution:
   def minCut(self, s: str) -> int:
       n = len(s)
       # Precompute palindrome table
       isPalindrome = [[False] * n for _ in range(n)]
       
       # All single characters are palindromes
       for i in range(n):
           isPalindrome[i][i] = True
       
       # Check palindromes of length 2
       for i in range(n - 1):
           isPalindrome[i][i+1] = (s[i] == s[i+1])
       
       # Fill palindrome table for longer substrings
       for length in range(3, n + 1):
           for start in range(n - length + 1):
               end = start + length - 1
               # Check if outer characters match and inner substring is palindrome
               if s[start] == s[end] and isPalindrome[start+1][end-1]:
                   isPalindrome[start][end] = True
       
       # Dynamic programming to find minimum cuts
       minCuts = [0] * (n + 1)
       minCuts[n] = -1  # Base case for empty string
       
       # Iterate backwards through the string
       for currentStart in range(n - 1, -1, -1):
           currentMinCuts = float('inf')
           for currentEnd in range(currentStart, n):
               # If substring is palindrome, calculate potential cuts
               if isPalindrome[currentStart][currentEnd]:
                   potentialCuts = 1 + minCuts[currentEnd + 1]
                   currentMinCuts = min(currentMinCuts, potentialCuts)
           
           # Store minimum cuts for current starting point
           minCuts[currentStart] = currentMinCuts
       
       # Return minimum cuts for entire string
       return minCuts[0]
