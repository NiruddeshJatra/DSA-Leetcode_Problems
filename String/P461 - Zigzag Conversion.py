# Time Complexity:
# - O(n), where n is the length of the input string
# - We visit each character in the string exactly once
# - The nested loops don't create additional complexity as each character is processed once

# Space Complexity:
# - O(n) for the result string
# - We build the answer string character by character

# INTUITION:
# The ZigZag conversion creates a pattern where characters are arranged in rows
# The key insight is to identify the mathematical pattern for character positions
# Pattern observations:
# - First and last rows have consistent gaps of (2*numRows - 2)
# - Middle rows alternate between two different gap sizes
# - Gap sizes depend on the current row position
# Example:
# s = "PAYPALISHIRING", numRows = 3
# Zigzag pattern:
# P   A   H   R
# A P L S I I G
# Y   I   N
# Reading row by row: "PAHNAPLSIIGYIR"

# ALGO:
# 1. Handle edge case where numRows = 1
# 2. Process each row from top to bottom
# 3. For each row, calculate the correct indices using the zigzag pattern:
#    - First/last rows: consistent gap of (2*numRows - 2)
#    - Middle rows: alternate between two gap sizes
#      * Gap 1: (2*numRows - 2 - 2*row)
#      * Gap 2: (2*row)
# 4. Collect characters in the correct zigzag order

class Solution:
   def convert(self, s: str, numRows: int) -> int:
       # Handle edge case: single row means no zigzag conversion needed
       if numRows == 1:
           return s
       
       result = ""
       
       # Process each row from top to bottom
       for currentRow in range(numRows):
           # Start with the first character in this row
           charIndex = currentRow
           alternatingGap = 0  # Counter to alternate between two gap sizes
           
           # Collect all characters belonging to current row
           while charIndex < len(s):
               # Add current character to result
               result += s[charIndex]
               
               # Calculate next character index based on row position
               if currentRow == 0 or currentRow == numRows - 1:
                   # First and last rows: consistent gap
                   charIndex += 2 * numRows - 2
               elif alternatingGap % 2 == 0:
                   # Middle rows: first gap size (going down)
                   charIndex += 2 * numRows - 2 - 2 * currentRow
               else:
                   # Middle rows: second gap size (going up)
                   charIndex += 2 * currentRow
               
               # Increment counter for gap alternation
               alternatingGap += 1
       
       return result
