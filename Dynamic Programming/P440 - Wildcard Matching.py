# Time Complexity:
# - O(m * n) where m is the length of string s and n is the length of pattern p.
# - We need to fill a table of size (m+1) x (n+1), computing each cell exactly once.

# Space Complexity:
# - Recursive: O(m * n) for the memoization table + O(m + n) for the recursion stack.
# - Tabulation: O(m * n) for the 2D DP table.
# - Space-optimized: O(m) as we only need to store two rows at a time.

# INTUITION:
# This is the Wildcard Matching problem, where we need to determine if a string matches a pattern
# that can contain two special characters: '?' (matches any single character) and '*' (matches any
# sequence of characters, including an empty sequence).
#
# The key insight is to break down this problem into smaller subproblems. For each position in both
# the string and pattern, we need to determine if the substring up to that position matches.
#
# Consider what happens when we encounter different characters in the pattern:
# 1. If we have a regular character, it must match exactly with the string.
# 2. If we have a '?', it matches any single character in the string.
# 3. If we have a '*', we have two choices:
#    a. Use the '*' to match the current character in the string and keep the '*' active for potential future matches.
#    b. Skip the '*' entirely (match it with an empty sequence).
#
# Example: Matching "abcde" with pattern "a*c?e"
# - 'a' matches 'a'
# - '*' can match 'b' and we keep '*' active to potentially match more
# - Alternatively, '*' could match nothing, and we move to 'c'
# - 'c' matches 'c'
# - '?' matches 'd'
# - 'e' matches 'e'
# - Result: True (pattern matches string)

# ALGORITHM:
# 1. Define a function f(i,j) that returns whether s[0...i-1] matches p[0...j-1].
# 2. Base cases:
#    - f(0,0) = True (empty pattern matches empty string)
#    - f(i,0) = False for i > 0 (non-empty string can't match empty pattern)
#    - f(0,j) = True if p[0...j-1] consists of only '*' characters (since '*' can match empty)
# 3. Recursive cases:
#    - If p[j-1] is a regular character or '?', it must match s[i-1]
#    - If p[j-1] is '*', we can either use it to match the current character or skip it
# 4. Implement using memoization (top-down) or tabulation (bottom-up).

class Solution:
   # Top-down memoization approach
   def isMatch(self, s: str, p: str) -> bool:
       def f(i, j):
           # Base case: both string and pattern are empty
           if j == 0 and i == 0:
               return True
           
           # Base case: pattern is empty but string is not
           if j == 0 and i > 0:
               return False
           
           # Base case: string is empty but pattern is not
           # Pattern must be all '*' characters to match empty string
           if i == 0 and j > 0:
               for k in range(1, j+1):
                   if p[k-1] != '*':
                       return False
               return True
           
           # Return memoized result if available
           if dp[i][j] != -1:
               return dp[i][j]
           
           # Case 1: Current characters match or pattern has '?'
           if s[i-1] == p[j-1] or p[j-1] == '?':
               dp[i][j] = f(i-1, j-1)
               return dp[i][j]
           
           # Case 2: Pattern has '*' - we have two choices
           elif p[j-1] == '*':
               # Either skip '*' (match empty) OR use '*' to match current character and keep it active
               dp[i][j] = f(i, j-1) or f(i-1, j)
               return dp[i][j]
           
           # Case 3: Characters don't match
           dp[i][j] = False
           return False
       
       m, n = len(s), len(p)
       # Initialize memoization table with -1 (unprocessed)
       dp = [[-1] * (n + 1) for _ in range(m + 1)]
       return f(m, n)
   
   # Bottom-up tabulation approach
   def isMatch(self, s: str, p: str) -> bool:
       m, n = len(s), len(p)
       # Initialize DP table
       dp = [[False] * (n + 1) for _ in range(m + 1)]
       
       # Base case: empty pattern matches empty string
       dp[0][0] = True
       
       # Base case: empty string - can only match if pattern consists of all '*'
       for j in range(1, n+1):
           allStars = True
           for k in range(1, j+1):
               if p[k-1] != '*':
                   allStars = False
                   break
           dp[0][j] = allStars
       
       # Fill the DP table
       for i in range(1, m+1):
           for j in range(1, n+1):
               # Case 1: Current characters match or pattern has '?'
               if s[i-1] == p[j-1] or p[j-1] == '?':
                   dp[i][j] = dp[i-1][j-1]
               # Case 2: Pattern has '*' - we have two choices
               elif p[j-1] == '*':
                   # Either skip '*' OR use '*' to match current character
                   dp[i][j] = dp[i][j-1] or dp[i-1][j]
               # Case 3: Characters don't match - dp[i][j] remains False
       
       return dp[m][n]
   
   # Space-optimized approach (O(m) space)
   def isMatch(self, s: str, p: str) -> bool:
       m, n = len(s), len(p)
       # Initialize previous row for DP
       prevRow = [False] * (m + 1)
       prevRow[0] = True  # Base case: empty pattern matches empty string
       
       for i in range(1, n + 1):
           # Initialize current DP row
           currentRow = [False] * (m + 1)
           
           # Check if current pattern prefix (up to i) consists of all '*'
           allStars = True
           for k in range(1, i + 1):
               if p[k-1] != '*':
                   allStars = False
                   break
           currentRow[0] = allStars
           
           for j in range(1, m + 1):
               # Case 1: Current characters match or pattern has '?'
               if p[i-1] == '?' or s[j-1] == p[i-1]:
                   currentRow[j] = prevRow[j-1]
               # Case 2: Pattern has '*' - we have two choices
               elif p[i-1] == '*':
                   # Either match zero characters (skip '*') OR extend match to current character
                   currentRow[j] = currentRow[j-1] or prevRow[j]
               # Case 3: Characters don't match - currentRow[j] remains False
           
           # Update previous row for next iteration
           prevRow = currentRow
       
       return prevRow[m]
