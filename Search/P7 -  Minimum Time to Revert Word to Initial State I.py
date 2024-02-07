# Time Complexity: O(n), where n is the length of the input word.
# Space Complexity: O(1)

# INTUITION:
# The code aims to find the minimum number of steps required to reach the initial state 
# by removing characters from the end of the word in steps of 'k'. It checks if the 
# substring obtained after removing characters matches the remaining substring at the 
# beginning of the word. If it does, it returns the current step count; otherwise, it 
# continues until all characters are removed.

# ALGO:
# 1. Initialize variables: 'n' to store the length of the input word, 'i' and 'time' to 
#    keep track of the current position and step count, 'removedStr' to store the removed 
#    substring, and 'newStr' to store the remaining substring after removal.
# 2. Iterate while 'i' is less than 'n':
#    2.1. Increment 'i' by 'k'.
#    2.2. Update 'newStr' with the substring starting from index 'i'.
#    2.3. Increment 'time' to indicate a step.
#    2.4. Check if 'newStr' is equal to the substring obtained by removing characters 
#         from the beginning of the word up to length 'n - i':
#         2.4.1. If true, return 'time'.
# 3. Return 'time' if no match is found.

class Solution:
    def minimumTimeToInitialState(self, word: str, k: int) -> int:
        n = len(word)  # Length of the input word.
        i, time = 0, 0  # Initialize position and step count.
        removedStr = ""  # Initialize removed substring.
        newStr = ""  # Initialize remaining substring.
        while i < n:
            i += k  # Increment 'i' by 'k'.
            newStr = word[i:]  # Update 'newStr' with remaining substring.
            time += 1  # Increment step count.
            if newStr == word[:n - i]:  # Check if remaining substring matches prefix.
                return time  # If match found, return current step count.
        return time  # Return step count if no match found.
