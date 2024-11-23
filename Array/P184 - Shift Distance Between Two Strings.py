# Time Complexity: O(n * m), where n is the length of the strings `s` and `t`, and m is the size of the `nextCost` or `previousCost` arrays.  
# - For each character in `s` (of length n), we calculate the cost of shifting from one character to another.  
# - In the worst case, we may traverse the entire `nextCost` or `previousCost` array (of size m) for each character.  
# - Thus, the total complexity is O(n * m).  

# Space Complexity: O(1), as we use a constant amount of extra space.  
# - The cost of shifting between characters is calculated iteratively without storing intermediate results.

# INTUITION:  
# The problem involves determining the minimum cost to convert string `s` into string `t` by shifting characters either forward or backward.  
# - Each character in `s` can be shifted to another character in `t` at a specific cost determined by `nextCost` and `previousCost`.  
# - For each character, we compute the cost of shifting forward and backward, and we add the smaller of the two to the total cost.  
# - The approach ensures that the overall transformation cost is minimized by considering both shifting directions for every character.

# ALGORITHM:  
# 1. Initialize `cost` to 0 to store the total transformation cost.  
# 2. For each character in `s` and `t`:  
#    - Calculate the starting index `start` (character in `s`) and the target index `end` (character in `t`).  
#    - If `start <= end`:  
#      - Compute the forward shift cost as the sum of `nextCost[start:end]`.  
#      - Compute the backward shift cost as the sum of `previousCost` values for the wrap-around.  
#    - If `start > end`:  
#      - Compute the forward shift cost as the sum of `nextCost` values for the wrap-around.  
#      - Compute the backward shift cost as the sum of `previousCost[end+1:start+1]`.  
#    - Add the minimum of the forward and backward costs to `cost`.  
# 3. Return the total `cost`.

from typing import List

class Solution:
    def shiftDistance(self, s: str, t: str, nextCost: List[int], previousCost: List[int]) -> int:
        totalCost = 0

        for i in range(len(s)):
            # Calculate the positions in the alphabet
            start = ord(s[i]) - ord('a')
            end = ord(t[i]) - ord('a')

            if start <= end:
                # Forward and backward costs for characters from `start` to `end`
                forwardCost = sum(nextCost[start:end])
                backwardCost = sum(previousCost[:start+1]) + sum(previousCost[end+1:])
            else:
                # Wrap-around costs for characters when `start > end`
                forwardCost = sum(nextCost[start:]) + sum(nextCost[:end])
                backwardCost = sum(previousCost[end+1:start+1])

            # Add the minimum of forward or backward cost
            totalCost += min(forwardCost, backwardCost)

        return totalCost


# Example Usage:
# solution = Solution()
# s = "abc"
# t = "bcd"
# nextCost = [1] * 26
# previousCost = [2] * 26
# print(solution.shiftDistance(s, t, nextCost, previousCost))  # Example Output: 3
