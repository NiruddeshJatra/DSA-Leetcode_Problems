# Time Complexity:
# - O(N log N) where N is number of intervals
# - Sorting takes O(N log N)
# - Single pass through intervals is O(N)

# Space Complexity:
# - O(1) as we only store maxEnd variable
# - Sorting is typically done in-place for built-in sort
# - No additional data structures used

# INTUITION:
# To check if a person can attend all meetings, we need to ensure no
# two meetings overlap. By sorting by end time and checking each meeting's
# start time against previous meeting's end time, we can detect any overlap.
#
# Example:
# [(0,30), (5,10), (15,20)]
# Sort by end time -> [(5,10), (15,20), (0,30)]
# 1. maxEnd = 10
# 2. 15 > 10, maxEnd = 20
# 3. 0 < 20 -> Found overlap, return False

# ALGO:
# 1. If empty list, return True (no conflicts)
# 2. Sort intervals by end time
# 3. Keep track of max end time seen so far
# 4. For each interval:
#    - If start < maxEnd, found overlap -> return False
#    - Otherwise update maxEnd
# 5. Return True if no overlaps found

class Solution:
   def canAttendMeetings(self, intervals: List[Interval]) -> bool:
       # Empty case - no conflicts possible
       if not intervals:
           return True
           
       # Sort intervals by end time
       intervals.sort(key=lambda x: x.end)
       
       # Track latest end time
       latestEndTime = intervals[0].end
       
       # Check each interval for overlap
       for interval in intervals[1:]:
           currentStart = interval.start
           currentEnd = interval.end
           
           # Check if current meeting starts before previous ends
           if currentStart < latestEndTime:
               return False
               
           # Update latest end time
           latestEndTime = currentEnd
           
       return True
