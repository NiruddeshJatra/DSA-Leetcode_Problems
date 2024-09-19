# Time Complexity: O(n^3), where n is the number of elements in `nums`. The outer two loops run in O(n^2) and the two-pointer approach inside runs in O(n).
# Space Complexity: O(n), since we use a set `res` to store the unique quadruplets.

# INTUITION:
# The goal is to find all unique quadruplets in the list `nums` that sum up to a given target.
# We can achieve this by sorting the array and using a two-pointer approach for the innermost two variables while iterating over the outer two with nested loops.

# ALGO:
# 1. Sort the input array `nums` to enable the use of the two-pointer technique.
# 2. Use two nested loops for the first two elements of the quadruplet.
# 3. For the remaining two elements, use two pointers (`k` and `l`), one starting after the second loop index and the other starting at the end of the list.
# 4. Adjust the pointers based on the sum of the four elements:
#    - If the sum is greater than the target, decrement the `l` pointer to reduce the sum.
#    - If the sum is less than the target, increment the `k` pointer to increase the sum.
#    - If the sum equals the target, add the quadruplet to the result set and move both pointers inward.
# 5. Use a set `res` to avoid duplicates.

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # Step 1: Sort the input array
        nums.sort()
        res = set()  # Use a set to avoid duplicate quadruplets
        
        # Step 2: Outer loops for the first two numbers
        for i in range(len(nums) - 3):
            for j in range(i + 1, len(nums) - 2):
                
                # Step 3: Two-pointer approach for the remaining two numbers
                k, l = j + 1, len(nums) - 1
                while k < l:
                    four_sum = nums[i] + nums[j] + nums[k] + nums[l]
                    
                    if four_sum > target:
                        l -= 1  # Decrease sum by moving `l` to the left
                    elif four_sum < target:
                        k += 1  # Increase sum by moving `k` to the right
                    else:
                        # Step 4: Found a quadruplet
                        res.add((nums[i], nums[j], nums[k], nums[l]))
                        k += 1  # Move both pointers inward after finding a valid quadruplet
                        l -= 1
        
        # Step 5: Convert the set to a list and return it
        return list(res)
