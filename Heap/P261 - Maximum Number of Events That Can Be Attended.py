# Time Complexity:
# - O(N log N) for sorting events array where N is number of events
# - O(N log N) for heap operations (push/pop) in worst case
# - Total: O(N log N)

# Space Complexity:
# - O(N) for the min heap that could store at most N events at a time
# - Original events array is modified in-place, so no extra space needed there

# INTUITION:
# To maximize attended events, we should:
# 1. Process events day by day and always attend earliest ending events first
# 2. Use a min heap to efficiently track and select earliest ending available events
# 3. Only keep events in heap that can still be attended (end date >= current day)
# A sorted array + min heap gives optimal solution because:
# - Sorting lets us process events in chronological order
# - Min heap gives us O(log N) access to earliest ending event each day
# - Removing expired events keeps heap size minimal

# ALGORITHM:
# 1. Sort events by start date (in reverse to pop from end)
# 2. For each day:
#    - If no current events available, jump to next event's start date
#    - Add all events that start on/before current day to min heap
#    - Attend earliest ending event (top of min heap)
#    - Remove any events that can no longer be attended
#    - Move to next day
# 3. Continue until no more events can be processed

class Solution:
   def maxEvents(self, events: List[List[int]]) -> int:
       # Sort events by start date in reverse 
       # (reverse lets us pop from end in O(1))
       events.sort(reverse=True)
       
       # Track current day and events we've attended
       currentDay = 0
       attendedCount = 0
       
       # Min heap stores end dates of available events
       availableEvents = []
       
       # Process while we have either:
       # - Events yet to start
       # - Events available to attend
       while events or availableEvents:
           # If no events available, jump to next event's start
           if not availableEvents:
               currentDay = events[-1][0]
               
           # Add all events that start today or earlier
           while events and currentDay >= events[-1][0]:
               startDate, endDate = events.pop()
               heapq.heappush(availableEvents, endDate)
               
           # Attend event with earliest end date
           heapq.heappop(availableEvents)
           attendedCount += 1
           currentDay += 1
           
           # Remove events that can no longer be attended
           while availableEvents and currentDay > availableEvents[0]:
               heapq.heappop(availableEvents)
       
       return attendedCount
