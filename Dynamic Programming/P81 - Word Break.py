"""
### Problem
Given a string `s` and a dictionary of strings `wordDict`, return true if `s` can be segmented into a space-separated sequence of one or more dictionary words.

### Intuition
We can use dynamic programming to solve the problem efficiently. The idea is to use a memoization table to store the results of subproblems, thereby avoiding redundant computations.

### Approach
1. **Memoization**: Use a dictionary `memo` to store the results of subproblems.
2. **Recursive Backtracking**: Define a recursive function `backtrack(i)` that checks if the substring starting at index `i` can be segmented.
   - If `i` is already in `memo`, return the stored result.
   - If `i` equals the length of the string `s`, return True since we have successfully segmented the entire string.
   - Iterate over each word in `wordDict` and check if the substring starting at `i` matches the word.
   - If a match is found, recursively call `backtrack` with the index `i + len(word)`.
   - If the recursive call returns True, store the result in `memo` and return True.
   - If no match is found, store False in `memo` for the index `i`.
3. **Return Result**: Start the recursion from index 0 and return the result.

### Time Complexity
The time complexity is O(n * m), where `n` is the length of the string `s` and `m` is the average length of words in `wordDict`.

### Space Complexity
The space complexity is O(n) due to the memoization dictionary.

### Code
"""

from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}
        
        def backtrack(i):
            if i in memo:
                return memo[i]
            if i == len(s):
                return True

            for word in wordDict:
                if s.startswith(word, i) and backtrack(i + len(word)):
                    memo[i] = True
                    return True

            memo[i] = False
            return False

        return backtrack(0)

