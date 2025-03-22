# Time Complexity:
# - O(m * n) where m and n are the lengths of the two input strings.
# - We compute each subproblem exactly once, filling a table of m*n cells.

# Space Complexity:
# - Recursive: O(m * n) for the memoization table + O(m + n) for the recursion stack.
# - Tabulation: O(m * n) for the 2D DP table.
# - Space-optimized: O(n) as we only need to store two rows at a time.

# INTUITION:
# This problem asks for the minimum number of operations (insert, delete, replace) to convert one string 
# to another - also known as the Edit Distance or Levenshtein Distance problem.
#
# The key insight is that for each position in both strings, we have a few choices:
# 1. If the current characters match, no operation is needed - we can just move forward.
# 2. If they don't match, we have three choices:
#    a. Insert a character (equivalent to advancing in the second string)
#    b. Delete a character (equivalent to advancing in the first string)
#    c. Replace a character (equivalent to advancing in both strings)
#
# Example: Converting "horse" to "ros"
# - Take last characters: 'e' vs 's' - they don't match
# - We can either:
#   - Insert 's' after 'e' (then need to convert "horse" to "ro")
#   - Delete 'e' (then need to convert "hors" to "ros")
#   - Replace 'e' with 's' (then need to convert "hors" to "ro")
# - We select the option that leads to the minimum total operations.

# ALGORITHM:
# 1. Define a function f(i,j) to compute the edit distance between text1[0...i] and text2[0...j].
# 2. Base cases:
#    - If i < 0, return j+1 (need j+1 insertions)
#    - If j < 0, return i+1 (need i+1 deletions)
# 3. Recursive case:
#    - If text1[i] == text2[j], no operation needed, return f(i-1, j-1)
#    - Else, take minimum of:
#      - f(i-1, j) + 1 (deletion)
#      - f(i, j-1) + 1 (insertion)
#      - f(i-1, j-1) + 1 (replacement)
# 4. Implement this using either memoization (top-down) or tabulation (bottom-up).

class Solution:
   # Top-down memoization approach
   def minDistance(self, text1: str, text2: str) -> int:
       def f(i, j):
           # Base cases
           if i < 0:
               return j + 1  # Insert j+1 characters
           if j < 0:
               return i + 1  # Delete i+1 characters
           
           # Return memoized result if available
           if dp[i][j] != -1:
               return dp[i][j]
           
           # If characters match, no operation needed
           if text1[i] == text2[j]:
               dp[i][j] = f(i-1, j-1)
           else:
               # Try all three operations and take minimum
               dp[i][j] = 1 + min(
                   f(i-1, j),      # Delete operation
                   f(i, j-1),      # Insert operation
                   f(i-1, j-1)     # Replace operation
               )
           
           return dp[i][j]
       
       m, n = len(text1), len(text2)
       dp = [[-1] * n for _ in range(m)]  # Memoization table
       return f(m-1, n-1)

   # Bottom-up tabulation approach
   def minDistance(self, text1: str, text2: str) -> int:
       m, n = len(text1), len(text2)
       # Create DP table with dimensions (m+1) x (n+1)
       dp = [[0] * (n + 1) for _ in range(m + 1)]
       
       # Initialize base cases
       for j in range(n + 1):
           dp[0][j] = j  # Converting empty string to text2[0...j]
       
       for i in range(m + 1):
           dp[i][0] = i  # Converting text1[0...i] to empty string
       
       # Fill the DP table
       for i in range(1, m+1):
           for j in range(1, n+1):
               # If characters match, no operation needed
               if text1[i-1] == text2[j-1]:
                   dp[i][j] = dp[i-1][j-1]
               else:
                   # Take minimum of three operations and add 1
                   dp[i][j] = 1 + min(
                       dp[i-1][j],    # Delete
                       dp[i][j-1],    # Insert
                       dp[i-1][j-1]   # Replace
                   )
       
       return dp[m][n]  # Return final result

   # Space-optimized approach (O(n) space)
   def minDistance(self, text1: str, text2: str) -> int:
       m, n = len(text1), len(text2)
       # We only need to store the previous row
       prevRow = [j for j in range(n + 1)]  # Initialize with base cases
       
       for i in range(1, m+1):
           # Initialize current row with the first element
           currentRow = [0] * (n + 1)
           currentRow[0] = i  # Base case: converting text1[0...i] to empty string
           
           for j in range(1, n+1):
               # If characters match, copy from diagonal
               if text1[i-1] == text2[j-1]:
                   currentRow[j] = prevRow[j-1]
               else:
                   # Take minimum of three operations and add 1
                   currentRow[j] = 1 + min(
                       prevRow[j],      # Delete
                       currentRow[j-1],  # Insert
                       prevRow[j-1]     # Replace
                   )
           
           # Update previous row for next iteration
           prevRow = currentRow
       
       return prevRow[n]  # Return final result
