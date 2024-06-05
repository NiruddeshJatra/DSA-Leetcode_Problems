# Time Complexity: O(n), where n is the length of the string `s`.
# Space Complexity: O(n) due to the recursion stack.

# INTUITION:
# The goal is to implement the `atoi` function, which converts a string to an integer.
# This involves handling whitespace, optional signs, and numeric characters.
# We need to ignore leading whitespaces, check for optional '+' or '-' sign,
# and then convert the subsequent numeric characters into an integer.
# Any non-numeric characters after the number should terminate the conversion.
# The conversion also needs to handle integer overflow by clamping the results within the 32-bit signed integer range.

# ALGO:
# 1. Define a helper function `helper(i, digitStarted, ans)` that processes the string recursively:
#    a. Base case: If `i` reaches the end of the string, return `ans`.
#    b. If `digitStarted` is True:
#       - If the current character is a digit, update `ans` and continue.
#       - If it's not a digit, return the current value of `ans`.
#    c. If `digitStarted` is False:
#       - Skip whitespace characters.
#       - If a '+' is found, start digit conversion.
#       - If a '-' is found, start digit conversion and multiply the result by -1.
#       - If a digit is found, start digit conversion.
#       - If any other character is found, return 0.
# 2. Call the helper function starting from index 0, with `digitStarted` set to False and `ans` initialized to 0.
# 3. Clamp the final result within the 32-bit signed integer range before returning.

class Solution:
    def myAtoi(self, s: str) -> int:
        def helper(i, digitStarted, ans):
            if i == len(s):
                return ans
            if digitStarted:
                if s[i] in "0123456789": 
                    ans = ans * 10 + int(s[i])
                    return helper(i + 1, True, ans)
                else:
                    return ans
            if s[i] == " ":
                return helper(i + 1, False, ans)
            if s[i] == "+":
                return helper(i + 1, True, ans)
            if s[i] == "-":
                return (-1) * helper(i + 1, True, ans)
            if s[i] in "0123456789": 
                return helper(i + 1, True, int(s[i]))
            return 0

        ans = helper(0, False, 0)
        if ans > (2**31 - 1):
            return 2**31 - 1
        elif ans < -2**31:
            return -2**31
        else:
            return ans
