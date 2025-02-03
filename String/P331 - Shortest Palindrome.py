# Time Complexity:
# - O(N) where N is length of string
# - Single pass through string for rolling hash
# - String slicing and reversal also O(N)
# - Overall O(N)

# Space Complexity:
# - O(1) for variables storing hash values
# - O(N) for final string concatenation
# - Overall O(N)

# INTUITION:
# To find shortest palindrome, we need to:
# 1. Find longest palindrome prefix in string
# 2. Add reverse of remaining suffix to start
# Use rolling hash to efficiently check if prefix is palindrome
# Example: s = "aacecaaa"
# - "a" is palindrome
# - "aa" is palindrome
# - "aac" is not palindrome
# - "aace" is not palindrome
# - "aacec" is not palindrome
# - "aaceca" is not palindrome
# - "aacecaa" is palindrome
# Add reversed remaining "a" to start
# Result: "aaacecaaa"

# ALGO:
# 1. Use Rabin-Karp rolling hash:
#    - Forward hash (prefix) from left to right
#    - Reverse hash (suffix) from right to left
#    - When hashes match, potential palindrome
# 2. Track last position where hashes matched
# 3. Return:
#    - Reverse of substring after last match
#    - Concatenated with original string

def shortestPalindrome(self, s: str) -> str:
   # Initialize hash values
   prefixHash = suffixHash = lastMatchIndex = 0
   MOD = 10**9 + 7  # Large prime for modulo
   multiplier = power = 1
   BASE = 29  # Prime base for hash
   
   # Calculate rolling hashes
   for i, char in enumerate(s):
       # Convert char to number (1-26)
       charValue = ord(char) - ord('a') + 1
       
       # Update forward hash (prefix)
       prefixHash = (prefixHash * BASE) % MOD
       prefixHash = (prefixHash + charValue) % MOD
       
       # Update reverse hash (suffix)
       suffixHash = (suffixHash + charValue * power) % MOD
       power = (power * BASE) % MOD
       
       # If hashes match, potential palindrome prefix
       if prefixHash == suffixHash:
           lastMatchIndex = i
   
   # Create shortest palindrome:
   # 1. Take substring after last match
   # 2. Reverse it
   # 3. Add original string
   return s[lastMatchIndex + 1:][::-1] + s
