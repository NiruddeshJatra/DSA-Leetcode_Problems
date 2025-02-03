# Time Complexity:
# - O(N + M) where N is length of repeated string A and M is length of B
# - String repeat operation is O(N * times)
# - String search (in operator) is O(N + M)
# - Overall O(N + M) as times is bounded by length of strings

# Space Complexity:
# - O(N * times) for creating repeated string
# - times is proportional to len(B)/len(A)
# - Overall O(M) where M is length of string B

# INTUITION:
# To find pattern B in repeated A:
# 1. Need minimum repetitions to cover length of B
# 2. May need one extra repetition for overlap
# Example 1: a="abcd", b="cdab" 
# - Minimum 1 repeat not enough: "abcd"
# - Need 2 repeats: "abcdabcd"
# Example 2: a="abcd", b="bcdab"
# - Two repeats needed for proper alignment
# - Pattern starts in middle of first repeat

# ALGO:
# 1. Calculate minimum repeats needed:
#    ceil(len(b)/len(a))
#    - Ensures repeated string is at least as long as B
# 2. Try with minimum repeats and minimum + 1:
#    - If B found in either case, return count
#    - Otherwise pattern impossible, return -1
# 3. Check pattern exists using 'in' operator

def repeatedStringMatch(self, a: str, b: str) -> int:
   # Calculate minimum repeats needed
   minimumRepeats = ceil(len(b) / len(a))
   
   # Try minimum repeats and minimum + 1
   for extraRepeat in range(2):
       currentRepeats = minimumRepeats + extraRepeat
       # Check if pattern exists in repeated string
       if b in a * currentRepeats:
           return currentRepeats
   
   # Pattern not found
   return -1
