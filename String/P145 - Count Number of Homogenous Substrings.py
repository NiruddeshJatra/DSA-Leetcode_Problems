# Time Complexity: O(n), where n is the length of the string `s`. 
# We iterate through the string once and count homogenous substrings for each character.

# Space Complexity: O(1), as we are only using a few variables to track indices and counts.

# INTUITION:
# The goal is to count all homogenous substrings (substrings consisting of the same character). 
# The key observation is that for a stretch of `k` consecutive identical characters, 
# there are k + (k-1) + (k-2) + ... + 1 homogenous substrings.
# We can count these substrings incrementally by adding the number of substrings ending at each character.

# ALGO:
# 1. Initialize a variable `cnt` to store the total number of homogenous substrings. 
#    Initially, it is set to the length of the string since each character is a homogenous substring by itself.
# 2. Iterate through the string:
#    2.1 If the current character is the same as the previous one, increment the count of homogenous substrings by the 
#        number of new substrings formed with this character.
#    2.2 If the current character is different from the previous one, reset the temporary index `tempIdx` to the current position.
# 3. Return the total count modulo (10^9 + 7) as required by the problem constraints.

class Solution:
    def countHomogenous(self, s: str) -> int:
        cnt = len(s)  # Start by counting each character as a homogenous substring
        tempIdx = 0  # This variable will track the starting index of a homogenous substring
        
        for i in range(1, len(s)):  # Start iterating from the second character
            if s[i] == s[tempIdx]:
                cnt += i - tempIdx  # Add the number of new homogenous substrings formed
            else:
                tempIdx = i  # Update tempIdx to the current character's index if it's different
        
        return cnt % (10**9 + 7)  # Return the result modulo 10^9 + 7
