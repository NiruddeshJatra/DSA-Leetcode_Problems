# INTUITION:
# This problem can be solved using backtracking. We explore all possible subsets by either including or not including each element.

# ALGO:
# 1. Initialize an empty list `ans` to store the subsets and `temp` to store the current subset.
# 2. Define a recursive function `backtrack(start)`:
#     2.1 Append a copy of the current subset `temp` to `ans`.
#     2.2 Iterate through `nums` starting from the `start` index.
#         2.2.1 Include `nums[i]` in `temp`.
#         2.2.2 Call `backtrack(i + 1)` to generate subsets including `nums[i]`.
#         2.2.3 Backtrack by removing the last element added to `temp`.
# 3. Start the recursion with `backtrack(0)`.
# 4. Return `ans` containing all the subsets.

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        temp, ans = [], []

        def backtrack(start):
            ans.append(temp[:])
            for i in range(start, len(nums)):
                temp.append(nums[i])
                backtrack(i + 1)
                temp.pop()

        backtrack(0)
        return ans
