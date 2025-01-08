# Time Complexity:
# - O(N), where N is the length of string s
# - We only need to traverse string s once, and for each character we do O(1) operations

# Space Complexity:
# - O(1), as we only use two pointers and a counter variable
# - No additional data structures are used that grow with input size

# INTUITION:
# The problem asks us to find how many characters we need to append to string s to make t a subsequence.
# Using two-pointer technique is ideal here because:
# 1. We need to maintain the relative order of characters (subsequence property)
# 2. We can efficiently track matching characters without backtracking
# 3. After finding all matches, the remaining characters in t are what we need to append

# ALGO:
# 1. Initialize pointer j for string t and result counter
# 2. Iterate through string s with pointer i:
#    - If current characters match (s[i] == t[j]):
#      * Move t's pointer (j) forward
#    - If we've matched all characters in t:
#      * Break as we don't need to continue
# 3. Return the number of remaining characters in t (len(t) - j)

class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        # Pointer for string t
        t_pointer = 0
        
        # Iterate through each character in s
        for curr_char in s:
            # If we find a match, move t's pointer forward
            if t_pointer < len(t) and curr_char == t[t_pointer]:
                t_pointer += 1
            
            # If we've matched all characters in t, we can stop
            if t_pointer == len(t):
                break
        
        # Return remaining characters needed from t
        return len(t) - t_pointer
