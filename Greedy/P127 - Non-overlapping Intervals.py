# Time Complexity: O(n log n), where n is the number of intervals. Sorting the intervals takes O(n log n), and then we iterate through them in O(n).
# Space Complexity: O(1), as we're using a constant amount of extra space, not including the input.

# INTUITION:
# The goal is to remove the minimum number of intervals such that no two intervals overlap. 
# By sorting intervals by their end times, we can greedily select intervals that finish earlier and thus leave more room for future intervals to fit without overlapping.

# ALGO:
# 1. First, we sort the intervals by their end time. This is because the earlier an interval ends, the more space it leaves for the next interval.
# 2. We initialize `end` to the smallest possible value (`float('-inf')`) and start counting overlaps.
# 3. For each interval:
#    - If the start time of the current interval is less than `end`, it means the current interval overlaps with the previous one, so we increment the count of removed intervals.
#    - If it does not overlap, we update `end` to the end time of the current interval.
# 4. Finally, return the count of intervals that need to be removed.

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Step 1: Sort intervals by their end times
        intervals.sort(key=lambda x: x[1])
        
        # Step 2: Initialize variables for tracking
        ans = 0
        end = float('-inf')  # Initialize to negative infinity for comparisons
        
        # Step 3: Iterate through the intervals
        for i in intervals:
            # If the current interval overlaps with the previous one
            if i[0] < end:
                ans += 1  # Increment the count of intervals to remove
            else:
                end = i[1]  # Update the end time to the current interval's end
        
        # Step 4: Return the number of intervals to be removed
        return ans
