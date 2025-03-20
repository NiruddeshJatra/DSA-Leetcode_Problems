# Time Complexity:
# - O(1) because we're iterating through a fixed-size array of Roman numeral mappings (13 pairs).
# - The while loop might seem concerning, but num can only decrease a finite number of times 
#   (at most the value of num), and the total number of iterations across all while loops is bounded by 
#   the initial value of num.

# Space Complexity:
# - O(1) for storing the Roman numeral mappings in storeIntRoman (constant size).
# - The output string's size is proportional to the input, but we don't count output in space complexity.

# INTUITION:
# Converting integers to Roman numerals can be approached greedily. Roman numerals use a combination of symbols, 
# and the largest possible symbol (or combination) should be used at each step to represent the remaining number.
# 
# For example, to convert 1994:
# 1. Start with M (1000) → 1994-1000 = 994 remaining
# 2. Use CM (900) → 994-900 = 94 remaining
# 3. Use XC (90) → 94-90 = 4 remaining
# 4. Use IV (4) → 4-4 = 0 remaining
# Result: MCMXCIV
#
# We need to handle special cases like 4 (IV), 9 (IX), 40 (XL), etc., which use subtraction rather than addition.

# ALGO:
# 1. Create a list of integer-Roman numeral pairs in descending order, including special combinations like CM, CD, etc.
# 2. Iterate through the list of pairs.
# 3. For each pair, while the current number is greater than or equal to the integer value:
#    a. Append the corresponding Roman numeral to the result.
#    b. Subtract the integer value from the current number.
# 4. Continue until the number becomes 0.
# 5. Return the resulting Roman numeral string.

class Solution:
   def intToRoman(self, num: int) -> str:
       romanResult = ""
       
       # Store all possible Roman numeral representations, ordered from largest to smallest
       # Include special cases like CM (900), CD (400), etc.
       valueSymbolPairs = [
           [1000, "M"], [900, "CM"], [500, "D"], [400, "CD"],
           [100, "C"], [90, "XC"], [50, "L"], [40, "XL"],
           [10, "X"], [9, "IX"], [5, "V"], [4, "IV"], [1, "I"]
       ]
       
       # Process the number greedily, starting with the largest values
       for value, symbol in valueSymbolPairs:
           # While the remaining number is greater than or equal to the current value,
           # add its symbol to the result and subtract its value from the number
           while num >= value:
               romanResult += symbol
               num -= value
               
           # If the number becomes 0, we can stop early
           if num == 0:
               break
               
       return romanResult
