# Time Complexity:
# - O(2^(n/2) * n), where n is the total number of elements in the array.
# - We generate all subsets of the first half and second half, which takes O(2^(n/2)).
# - We sort one of the arrays and perform binary search, adding another factor of n.

# Space Complexity:
# - O(2^(n/2)), as we store all possible subset sums for both halves of the array.

# INTUITION:
# This problem asks us to partition the array into two subsets with equal size (n/2 elements each)
# such that the absolute difference between their sums is minimized.
#
# A brute force approach would be to check all possible ways to select n elements, but this would be
# O(2^n), which is too slow. Instead, we can use the "meet in the middle" technique:
#
# 1. Split the array into two halves of size n/2 each.
# 2. Generate all possible subset sums for both halves.
# 3. For each subset of size k from the first half, look for a complementary subset of size (n/2 - k)
#    from the second half such that their combined sum is as close as possible to totalSum/2.
#
# For example, with array [3,9,7,3]:
# - Split into [3,9] and [7,3]
# - For first half: we can select 1 element (3 or 9) or 2 elements [3,9]
# - For second half: similar selections
# - If we pick [3] from first half, we need to pick [3] from second half to have equal sizes
# - This gives partition [3,3] and [9,7] with difference |6-16| = 10
# - We check all such valid combinations to find the minimum difference

# ALGO:
# 1. Split the array into two halves of size n/2 each.
# 2. Generate all possible subset sums for both halves, organized by subset size.
# 3. For each subset size k from the first half:
#    a. Find complementary subsets of size (n/2 - k) from the second half
#    b. Sort the second half's subset sums for binary search
#    c. For each sum from the first half, find the closest sum from the second half
#       that would make their combined sum close to totalSum/2
# 4. Return the minimum absolute difference found.

import bisect
from typing import List
from itertools import combinations

class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums) // 2  # Half of the total array length
        
        # Function to generate all possible subset sums for an array
        def generateSubsetSums(arr):
            # Dictionary to store sums by subset size
            subsetSums = {}
            
            # Generate subsets of all sizes from 1 to len(arr)
            for size in range(1, len(arr) + 1):
                subsetSums[size] = []
                # Generate all combinations of 'size' elements
                for combo in combinations(arr, size):
                    subsetSums[size].append(sum(combo))
                    
            return subsetSums
        
        # Split the array and generate subset sums for both halves
        leftHalf = nums[:n]
        rightHalf = nums[n:]
        leftSums = generateSubsetSums(leftHalf)
        rightSums = generateSubsetSums(rightHalf)
        
        totalSum = sum(nums)
        minDifference = abs(sum(leftHalf) - sum(rightHalf))  # Initialize with a valid partition
        
        # For each size k in the left half, find complementary subsets in the right half
        for leftSize in range(1, n):
            rightSize = n - leftSize  # Ensure total selected elements is n
            
            # Get sums for the current sizes
            left = leftSums[leftSize]
            right = rightSums[rightSize]
            
            # Sort right sums for binary search
            right.sort()
            
            # Target sum we want to achieve for the entire partition
            targetSum = totalSum // 2
            
            # For each sum in the left subset
            for leftSum in left:
                # Complement needed from the right subset to get close to targetSum
                desiredRightSum = targetSum - leftSum
                
                # Find the closest sum in the right subset using binary search
                index = bisect.bisect_left(right, desiredRightSum)
                
                # Check the found index
                if 0 <= index < len(right):
                    currentRightSum = right[index]
                    totalPartitionSum = leftSum + currentRightSum
                    otherPartitionSum = totalSum - totalPartitionSum
                    currentDifference = abs(totalPartitionSum - otherPartitionSum)
                    minDifference = min(minDifference, currentDifference)
                
                # Also check the previous element if it exists
                if 0 <= index - 1 < len(right):
                    currentRightSum = right[index - 1]
                    totalPartitionSum = leftSum + currentRightSum
                    otherPartitionSum = totalSum - totalPartitionSum
                    currentDifference = abs(totalPartitionSum - otherPartitionSum)
                    minDifference = min(minDifference, currentDifference)
        
        return minDifference
