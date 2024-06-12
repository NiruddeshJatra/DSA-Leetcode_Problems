"""
### Problem
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order. The mapping of digit to letters is as follows (just like on the telephone buttons):

- 2: "abc"
- 3: "def"
- 4: "ghi"
- 5: "jkl"
- 6: "mno"
- 7: "pqrs"
- 8: "tuv"
- 9: "wxyz"

### Intuition
To generate all possible letter combinations for the given digits, we can use backtracking. For each digit in the input string, we map it to the corresponding set of letters and recursively build combinations by exploring all possibilities.

### Approach
1. **Base Case**: If the input string `digits` is empty, return an empty list.
2. **Backtracking Function**: Define a recursive function `combination` to build the letter combinations:
   - If the length of the temporary combination `temp` matches the length of the input `digits`, add the combination to the result list `ans`.
   - Iterate through each character mapped to the current digit and recursively build the combination.
   - Backtrack by removing the last added character and continue exploring other possibilities.
3. **Initialize**: Start the backtracking process with the first digit.
4. **Return**: Return the result list containing all possible combinations.

### Time Complexity
The time complexity is \(O(4^n)\), where \(n\) is the length of the input string `digits`. Each digit can map to up to 4 letters, leading to 4 possibilities per digit.

### Space Complexity
The space complexity is \(O(n)\) due to the recursion stack and the temporary list used for building combinations.

### Algorithm
1. Define the `combination` function:
   - If the length of `temp` matches the length of `digits`, append the current combination to `ans`.
2. Iterate through each character mapped to the current digit:
   - Add the character to `temp`.
   - Recursively call `combination` with the next digit index.
   - Backtrack by removing the character.
3. Initialize and start the backtracking process.
4. Return the result list.
"""

from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        ans, temp = [], []
        letterMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        def combination(index):
            if len(temp) == len(digits):
                ans.append("".join(temp))
                return

            for char in letterMap[digits[index]]:
                temp.append(char)
                combination(index + 1)
                temp.pop()

        combination(0)
        return ans
