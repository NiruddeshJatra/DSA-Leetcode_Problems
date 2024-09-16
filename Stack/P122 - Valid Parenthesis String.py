# Time Complexity: O(n), where n is the length of the string `s`. We loop through the string twice—once to process the parentheses and asterisks and once to validate the remaining unpaired left parentheses.
# Space Complexity: O(n), due to the use of two stacks to store the indices of `(` and `*` characters.

# INTUITION:
# The string `s` contains three types of characters: '(', ')', and '*'. The '*' can be interpreted as either '(', ')' or an empty string. Our task is to determine whether the given string can be valid, meaning that every closing parenthesis has a corresponding opening parenthesis in the correct order.
#
# **Key Insight**:
# - Keep track of the positions of both '(' and '*' characters.
# - Try to match ')' with either a '(' or '*' from earlier in the string.
# - After matching, ensure that any remaining unmatched '(' can be paired with '*' later in the string.

# ALGO:
# 1. **Track Positions of '(' and '*'**:
#    - Use two stacks: one for the indices of '(' and one for the indices of '*'.
# 2. **Iterate Through the String**:
#    - For each character in the string:
#      - If it's '(', add its index to the `left` stack.
#      - If it's '*', add its index to the `asterisk` stack.
#      - If it's ')', first try to match it with a '(' from the `left` stack. If no '(' is available, match it with a '*' from the `asterisk` stack. If neither is available, the string is invalid, so return `False`.
# 3. **Check Remaining Unmatched '('**:
#    - After the first pass, if there are still unmatched '(' in the `left` stack, attempt to match them with '*' from the `asterisk` stack.
#    - If any unmatched '(' cannot be matched with a later '*', return `False`.
# 4. **Return True If All Valid**:
#    - If all parentheses can be successfully matched, return `True`.

class Solution:
    def checkValidString(self, s: str) -> bool:
        # Step 1: Initialize two lists to track the positions of '(' and '*'
        left = []
        asterisk = []

        # Step 2: Iterate through each character in the string
        for i, ch in enumerate(s):
            if ch == '*':
                # Track the index of '*' in the `asterisk` list
                asterisk.append(i)
            elif ch == '(':
                # Track the index of '(' in the `left` list
                left.append(i)
            else:
                # If ')' is encountered, try to match with a '(' or '*'
                if left:
                    left.pop()  # Pop a '(' from `left` if available
                elif asterisk:
                    asterisk.pop()  # Pop a '*' from `asterisk` if no '(' is available
                else:
                    # No matching '(' or '*' to balance the ')'
                    return False

        # Step 3: Try to match any remaining '(' with '*' after all ')' have been processed
        while left and asterisk:
            # If a '(' appears after a '*', the string is invalid
            if left.pop() > asterisk.pop():
                return False

        # Step 4: Return True if all '(' have been matched, otherwise return False
        return not left
