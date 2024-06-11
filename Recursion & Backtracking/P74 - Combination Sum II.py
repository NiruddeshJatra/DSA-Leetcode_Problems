"""
### Problem
Given a collection of candidate numbers (`candidates`) and a target number (`target`), find all unique combinations in `candidates` where the candidate numbers sum to `target`. Each number in `candidates` may only be used once in the combination. The solution set must not contain duplicate combinations.

### Intuition
To solve this problem, we use a backtracking approach. The idea is to recursively explore all possible combinations of candidates that sum up to the target, ensuring that each candidate is used only once and avoiding duplicates by skipping over repeated elements.

### Approach
1. Sort the `candidates` list to handle duplicates easily.
2. Use a helper function `backtrack` that takes the current starting index and the current sum.
3. In the `backtrack` function:
   - If the current sum equals the target, add the current combination to the result list.
   - If the current sum exceeds the target, return.
   - Iterate through the candidates starting from the given index.
   - Skip duplicate elements to avoid duplicate combinations.
   - Recursively call `backtrack` for the next index and updated sum.

### Time Complexity
The time complexity is \(O(2^n)\), where \(n\) is the number of candidates. This is because, in the worst case, we may need to explore all possible combinations of the candidates.

### Space Complexity
The space complexity is \(O(n)\) due to the recursion stack.

### Algorithm
1. Sort the `candidates` list.
2. Define the `backtrack` function:
   - If the current sum equals the target, append the current combination to the result list.
   - If the current sum exceeds the target, return.
   - Iterate through the candidates starting from the given index.
   - Skip duplicates.
   - Recursively call `backtrack` with the next index and updated sum.
3. Call the `backtrack` function starting from index 0 and sum 0.
"""

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        temp, ans = [], []
        sum = 0
        
        def backtrack(start, sum):
            if target == sum:
                ans.append(temp[:])
                return

            if target < sum:
                return
            
            prev = -1
            for i in range(start, len(candidates)):
                if candidates[i] == prev:
                    continue
                temp.append(candidates[i])
                sum += candidates[i]
                backtrack(i + 1, sum)
                temp.pop()
                sum -= candidates[i]
                prev = candidates[i]

        candidates.sort()
        backtrack(0, sum)
        return ans
