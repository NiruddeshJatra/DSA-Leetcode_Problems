"""
### Problem
Given a string `s`, partition `s` such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of `s`.

### Intuition
To generate all possible palindrome partitions for the given string, we can use backtracking. For each position in the string, we consider every possible substring starting from that position, and if the substring is a palindrome, we recursively build partitions by exploring all possibilities.

### Approach
1. **Base Case**: If the current index `i` is equal to the length of the string `s`, add the current partition to the result list `ans`.
2. **Backtracking Function**: Define a recursive function `backtrack` to build the partitions:
   - If the current index `i` reaches the length of the string `s`, append the current partition `part` to `ans`.
   - Iterate through each possible substring starting from the current index `i` to the end of the string.
   - Check if the substring is a palindrome.
   - If it is, add it to the current partition and recursively call `backtrack` for the next index.
   - Backtrack by removing the last added substring and continue exploring other possibilities.
3. **Initialize**: Start the backtracking process with the first character.
4. **Return**: Return the result list containing all possible partitions.

### Time Complexity
The time complexity is O(n * 2^n), where n is the length of the string `s`. This is because in the worst case, each character could potentially be a partition point, resulting in 2^n possible partitions, and checking if a substring is a palindrome takes O(n) time.

### Space Complexity
The space complexity is O(n) due to the recursion stack used in the backtracking process and the temporary list used for building partitions.

### Algorithm
1. Define the `backtrack` function:
   - If the current index `i` equals the length of `s`, append the current partition to `ans`.
   - Iterate through each possible substring starting from `i`:
     - Check if the substring is a palindrome.
     - If it is, add the substring to the current partition.
     - Recursively call `backtrack` with the next index.
     - Backtrack by removing the last added substring.
2. Initialize and start the backtracking process.
3. Return the result list.
"""

from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans, part = [], []
        
        def backtrack(i):
            if i == len(s):
                ans.append(part[:])
                return

            for j in range(i, len(s)):
                temp = s[i:j+1]
                if temp == temp[::-1]:
                    part.append(temp)
                    backtrack(j+1)
                    part.pop()

        backtrack(0)
        return ans
