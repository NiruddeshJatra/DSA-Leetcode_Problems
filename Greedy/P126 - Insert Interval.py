# Time Complexity: O(n), where n is the number of intervals. We are iterating through all the intervals once.
# Space Complexity: O(n), as we are storing the result in separate lists for left, right, and the merged interval.

# INTUITION:
# We want to insert a new interval into a list of non-overlapping intervals such that the list remains sorted and non-overlapping after insertion. To do this, we can categorize the intervals into three groups:
# 1. Intervals completely to the left of the new interval (those whose end is before the start of the new interval).
# 2. Intervals completely to the right of the new interval (those whose start is after the end of the new interval).
# 3. Intervals that overlap with the new interval (those that we need to merge).

# ALGO:
# 1. Initialize three lists: `left` to store intervals completely before the new interval, `right` to store intervals completely after the new interval, and a variable for merging overlapping intervals.
# 2. Loop through all the intervals:
#    2.1 If an interval's end is less than the start of the new interval, append it to `left`.
#    2.2 If an interval's start is greater than the end of the new interval, append it to `right`.
#    2.3 If an interval overlaps with the new interval, adjust the new interval's start and end to include the overlapping interval.
# 3. After the loop, return the merged list by concatenating the `left` list, the merged interval, and the `right` list.

def insert(self, intervals, newInterval):
    s, e = newInterval.start, newInterval.end
    left, right = [], []
    
    # Step 2: Loop through the existing intervals
    for i in intervals:
        # If the interval ends before the new interval starts, it belongs to the left
        if i.end < s:
            left += i,
        # If the interval starts after the new interval ends, it belongs to the right
        elif i.start > e:
            right += i,
        # If the interval overlaps with the new interval, adjust the start and end
        else:
            s = min(s, i.start)
            e = max(e, i.end)
    
    # Step 3: Return the concatenated result
    return left + [Interval(s, e)] + right
