# Time Complexity: O(n), where n is the length of the input array `nums`.
# We traverse the array to create the frequency counter and another time to construct the result list.

# Space Complexity: O(n), where n is the length of the input array `nums`.
# The space is used for storing the frequency counter.

# INTUITION:
# The problem involves identifying "lonely" numbers, defined as numbers that:
# 1. Appear exactly once in the array.
# 2. Have no adjacent numbers in the array (i.e., `n-1` and `n+1` are absent).
# By using a frequency counter (`hashmap`), we can efficiently check both conditions:
# - If `hashmap[n] == 1`, the number appears exactly once.
# - If `hashmap[n+1]` and `hashmap[n-1]` are both 0, it means there are no adjacent numbers.
# This approach avoids nested loops and ensures optimal performance.

# ALGO:
# 1. Use `Counter` to build a frequency map (`hashmap`) for all numbers in `nums`.
# 2. Iterate through `nums` and check for each number `n`:
#    - If `hashmap[n] == 1` (it is unique).
#    - If `hashmap[n+1] + hashmap[n-1] == 0` (no adjacent numbers).
# 3. Add numbers meeting both conditions to the result list.
# 4. Return the result list.

from typing import List
from collections import Counter

class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        frequencyMap = Counter(nums)

        return [num for num in nums if frequencyMap[num] == 1 and frequencyMap[num + 1] + frequencyMap[num - 1] == 0]
