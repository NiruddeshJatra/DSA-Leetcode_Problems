# Time Complexity: O(n), where n is the length of the string `s`. We iterate through each character in the string exactly once.
# Space Complexity: O(n), as we use a stack and the `ans` string to store intermediate characters, which could take up to `n` space in the worst case.

# INTUITION:
# The problem is to remove the outermost parentheses from every primitive part of the given valid parentheses string. 
# To solve this, we can use a stack to keep track of open parentheses. 
# We only append to the result string when we encounter inner parentheses (i.e., those that are not part of the outermost pair).

# ALGO:
# 1. Initialize an empty stack and an empty string `ans` to store the resulting parentheses string.
# 2. Loop through each character in the input string:
#    - If the character is a closing parenthesis `)`, pop the last open parenthesis from the stack and check if the stack is not empty. If it's not empty, append the closing parenthesis to `ans` (because it belongs to an inner expression).
#    - If the character is an opening parenthesis `(`, check if the stack is not empty (indicating that the current parenthesis is not part of the outermost layer). If so, append it to `ans`, and then push the current parenthesis onto the stack.
# 3. Return the final `ans` string, which contains the parentheses without the outermost parts.

class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        # Step 1: Initialize stack and answer string
        stack = []
        ans = ""
        
        # Step 2: Iterate through the input string `s`
        for ch in s:
            if ch == ')':
                # Step 3: Pop the stack when encountering a closing parenthesis
                stack.pop()
                # Step 4: Append to `ans` if the stack is not empty (not an outer parenthesis)
                if stack:
                    ans += ch
            else:
                # Step 5: Append to `ans` if the stack is not empty (not an outer parenthesis)
                if stack:
                    ans += ch
                # Step 6: Push the opening parenthesis onto the stack
                stack.append(ch)
        
        # Step 7: Return the result string `ans`
        return ans
