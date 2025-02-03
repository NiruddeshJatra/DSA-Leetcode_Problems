# Time Complexity:
# - O(N) where N is length of string
# - Single pass through string for rolling hash calculation
# - String slicing at end is O(N)
# - Overall complexity is O(N)

# Space Complexity:
# - O(1) for hash variables and calculations
# - O(N) for returned string slice
# - Overall O(N) for result

# INTUITION:
# We need to find longest string that is both prefix and suffix
# Use rolling hash to efficiently check equality:
# 1. Build prefix hash from left to right
# 2. Build suffix hash from right to left
# 3. When hashes match, potential longest prefix/suffix
# Example: s = "level"
# Check prefixes and suffixes:
# l|evel vs l|evel ✓
# le|vel vs v|el ✗
# lev|el vs e|l ✗
# leve|l vs l| ✗
# Answer: "l"

# ALGO:
# 1. Use Rabin-Karp rolling hash:
#    - Forward hash from left for prefix
#    - Reverse hash from right for suffix
#    - Use modulo arithmetic to prevent overflow
# 2. For each position (except last):
#    - Update prefix hash with current char
#    - Update suffix hash with corresponding char from end
#    - If hashes match, update last matching position
# 3. Return prefix up to last matching position

def longestPrefix(self, s: str) -> str:
   stringLength = len(s)
   prefixHash = suffixHash = 0
   lastMatch = -1
   MOD = 10**9 + 7     # Large prime for modulo
   power = 1           # Current power of base
   BASE = 29          # Prime base for hash
   
   # Process all positions except last
   for i in range(stringLength - 1):
       # Get characters for prefix and suffix
       prefixChar = ord(s[i]) - ord('a') + 1
       suffixChar = ord(s[stringLength - 1 - i]) - ord('a') + 1
       
       # Update prefix hash
       prefixHash = (prefixHash * BASE) % MOD
       prefixHash = (prefixHash + prefixChar) % MOD
       
       # Update suffix hash
       suffixHash = (suffixHash + suffixChar * power) % MOD
       power = (power * BASE) % MOD
       
       # If hashes match, update last matching position
       if prefixHash == suffixHash:
           lastMatch = i
   
   # Return longest matching prefix
   return s[:lastMatch + 1]
