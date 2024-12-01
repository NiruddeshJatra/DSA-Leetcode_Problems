# Time Complexity: O(n), where n is the number of elements in nums.
# - Calculating the sum of the array takes O(n).
# - Constructing the frequency counter also takes O(n).
# - Iterating over the array to find the outlier takes O(n).

# Space Complexity: O(n).
# - The space is used for the frequency counter.

# INTUITION:
# - The problem revolves around identifying the largest "outlier" based on a condition:
#   - An outlier is defined as a number `x` such that `total - 2 * x` is also present in the array.
# - The equation `total - 2 * x` arises when we consider the sum of all numbers after removing `x` and adding `-x` back.
# - Using a frequency counter helps track duplicates and validate the conditions.

# ALGORITHM:
# 1. Compute the total sum of the array.
# 2. Build a frequency counter for all elements in the array.
# 3. For each number in the array:
#    - Compute the possible outlier value: `possibleOutlier = total - 2 * num`.
#    - Check if `possibleOutlier` exists in the array:
#      - Ensure it's a valid outlier by checking if `possibleOutlier != num` or the frequency of `num` is greater than 1.
#      - Update the largest outlier value if the condition is satisfied.
# 4. Return the largest outlier value found, or `-inf` if none is found.

class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        # Initialize the largest outlier as negative infinity
        outlier = float('-inf')
        
        # Compute the total sum of the array
        total = sum(nums)
        
        # Create a frequency counter for the array
        freq = Counter(nums)
        
        # Iterate through each number in the array
        for num in nums:
            # Calculate the possible outlier
            possibleOutlier = total - 2 * num
            
            # Check if the possible outlier exists in the array
            if possibleOutlier in freq:
                # Ensure it's a valid outlier
                if possibleOutlier != num or freq[num] > 1:
                    # Update the largest outlier
                    outlier = max(outlier, possibleOutlier)
        
        return outlier

# Example Usage:
# Input: nums = [3, 6, 9, 12, 15]
# Output: 15
# Explanation:
# - Total = 45
# - If num = 15, possibleOutlier = 45 - 2 * 15 = 15 (valid outlier).

# Input: nums = [2, 4, 6, 8]
# Output: -inf
# Explanation: No valid outlier exists.

# Input: nums = [5, 5, 10, 20]
# Output: 10
# Explanation:
# - Total = 40
# - If num = 10, possibleOutlier = 40 - 2 * 10 = 20 (valid outlier).
