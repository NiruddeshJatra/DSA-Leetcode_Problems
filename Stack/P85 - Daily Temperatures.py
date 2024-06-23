"""
### Problem
Given a list of daily temperatures `temperatures`, return a list `answer` such that `answer[i]` is the number of days you have to wait after the `i`-th day to get a warmer temperature. If there is no future day for which this is possible, keep `answer[i]` == 0 instead.

### Intuition
To solve the problem of finding how many days until a warmer temperature, we can use a stack to keep track of the indices of the days. By using a stack, we can efficiently keep track of the temperatures in a way that allows us to quickly find the next warmer day for each day in the input list.

### Approach
1. **Initialize the Answer List**: Create a list `ans` of the same length as `temperatures`, initialized to 0, to store the results.
2. **Stack Initialization**: Initialize an empty stack to keep track of the indices of the temperatures.
3. **Iterate Through Temperatures**: Loop through each temperature in the list:
   - While the stack is not empty and the current temperature is higher than the temperature at the index of the top of the stack:
     - Pop the index from the stack.
     - Calculate the difference between the current index and the popped index and store it in the answer list at the position of the popped index.
   - Push the current index onto the stack.
4. **Return the Result**: After processing all temperatures, return the answer list.

### Time Complexity
The time complexity is O(n), where `n` is the length of the list `temperatures`. Each index is pushed and popped from the stack at most once.

### Space Complexity
The space complexity is O(n) in the worst case, where `n` is the length of the list `temperatures`. This is due to the stack storing indices.

### Algorithm
1. Initialize the answer list `ans` with zeros.
2. Initialize an empty stack.
3. Loop through the list `temperatures` with index `i`.
   - While the stack is not empty and the temperature at the top of the stack is less than the current temperature:
     - Pop the index from the stack.
     - Calculate the difference between the current index and the popped index.
     - Store the difference in the answer list at the position of the popped index.
   - Push the current index onto the stack.
4. Return the answer list `ans`.
"""

from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                index = stack.pop()
                ans[index] = i - index
            stack.append(i)
        return ans
