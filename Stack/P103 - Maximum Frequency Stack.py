"""
### Problem
Design a stack-like data structure that allows you to push integers and retrieve the most frequent element. If there is a tie, the most recent element among the most frequent elements is returned.

### Intuition
To efficiently manage and retrieve the most frequent elements, we can use two `defaultdict`s:
1. **freq**: Tracks the frequency of each element.
2. **group**: Groups elements by their frequency.

Additionally, a variable `maxFreq` keeps track of the current maximum frequency of any element in the stack.

### Approach
1. **Initialization**:
   - `freq`: `defaultdict` of integers to track frequencies of elements.
   - `group`: `defaultdict` of lists to store elements grouped by their frequencies.
   - `maxFreq`: Keeps track of the highest frequency of elements present.

2. **Push Operation**:
   - Increment the frequency of the pushed element in `freq`.
   - Append the element to the list in `group` corresponding to its new frequency.
   - Update `maxFreq` if the new frequency of the element is greater than the current `maxFreq`.

3. **Pop Operation**:
   - Retrieve the most frequent element from `group` using `maxFreq`.
   - Decrement the frequency of the retrieved element in `freq`.
   - If no elements are left in the list for `maxFreq` in `group`, decrement `maxFreq`.

### Time Complexity
- Push Operation: O(1)
- Pop Operation: O(1)

### Space Complexity
O(n), where n is the number of elements in the stack, due to the space needed to store elements in `group` and `freq`.

### Code
"""

from collections import defaultdict

class FreqStack:

    def __init__(self):
        self.group = defaultdict(list)
        self.freq = defaultdict(int)
        self.maxFreq = 0

    def push(self, val: int) -> None:
        self.freq[val] += 1
        self.group[self.freq[val]].append(val)
        self.maxFreq = max(self.maxFreq, self.freq[val])

    def pop(self) -> int:
        ans = self.group[self.maxFreq].pop()
        self.freq[ans] -= 1
        if not self.group[self.maxFreq]:
            self.maxFreq -= 1
        return ans

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
