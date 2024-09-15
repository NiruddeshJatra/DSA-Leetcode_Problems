# Time Complexity: O(n^2), where n is the length of the array `nums`. Sorting the array takes O(n log n), and the nested loops contribute O(n^2) for the two-pointer search.
# Space Complexity: O(1) (ignoring the space used by sorting), because we are only using a constant amount of extra space for the pointers and counters.

# INTUITION:
# The problem is to find how many triplets of indices (i, j, k) can form a triangle with side lengths `nums[i]`, `nums[j]`, and `nums[k]`. For a triangle to be valid, the sum of any two sides must be greater than the third side.
#
# **Key Insight**:
# - If we sort the array, we can simplify the triangle condition:
#     - If `nums[i] + nums[j] > nums[k]`, then since the array is sorted (`nums[i] <= nums[j] <= nums[k]`), the other two conditions (`nums[i] + nums[k] > nums[j]` and `nums[j] + nums[k] > nums[i]`) will automatically hold.
# - Thus, after sorting, we only need to check if `nums[i] + nums[j] > nums[k]` for valid triangles.

# ALGO:
# 1. **Sort the Array**:
#    - First, sort the array and filter out any zero or negative values since they can't be sides of a triangle.
# 2. **Use a Two-pointer Approach**:
#    - For each element `nums[k]` (starting from the largest side and moving leftwards), use two pointers `i` (starting from the left) and `j` (starting just before `k`) to find pairs of `nums[i]` and `nums[j]` such that `nums[i] + nums[j] > nums[k]`.
#    - If such a pair is found, all values from `i` to `j` can form a triangle with `nums[k]` (because the array is sorted), so we increment the count by `j - i`.
#    - If no valid pair is found, adjust the pointers accordingly.
# 3. **Return the Total Count of Valid Triangles**:
#    - After processing all possible combinations, return the total count.

class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        # Step 1: Sort the array and filter out non-positive values
        nums = sorted([i for i in nums if i > 0])
        
        # Step 2: Initialize count to 0
        cnt = 0
        
        # Step 3: Use a two-pointer approach to find valid triangles
        for k in range(len(nums) - 1, 1, -1):
            j = k - 1
            i = 0
            while i < j:
                # Step 3.1: Check if the current triplet can form a triangle
                if nums[i] + nums[j] > nums[k]:
                    # If true, all pairs from i to j can form a triangle with nums[k]
                    cnt += j - i
                    j -= 1
                else:
                    i += 1
        
        # Step 4: Return the total count of valid triangles
        return cnt
