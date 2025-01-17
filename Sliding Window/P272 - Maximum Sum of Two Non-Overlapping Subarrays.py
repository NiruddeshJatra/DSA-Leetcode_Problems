# Time Complexity: 
# - O(N), where N is the length of nums array
# - We do two passes through the array, each taking O(N) time

# Space Complexity:
# - O(1), we only use a constant amount of extra space regardless of input size
# - We maintain a few variables for sums and results

# INTUITION:
# The problem requires finding two non-overlapping subarrays of given lengths that maximize their sum.
# The key insight is to:
# 1. Use sliding window technique to compute sums of consecutive elements
# 2. For each position of the second window, keep track of the maximum sum
#    encountered so far for the first window
# 3. Try both arrangements (firstLen followed by secondLen and vice versa)
#    since optimal solution could be in either order

# ALGORITHM:
# 1. Create helper function maxSum(first, second) that:
#    - Initializes sliding windows for both subarrays
#    - Maintains maximum sum seen so far for first window
#    - Slides both windows through array updating sums and max result
# 2. Return maximum of two possible arrangements:
#    - firstLen length subarray followed by secondLen length subarray
#    - secondLen length subarray followed by firstLen length subarray

class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        def maxSum(firstLength: int, secondLength: int) -> int:
            # Initialize sums for both windows
            firstWindowSum = secondWindowSum = 0
            
            # Calculate initial sums for both windows
            for i in range(firstLength + secondLength):
                if i < firstLength:
                    firstWindowSum += nums[i]
                else:
                    secondWindowSum += nums[i]
            
            # Keep track of maximum sum for first window and overall result
            maxFirstWindowSum = firstWindowSum
            currentResult = firstWindowSum + secondWindowSum
            
            # Slide both windows through the array
            for i in range(firstLength + secondLength, len(nums)):
                # Update first window sum by adding new element and removing oldest
                firstWindowSum += nums[i - secondLength] - nums[i - secondLength - firstLength]
                # Update maximum sum seen so far for first window
                maxFirstWindowSum = max(maxFirstWindowSum, firstWindowSum)
                
                # Update second window sum by adding new element and removing oldest
                secondWindowSum += nums[i] - nums[i - secondLength]
                # Update result if current combination gives better sum
                currentResult = max(currentResult, maxFirstWindowSum + secondWindowSum)
            
            return currentResult
        
        # Try both possible arrangements and return the better result
        return max(maxSum(firstLen, secondLen), maxSum(secondLen, firstLen))
