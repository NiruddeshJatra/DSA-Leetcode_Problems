# Time Complexity: O(n), where n is the length of the string `s`. We iterate through the string to build the frequency count, and then iterate through the frequency dictionary to calculate the result.
# Space Complexity: O(1), because although we use a `Counter` to store character frequencies, the size of the alphabet (number of unique characters) is constant and independent of the input size, so it does not scale with the input string length.

# INTUITION:
# The task is to find the length of the longest possible palindrome that can be formed using the characters from the string `s`. 
# - A palindrome is a string that reads the same forward and backward.
# - To build the longest palindrome, we want to use as many pairs of characters as possible. Characters that appear an even number of times can be fully used. Characters that appear an odd number of times can be used in pairs, with one of them potentially being the center of the palindrome.
#
# **Key Insight**:
# - For every character with an even frequency, we can use all its occurrences.
# - For characters with odd frequencies, we can use all but one (to keep the count even), and we can place one character in the center of the palindrome.
# - If there’s at least one character with an odd frequency, we can add 1 to the total length (for the center character).

# ALGO:
# 1. **Calculate Frequency**:
#    - Use a `Counter` to calculate the frequency of each character in the string `s`.
# 2. **Initialize Variables**:
#    - `ans` to store the length of the longest palindrome we can construct.
#    - `odd` to track whether we have encountered any character with an odd frequency.
# 3. **Iterate Over Character Frequencies**:
#    - If a character's frequency is even, add its count to `ans`.
#    - If a character's frequency is odd, add the largest even part of its count (i.e., `freq[i] - 1`) to `ans`, and set `odd = 1` to account for a possible center character.
# 4. **Adjust for the Center**:
#    - If any character had an odd frequency, add 1 to `ans` to account for the center character.
# 5. **Return the Result**:
#    - Return the total length of the palindrome.

from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        # Step 1: Calculate the frequency of each character
        freq = Counter(s)

        # Step 2: Initialize variables
        ans = 0  # Stores the length of the longest palindrome
        odd = 0  # Tracks if we have encountered an odd frequency character

        # Step 3: Iterate over the frequency counts
        for i in freq:
            if freq[i] % 2 == 0:
                # Step 3.1: Add the full count if it is even
                ans += freq[i]
            else:
                # Step 3.2: If odd, add the largest even part and set odd = 1
                odd = 1
                ans += freq[i] - 1

        # Step 4: Adjust for the center of the palindrome (if any odd frequency exists)
        if odd:
            return ans + 1

        # Step 5: Return the result
        return ans
