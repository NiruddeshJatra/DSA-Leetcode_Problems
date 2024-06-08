# INTUITION:
# The problem can be approached using backtracking to explore all possible combinations of the given candidates that sum up to the target value.

# ALGO:
# 1. Initialize an empty list `ans` to store the final combinations and `temp` to store the current combination.
# 2. Define a recursive function `backtrack(start, sum)`:
#     2.1 If `sum` equals `target`, append a copy of the current combination `temp` to `ans`.
#     2.2 If `sum` exceeds `target`, return as no further exploration is needed.
#     2.3 Iterate through `candidates` starting from the `start` index.
#         2.3.1 Include `candidates[i]` in `temp` and update `sum`.
#         2.3.2 Call `backtrack(i, sum)` to continue exploring further elements (including the current element again).
#         2.3.3 Backtrack by removing the last element added to `temp` and subtracting its value from `sum`.
# 3. Start the recursion with `backtrack(0, 0)`.
# 4. Return `ans` containing all valid combinations.

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        temp, ans = [], []
        sum = 0

        def backtrack(start, sum):
            if target == sum:
                ans.append(temp[:])
                return

            if target < sum:
                return

            for i in range(start, len(candidates)):
                temp.append(candidates[i])
                sum += candidates[i]
                backtrack(i, sum)
                temp.pop()
                sum -= candidates[i]

        backtrack(0, sum)
        return ans
