
# Time Complexity: O(n^2)
# Space Complexity: O(1) (excluding the space required for the output list)

# INTUITION:
# This function finds all unique triplets in the array 'nums' whose sum is zero. It first sorts the array to easily 
# handle duplicates. Then, it iterates through the array while fixing one element as the target 'num' and using 
# two pointers approach to find pairs that sum up to the negative of 'num'.

# ALGORITHM:
# 1. Sort the array 'nums' in ascending order.
# 2. Initialize an empty list 'ans' to store the unique triplets.
# 3. Iterate through the array 'nums' using enumerate:
#    3.1 Skip the current iteration if the current number is the same as the previous number to avoid duplicates.
#    3.2 Initialize two pointers 'l' and 'r' to find pairs that sum up to the negative of the current number.
#    3.3 While 'l' is less than 'r':
#        3.3.1 If the sum of 'nums[l]' and 'nums[r]' is less than the negative of 'num', increment 'l'.
#        3.3.2 If the sum is greater, decrement 'r'.
#        3.3.3 If the sum is equal, append the triplet [num, nums[l], nums[r]] to 'ans'.
#              Increment 'l' and skip duplicate numbers from the left.
# 4. Return the list of unique triplets 'ans'.

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        for index, num in enumerate(nums):
            if index > 0 and num == nums[index-1]:
                continue
            l, r = index+1, len(nums) - 1
            while l < r:
                if nums[l] + nums[r] < -num:
                    l += 1
                elif nums[l] + nums[r] > -num:
                    r -= 1
                else:
                    ans.append([num, nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
        return ans
