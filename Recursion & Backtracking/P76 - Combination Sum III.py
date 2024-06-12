"""
### Problem
Given two integers `k` and `n`, find all possible combinations of `k` numbers that add up to a number `n`, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

### Intuition
To solve this problem, we can use backtracking to explore all possible combinations of numbers from 1 to 9. By ensuring that each combination is unique and that we do not reuse any number, we can efficiently find all valid combinations.

### Approach
1. **Backtracking**: Define a recursive function `combination` to build the combinations:
   - **Base Case**: If `k` reaches 0 and `n` reaches 0 simultaneously, it means we have found a valid combination, so we add it to the result list.
2. **Recursive Exploration**: For each number from the current start to 9:
   - Add the number to the current combination.
   - Recursively call `combination` with updated parameters (next start index, decremented `k`, and decremented `n`).
   - Remove the last added number to backtrack and explore the next possibility.
3. **Return**: Start the backtracking process and return the result list.

### Time Complexity
The time complexity is \(O(2^n)\) in the worst case, where \(n\) is the total numbers considered (1 through 9).

### Space Complexity
The space complexity is \(O(k)\) due to the recursion stack and the temporary list used for combinations.

### Algorithm
1. Define the `combination` function:
   - If `k` and `n` are both 0, append the current combination to the result list.
2. Iterate from the current number to 9:
   - Add the number to the combination.
   - Recursively call `combination` with updated parameters.
   - Backtrack by removing the number.
3. Initialize the backtracking process.
4. Return the result list.

### Example
```python
# Example
sol = Solution()
print(sol.combinationSum3(3, 7))  # Output: [[1, 2, 4]]
print(sol.combinationSum3(3, 9))  # Output: [[1, 2, 6], [1, 3, 5], [2, 3, 4]]
"""

from typing import List

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        temp, ans = [], []
        def combination(start, k, n):
        if k == 0 and n == 0:
            ans.append(temp[:])
            return

        for i in range(start, 10):
            temp.append(i)
            combination(i + 1, k - 1, n - i)
            temp.pop()

    combination(1, k, n)
    return ans

