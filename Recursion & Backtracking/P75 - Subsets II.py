"""
### Problem
Given an integer array `nums` that may contain duplicates, return all possible subsets (the power set). The solution set must not contain duplicate subsets. Return the solution in any order.

### Intuition
To solve this problem, we use a backtracking approach. The idea is to recursively explore all possible subsets while ensuring that each subset is unique by skipping over duplicates.

### Approach
1. Sort the `nums` list to handle duplicates easily.
2. Use a helper function `backtrack` that takes the current starting index.
3. In the `backtrack` function:
   - Append the current subset to the result list.
   - Iterate through the `nums` starting from the given index.
   - Skip duplicate elements to avoid duplicate subsets.
   - Recursively call `backtrack` for the next index.
   - Remove the last element to backtrack.

### Time Complexity
The time complexity is \(O(2^n)\), where \(n\) is the number of elements in `nums`. This is because we may need to explore all possible subsets of the `nums`.

### Space Complexity
The space complexity is \(O(n)\) due to the recursion stack and the space needed to store the temporary list `temp`.

### Algorithm
1. Sort the `nums` list.
2. Define the `backtrack` function:
   - Append the current subset to the result list.
   - Iterate through the `nums` starting from the given index.
   - Skip duplicates.
   - Recursively call `backtrack` with the next index.
   - Remove the last element to backtrack.
3. Call the `backtrack` function starting from index 0.
"""

from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans, temp = [], []

        def backtrack(start):
            ans.append(temp[:])
            prev = -100  # Initialize to a value outside the possible range of nums
            for i in range(start, len(nums)):
                if nums[i] == prev:
                    continue
                temp.append(nums[i])
                backtrack(i + 1)
                temp.pop()
                prev = nums[i]

        nums.sort()
        backtrack(0)
        return ans
