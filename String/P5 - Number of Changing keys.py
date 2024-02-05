# Time Complexity: O(n), where n is the length of the input string 's'.
# Space Complexity: O(1)

# INTUITION:
# The code converts the input string to lowercase and then iterates through it, 
# counting the number of times the character changes from one position to the next. 
# This effectively counts the number of "key changes" in the string.

# ALGO:
# 1. Convert the input string to lowercase.
# 2. Initialize a variable 'count' to 0 to keep track of the number of key changes.
# 3. Iterate through the string using a for loop over the range from 1 to the length of the string.
#    3.1. If the current character is different from the previous character, increment 'count'.
# 4. Return the final value of 'count', which represents the number of key changes.

class Solution:
    def countKeyChanges(self, s: str) -> int:
        s = s.lower()  # Convert the input string to lowercase.
        count = 0  # Initialize a variable to keep track of key changes.
        for i in range(1, len(s)):
            if s[i] != s[i - 1]:  # Check if the current character is different from the previous one.
                count += 1  # Increment the count if a key change is detected.
        return count  # Return the count of key changes.
