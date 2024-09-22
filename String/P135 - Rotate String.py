# Time Complexity: O(n), where n is the length of the string s. The key operation is checking if goal is a substring of s + s, which takes O(n) time.
# The string concatenation of s + s also takes O(n), and the length comparison between s and goal is O(1).

# Space Complexity: O(n), because we are creating a new string s + s, which has a length of 2n.

# INTUITION:
# The idea is to check if we can rotate string `s` to match the string `goal`. A simple observation is that a rotation of `s` will always be a substring of `s + s`.
# For example, if s = "abcde", then rotating it yields strings like "bcdea", "cdeab", etc., and all of these rotations will be substrings of "abcdeabcde".
# Hence, we check if `goal` is a substring of `s + s` and if the lengths of `s` and `goal` are equal.

# ALGO:
# 1. First, check if the lengths of `s` and `goal` are equal. If they are not, return False since two strings of different lengths cannot be rotations of each other.
# 2. If their lengths are equal, concatenate `s` with itself (i.e., s + s).
# 3. Check if `goal` is a substring of `s + s`. If it is, return True; otherwise, return False.

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        # Step 1: Check if lengths of s and goal are equal
        if len(s) == len(goal):
            # Step 2: Check if goal is a substring of s + s
            if goal in s + s:
                return True
        # Step 3: If lengths are not equal or goal is not a substring of s + s, return False
        return False
