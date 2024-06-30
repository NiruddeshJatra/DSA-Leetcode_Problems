"""
### Problem
Remove `k` digits from the number `num` to make it the smallest possible.

### Intuition
Use a stack to maintain the digits of the smallest possible number. Remove elements from the stack if they are greater than the current digit and `k` is not zero.

### Approach
1. **Iterate through the digits**:
   - If the current digit is smaller than the top of the stack, pop the stack to maintain a smaller number.
   - Push the current digit onto the stack.
   - Decrement `k` for each pop.
2. **Trim the stack**:
   - If `k` is still positive, remove additional digits from the end.
3. **Convert to string**:
   - Join the stack into a string.
   - Remove leading zeros.
   - Return "0" if the result is empty.

### Time Complexity
O(n), where n is the length of `num`.

### Space Complexity
O(n), for the stack storing the digits.

### Code
"""

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for i in range(len(num)):
            while stack and k and num[i] < stack[-1]:
                stack.pop()
                k -= 1
            stack.append(num[i])

        if k:
            stack = stack[:-k]
        
        ans = "".join(stack).lstrip('0')
        if ans == "":
            return "0"
        return ans
