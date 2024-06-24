"""
### Problem
Given a positive integer `n`, you need to find the smallest integer which has exactly the same digits existing in the integer `n` and is greater in value than `n`. If no such positive integer exists, return `-1`.

### Intuition
The problem is essentially about finding the next permutation of the given number's digits. The next permutation is the lexicographically smallest permutation that is greater than the current permutation.

### Approach
1. **Find the First Decreasing Element from the End**:
   - Traverse the list of digits from the end and find the first element that is smaller than its next element. Let's call this index `i - 1`.

2. **If No Such Element Exists**:
   - If no such element is found, it means the digits are in descending order, so return `-1` because no greater permutation exists.

3. **Find the Element Just Larger Than `digits[i - 1]`**:
   - Traverse the list from the end again to find the smallest element that is larger than `digits[i - 1]` and swap them.

4. **Reverse the Suffix**:
   - Reverse the sequence from `i` to the end of the list to get the smallest permutation that is greater than the original number.

5. **Convert to Integer and Check Range**:
   - Convert the list of digits back to an integer and check if it fits within the 32-bit integer range. If it doesn't, return `-1`.

### Algorithm
1. Convert the integer `n` to a list of its digits.
2. Traverse the list from the end to find the first decreasing element.
3. If no such element exists, return `-1`.
4. Traverse the list from the end to find the element just larger than the decreasing element.
5. Swap the two elements.
6. Reverse the part of the list after the first decreasing element.
7. Convert the list back to an integer.
8. Check if the integer is within the 32-bit range.
9. Return the integer if valid, else return `-1`.

### Time Complexity
The time complexity is O(n), where n is the number of digits in the integer, due to the single pass to find the decreasing element, a pass to find the element to swap, and a pass to reverse the suffix.

### Space Complexity
The space complexity is O(n) due to storing the digits of the number.

### Code
"""

class Solution:
    def nextGreaterElement(self, n: int) -> int:
        digits = list(str(n))  # Convert the integer to a list of its digits
        i = len(digits) - 1
        
        # Find the first decreasing element from the end
        while i > 0 and digits[i] <= digits[i - 1]:
            i -= 1

        # If no such element is found, return -1
        if i == 0:
            return -1

        # Find the element just larger than digits[i - 1]
        j = len(digits) - 1
        while digits[j] <= digits[i - 1]:
            j -= 1

        # Swap the elements at i-1 and j
        digits[i - 1], digits[j] = digits[j], digits[i - 1]
        
        # Reverse the sequence from i to the end
        digits = digits[:i] + digits[i:][::-1]
        
        # Convert the list back to an integer
        ans = int("".join(digits))
        
        # Check if the result is within the 32-bit integer range
        if ans > 2**31 - 1:
            return -1
        return ans
