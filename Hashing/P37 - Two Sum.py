# Time Complexity: O(n)
# Space Complexity: O(n)

# INTUITION:
# This function finds two numbers in the array 'nums' that add up to the target sum 'target'. It utilizes a dictionary 
# 'indices' to store the indices of numbers encountered so far. While iterating through the array, it checks if the 
# complement of the current number with respect to the target is present in the 'indices' dictionary. If found, it 
# returns the indices of both numbers; otherwise, it updates the 'indices' dictionary.

# ALGORITHM:
# 1. Initialize an empty dictionary 'indices' to store the indices of numbers encountered so far.
# 2. Iterate through the array 'nums' using enumerate to track the index and value of each number:
#    2.1 Calculate the complement of the current number with respect to the target.
#    2.2 Check if the complement exists in the 'indices' dictionary:
#        2.2.1 If found, return the indices of both numbers.
#    2.3 Update the 'indices' dictionary with the current number and its index.
# 3. If no solution is found, return an empty list.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}
        for index, num in enumerate(nums):
            if target - num in indices:
                return [indices[target-num], index]
            indices[num] = index
        return []
