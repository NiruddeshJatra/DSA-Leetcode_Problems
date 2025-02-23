# Time Complexity:
# - O(N * M) where N is the length of input string and M is number of iterations
# - In each iteration, string length reduces by 1 
# - Need to iterate until string length becomes 2
# - For initial string length N, we need N-2 iterations

# Space Complexity:
# - O(N) for the temporary string newDigit
# - String length reduces by 1 in each iteration
# - No additional data structures used

# INTUITION:
# For a number like 12345, we want to repeatedly add adjacent digits and take modulo 10
# until we get a 2 digit number, then check if those digits are same.
#
# Example:
# Input: "12345"
# Step 1: (1+2)%10, (2+3)%10, (3+4)%10, (4+5)%10 = "3579"
# Step 2: (3+5)%10, (5+7)%10, (7+9)%10 = "818"
# Step 3: (8+1)%10, (1+8)%10 = "99"
# Since 9=9, return True

# ALGO:
# 1. While input string length > 2:
#    - Create new string by adding adjacent digits and taking modulo 10
#    - Update input string with new string
# 2. Check if final two digits are same
# 3. Return True if same, False otherwise

class Solution:
   def hasSameDigits(self, inputStr: str) -> bool:
       resultStr = ""
       
       # Keep processing until we get a 2-digit number
       while len(inputStr) != 2:
           # Process each adjacent pair
           for i in range(len(inputStr)-1):
               # Add digits and take modulo 10
               sumDigit = (int(inputStr[i]) + int(inputStr[i+1])) % 10
               resultStr += str(sumDigit)
           
           # Update input for next iteration
           inputStr = resultStr
           resultStr = ""
       
       # Check if final two digits are same
       return inputStr[0] == inputStr[1]
