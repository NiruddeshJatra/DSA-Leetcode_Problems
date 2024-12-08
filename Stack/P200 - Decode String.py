# Time Complexity: O(n), where n is the length of the string `s`.  
# - Each character in the string is pushed and popped from the stack at most once.  
# - Concatenation of strings during decoding takes linear time relative to the size of the substrings.  
# Therefore, the overall time complexity is O(n).

# Space Complexity: O(n), where n is the length of the string `s`.  
# - The stack may hold all characters of the input string in the worst case.  
# Thus, the space complexity is O(n).

# INTUITION:  
# The task is to decode a string that uses the format `k[encoded_string]`, where `k` is the number of times the `encoded_string` should be repeated.  
# The decoding process can be achieved using a stack:  
# 1. Push characters into the stack until encountering a closing bracket `]`.  
# 2. When `]` is found, extract the encoded substring and its multiplier `k` from the stack.  
# 3. Decode the substring by repeating it `k` times and push the result back onto the stack.  
# 4. At the end, the stack will contain the fully decoded string.  
# This approach ensures that nested patterns are decoded correctly by resolving the innermost patterns first (last-in, first-out).

# ALGO:  
# 1. Initialize an empty stack to store characters and partial results.  
# 2. Iterate through each character in the input string `s`:  
#    - If the character is not `]`, push it onto the stack.  
#    - If the character is `]`, perform the following:  
#      - Extract the encoded substring by popping characters until encountering `[`.  
#      - Extract the multiplier `k` by popping digits from the stack.  
#      - Decode the substring by repeating it `k` times and push the result back onto the stack.  
# 3. Finally, join all characters in the stack to form the fully decoded string.  
# 4. Return the decoded string.

from typing import List

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        
        # Iterate through the characters in the string
        for ch in s:
            # Push characters onto the stack until we encounter ']'
            if ch != ']':
                stack.append(ch)
            else:
                # Extract the encoded substring
                temp = ''
                while stack[-1] != '[':
                    temp = stack.pop() + temp
                stack.pop()  # Remove '[' from the stack

                # Extract the multiplier 'k'
                k = ''
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k

                # Decode the substring and push it back onto the stack
                stack.append(int(k) * temp)

        # Join all characters in the stack to form the decoded string
        return ''.join(stack)
