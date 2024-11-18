# Time Complexity: O(n), where `n` is the length of the string `s`.  
# - We iterate through the string once, performing constant-time operations for each character.

# Space Complexity: O(1).  
# - The algorithm uses a fixed amount of extra space for variables, irrespective of the input size.

# INTUITION:  
# The task is to find the maximum number of vowels in any substring of length `k`.  
# A **sliding window** technique is ideal for this problem, as it allows us to dynamically evaluate the number of vowels in the current substring without recomputing from scratch.  
# Using a fixed-size window of `k`, we slide across the string, adjusting the vowel count for characters entering and leaving the window.  
# This method is efficient because:  
# 1. It avoids recalculating the vowel count for overlapping substrings.  
# 2. We only need to perform a constant amount of work for each character in the string.

# ALGORITHM:  
# 1. Initialize variables:  
#    - `vowelCount` to track the current number of vowels in the window.  
#    - `ans` to store the maximum number of vowels found.  
#    - `left` pointer to track the start of the window.  
# 2. Iterate through the string using the `right` pointer:  
#    - If `s[right]` is a vowel, increment `vowelCount`.  
#    - Once the window reaches size `k`:  
#       - Update `ans` with the maximum value of `vowelCount`.  
#       - If `s[left]` (leaving the window) is a vowel, decrement `vowelCount`.  
#       - Move the `left` pointer to maintain the window size.  
# 3. Return `ans` as the maximum number of vowels found.

from typing import List

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowelCount = 0  # Count of vowels in the current window
        maxVowels = 0  # Maximum vowels in any window of size `k`
        leftPointer = 0  # Start of the sliding window

        for rightPointer in range(len(s)):
            # Add the current character to the window
            if s[rightPointer] in "aeiou":
                vowelCount += 1

            # Check if the window size is `k`
            if rightPointer - leftPointer + 1 == k:
                # Update the maximum number of vowels
                maxVowels = max(maxVowels, vowelCount)

                # Remove the character leaving the window
                if s[leftPointer] in "aeiou":
                    vowelCount -= 1

                # Slide the window
                leftPointer += 1

        return maxVowels
