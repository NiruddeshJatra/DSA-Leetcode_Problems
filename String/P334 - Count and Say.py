# Time Complexity:
# - O(2^n) as string length can double in each iteration
# - RLE function is O(L) where L is length of input string
# - Recursion depth is n

# Space Complexity:
# - O(2^n) for storing result strings
# - Recursion stack space is O(n)
# - Overall O(2^n)

# INTUITION:
# For each number n > 1, we:
# 1. Get n-1th term
# 2. Convert it using run-length encoding (RLE)
# Each number describes previous sequence
# Example sequence:
# n=1: "1"
# n=2: "11" (one 1)
# n=3: "21" (two 1s) 
# n=4: "1211" (one 2, one 1)
# n=5: "111221" (one 1, one 2, two 1s)

# ALGO:
# 1. Base case: return "1" for n=1
# 2. For n > 1:
#    - Get previous term recursively
#    - Apply RLE:
#      * Count consecutive same digits
#      * Build string with count + digit
#    - Return encoded string
# 3. RLE helper function:
#    - Track current digit and its count
#    - When digit changes, add count+digit to result
#    - Don't forget last group

def countAndSay(self, n: int) -> str:
   def runLengthEncode(sequence: str) -> str:
       result = ""
       count = 0
       currentDigit = sequence[0]
       
       # Process each character
       for char in sequence:
           if char == currentDigit:
               # Same digit, increment count
               count += 1
           else:
               # Different digit, add previous group
               result += str(count) + currentDigit
               # Reset for new digit
               count = 1
               currentDigit = char
       
       # Add last group
       result += str(count) + currentDigit
       return result
   
   # Base case
   if n == 1:
       return "1"
       
   # Get previous term and encode it
   return runLengthEncode(self.countAndSay(n-1))
