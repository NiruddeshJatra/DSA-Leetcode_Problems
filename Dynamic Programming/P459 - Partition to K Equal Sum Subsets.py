# Time Complexity:
# - O(k * 2^n), where n is the number of elements in the array and k is the number of subsets
# - In the worst case, we need to try all possible subsets of the array
# - Optimizations like sorting and early pruning improve average case performance

# Space Complexity:
# - O(n) for the recursion stack and the used array to track elements
# - n is the number of elements in the array

# INTUITION:
# The problem asks if we can partition the array into k subsets with equal sum
# Key insights:
# - Find the target sum for each subset (total sum divided by k)
# - Use backtracking to explore different ways to form these subsets
# - Apply optimizations to prune the search space quickly
# Example:
# arr = [4,3,2,3,5,2,1], k = 4
# Total sum = 20, target sum for each subset = 5
# One valid partition: [1,4], [2,3], [2,3], [5]

# ALGO:
# 1. Check if the sum is divisible by k, if not, return false
# 2. Sort the array in descending order for better pruning
# 3. Use backtracking to form k subsets with equal sum:
#    - Track used elements with boolean array
#    - When current subset sum equals target, move to next subset
#    - Apply pruning techniques:
#      * Skip used elements
#      * Skip if adding current element exceeds target
#      * Skip duplicate elements in certain cases
# 4. Return true if all subsets can be formed

class Solution:
   def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
       # Calculate the total sum and target sum for each subset
       totalSum = sum(nums)
       
       # Early check: if total sum is not divisible by k, it's impossible
       if totalSum % k != 0:
           return False
       
       targetSum = totalSum // k
       
       # Check if any element is larger than the target sum
       if max(nums) > targetSum:
           return False
       
       # Sort array in descending order for better pruning
       nums.sort(reverse=True)
       
       # Initialize array to track used elements
       used = [False] * len(nums)
       
       def backtrack(remainingSubsets, startIndex, currentSum):
           # Base case: all subsets have been formed
           if remainingSubsets == 0:
               return True
               
           # If current subset is complete, start a new one
           if currentSum == targetSum:
               return backtrack(remainingSubsets - 1, 0, 0)
           
           # Try adding each remaining element to current subset
           for i in range(startIndex, len(nums)):
               # Skip if element is already used
               if used[i]:
                   continue
                   
               # Skip if adding this element would exceed target sum
               if currentSum + nums[i] > targetSum:
                   continue
                   
               # Skip duplicates in certain cases to avoid redundant exploration
               if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                   continue
               
               # Use this element
               used[i] = True
               
               # Recursively try to complete the current subset
               if backtrack(remainingSubsets, i + 1, currentSum + nums[i]):
                   return True
               
               # Backtrack: unuse this element
               used[i] = False
               
               # Early termination for first element in a subset
               if currentSum == 0:
                   break
           
           # No valid solution found for this path
           return False
       
       # Start the backtracking process
       return backtrack(k, 0, 0)
