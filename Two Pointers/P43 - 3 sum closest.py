# Time Complexity: O(n^2)
# Space Complexity: O(1)

# INTUITION:
# This function finds the triplet in the array 'nums' whose sum is closest to the target integer 'target'. 
# It utilizes a two-pointer approach to explore all possible triplets, sorting the array first to easily handle duplicates.
# The function initializes 'ans' to a large value, then iterates through the array while fixing one number as 'num', 
# and using two pointers to find the other two numbers whose sum with 'num' is closest to 'target'.

# ALGORITHM:
# 1. Sort the array 'nums' to easily handle duplicates.
# 2. Initialize 'ans' to a large value (e.g., 10^18).
# 3. Iterate through the array 'nums' using enumerate:
#    3.1 Skip the current iteration if the current number is the same as the previous number to avoid duplicates.
#    3.2 Initialize two pointers 'l' and 'r' at indices 'index + 1' and 'len(nums) - 1' respectively.
#    3.3 While 'l' is less than 'r':
#        3.3.1 Calculate the current sum 'currentSum' as 'nums[l] + nums[r] + num'.
#        3.3.2 If 'currentSum' is less than 'target', increment 'l'.
#        3.3.3 If 'currentSum' is greater than 'target', decrement 'r'.
#        3.3.4 Update 'ans' if the absolute difference between 'target' and 'currentSum' is less than the 
#              absolute difference between 'target' and 'ans'.
# 4. Return 'ans', which represents the sum of the triplet closest to 'target'.

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans = 10**18
        for index, num in enumerate(nums):
            if index > 0 and num == nums[index-1]:
                continue
            l, r = index + 1, len(nums) - 1
            while l < r:
                currentSum = nums[l] + nums[r] + num
                if currentSum < target:
                    l += 1
                else:
                    r -= 1
                if abs(target - currentSum) < abs(target - ans):
                    ans = currentSum
        return ans
