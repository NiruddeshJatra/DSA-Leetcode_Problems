"""
### Problem
Given a string that contains only digits `num` and an integer `target`, add operators (`+`, `-`, `*`) between the digits so that the resulting expression evaluates to the target value. Return all possible expressions that evaluate to the target value.

### Intuition
To solve this problem, we can use a backtracking approach to try out all possible combinations of operators between the digits and evaluate the expressions. By keeping track of the current sum and the previous number used in the expression, we can handle the different precedence rules of the operators.

### Approach
1. **Backtracking Function**:
    - **Base Case**: If we have reached the end of the string and the current sum matches the target, add the current expression to the result list.
    - **Loop through Digits**: For each position in the string, form the current number and decide whether to:
        - **Start a New Expression**: If we are at the start of the string, initialize the expression with the current number.
        - **Add an Operator**: Otherwise, try adding `+`, `-`, and `*` before the current number and recursively continue building the expression.
    - **Avoid Leading Zeros**: Skip numbers with leading zeros.

2. **Handling Multiplication**:
    - For multiplication, subtract the previous number added to the sum and add the result of multiplying the previous number with the current number. This ensures correct precedence handling.

3. **Initialize Backtracking**: Start the backtracking process from the beginning of the string with an empty expression and initial sums set to zero.

### Time Complexity
The time complexity is exponential in the length of the string due to the number of possible combinations of operators.

### Space Complexity
The space complexity is O(n) due to the recursion stack and the space used to store the current expression.

### Code
"""
from typing import List

class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        ans = []

        def backtrack(start, expression, curSum, prevNum):
            if start == len(num):
                if target == curSum:
                    ans.append(expression)
                return

            for i in range(start, len(num)):
                if i > start and num[start] == "0":
                    break
                curNum = int(num[start : i + 1])
                if start == 0:
                    backtrack(i + 1, expression + str(curNum), curSum + curNum, curNum)
                else:
                    backtrack(
                        i + 1, expression + "+" + str(curNum), curSum + curNum, curNum
                    )
                    backtrack(
                        i + 1, expression + "-" + str(curNum), curSum - curNum, -curNum
                    )
                    backtrack(
                        i + 1,
                        expression + "*" + str(curNum),
                        curSum - prevNum + (prevNum * curNum),
                        prevNum * curNum
                    )

        backtrack(0, "", 0, 0)
        return ans
