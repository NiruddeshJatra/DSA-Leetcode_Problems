# Time Complexity: O(n^2), where n is the length of the string `s`. 
# We iterate over each character in the string and expand around every possible center, 
# which takes O(n) time for each center.

# Space Complexity: O(1), since we are only using a few extra variables to store intermediate values 
# (apart from the space required to store the final result).

# INTUITION:
# The problem is to find the longest palindromic substring. 
# A palindrome reads the same backward as forward, so we can expand around each possible center in the string.
# A palindrome can either have a single center (odd length) or two centers (even length).
# For each character (and its neighbor), we expand outward to check for the longest palindrome.

# ALGO:
# 1. Initialize `maxStr` to the first character of the string, assuming the input is non-empty.
# 2. Define a helper function `findPalindrome(left, right)` that expands around the two indices and returns the longest palindrome between them.
# 3. For each character in the string, check both odd-length and even-length palindromes by expanding around:
#    - The character itself for odd-length palindromes.
#    - The character and its next neighbor for even-length palindromes.
# 4. Update the `maxStr` whenever a longer palindrome is found.
# 5. Return `maxStr` as the result.

class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxStr = s[0]  # Initialize maxStr to the first character of the string

        def findPalindrome(left, right):
            # Expand around the center and return the longest palindrome found
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1 : right]  # Return the valid palindrome

        # Iterate over the string to check for palindromes
        for i in range(len(s) - 1):
            # Odd-length palindrome (center at i)
            odd = findPalindrome(i, i)
            # Even-length palindrome (center between i and i+1)
            even = findPalindrome(i, i+1)
        
            # Update maxStr if a longer palindrome is found
            if len(maxStr) < len(odd):
                maxStr = odd
            if len(maxStr) < len(even):
                maxStr = even

        return maxStr  # Return the longest palindromic substring
