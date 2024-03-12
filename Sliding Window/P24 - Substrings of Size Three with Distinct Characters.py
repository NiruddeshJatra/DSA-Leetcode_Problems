class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        # Time Complexity: O(n)
        # Space Complexity: O(1) - Since the size of the set is fixed

        # INTUITION:
        # We iterate through the string 's' and check each substring of length 3.
        # If all characters in the substring are distinct, we increment the count.

        # ALGO:
        # 1. Initialize a variable 'ans' to count the good substrings.
        # 2. Iterate through the string from index 0 to len(s) - 3:
        #     2.1 Check if the substring of length 3 starting from the current index has all distinct characters.
        #     2.2 If all characters are distinct, increment 'ans'.
        # 3. Return 'ans'.

        ans = 0  # Initialize count of good substrings to 0
        for i in range(len(s) - 2):  # Loop through the string up to the third last index
            if len(set(s[i:i + 3])) == 3:  # Check if the substring of length 3 has all distinct characters
                ans += 1  # Increment count if all characters are distinct
        return ans  # Return count of good substrings
