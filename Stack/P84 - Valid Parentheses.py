"""
### Problem
Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid. An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.

### Intuition
To determine if the string `s` containing brackets is valid, we can use a stack to keep track of the opening brackets. As we iterate through the string, we push each opening bracket onto the stack. For each closing bracket, we check if it matches the most recent opening bracket by popping from the stack. If the stack is empty when we encounter a closing bracket or if the closing bracket does not match the top of the stack, the string is not valid.

### Approach
1. **Stack Initialization**: Initialize an empty stack to keep track of the opening brackets.
2. **Iterate Through the String**: Loop through each character in the string `s`.
   - If the character is an opening bracket (`'('`, `'{'`, `'['`), push it onto the stack.
   - If the character is a closing bracket (`')'`, `'}'`, `']'`), check if the stack is not empty and if the top of the stack is the corresponding opening bracket:
     - If so, pop the top of the stack.
     - If not, return False because the brackets are not balanced or correctly ordered.
3. **Final Stack Check**: After processing all characters, if the stack is not empty, return False because there are unmatched opening brackets. Otherwise, return True.

### Time Complexity
The time complexity is O(n), where `n` is the length of the string `s`. We traverse the string once and perform constant-time operations (push, pop, check) for each character.

### Space Complexity
The space complexity is O(n) in the worst case, where `n` is the length of the string `s`. This is because, in the worst case, all characters in the string could be opening brackets, requiring the stack to store all of them.

### Algorithm
1. Initialize an empty stack.
2. Loop through each character in the string:
   - If the character is an opening bracket, push it onto the stack.
   - If the character is a closing bracket, check if it matches the top of the stack. If it does, pop the stack; otherwise, return False.
3. After the loop, check if the stack is empty. If it is, return True; otherwise, return False.
"""

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in "({[":
                stack.append(c)
            elif stack and ((c == ")" and stack[-1] == '(') or (c == "}" and stack[-1] == '{') or (c == "]" and stack[-1] == '[')):
                stack.pop()
            else:
                return False

        return not stack
