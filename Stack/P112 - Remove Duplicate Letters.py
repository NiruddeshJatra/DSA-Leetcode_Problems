# Time Complexity: O(n), where n is the length of the string `s`. Each character is processed once, and the stack operations (push and pop) take O(1) time on average. Thus, the overall complexity is linear.
# Space Complexity: O(n), where n is the number of unique characters in the string. This space is used by the stack, `lastOccurance`, and `visited` set.

# INTUITION:
# The problem asks us to remove duplicate letters from a string such that the resulting string is the smallest lexicographical order possible while preserving the order of the characters.
# 
# **Key Insight**: 
# - We need to construct the result with the smallest possible characters while ensuring each character appears only once.
# - To do this, we can use a **stack** to build the final string while ensuring lexicographical order. The stack allows us to remove characters that might appear later and can be replaced by a smaller character.
# - Additionally, we maintain a set `visited` to track the characters already included in the result and a dictionary `lastOccurance` to keep track of the last index each character appears in the string.
#
# **Greedy Choice**: 
# - If a smaller character than the one at the top of the stack appears and the current character can still appear later (i.e., it has not yet reached its last occurrence), we can remove the character at the top of the stack to make room for the smaller character.
# - If the character has already been added to the result (tracked by `visited`), we skip it to avoid duplicates.

# ALGO:
# 1. **Track Last Occurrences**: 
#    - Create a dictionary `lastOccurance` to record the last position of each character in the string.
# 2. **Iterate Over Characters**: 
#    - Traverse each character in the string.
#    - If the character is already in the result (tracked by `visited`), skip it.
# 3. **Use Stack to Maintain Lexicographical Order**:
#    - While the current character is smaller than the top of the stack and the top character can appear later (i.e., its last occurrence is after the current index), remove the top of the stack.
# 4. **Update Stack and Set**:
#    - Append the current character to the stack and add it to the `visited` set to avoid duplicates.
# 5. **Return the Result**:
#    - Join the characters in the stack to form the resulting string.

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # Step 1: Record the last occurrence of each character
        lastOccurance = {}
        for i in range(len(s)):
            lastOccurance[s[i]] = i

        # Step 2: Initialize a set for visited characters and a stack for the result
        visited = set()
        stack = []

        # Step 3: Traverse the string
        for i in range(len(s)):
            # If the character is already in the result, skip it
            if s[i] in visited:
                continue

            # Step 4: Ensure lexicographical order by popping larger characters
            while stack and s[i] < stack[-1] and lastOccurance[stack[-1]] > i:
                visited.remove(stack.pop())

            # Step 5: Add the current character to the stack and mark it as visited
            stack.append(s[i])
            visited.add(s[i])

        # Step 6: Return the result as a string
        return "".join(stack)
