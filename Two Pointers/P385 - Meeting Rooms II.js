// Time Complexity:
// - O(N log N) where N is number of intervals
// - Sorting start and end times takes O(N log N) each
// - Single pass through sorted arrays is O(N)

// Space Complexity:
// - O(N) for storing sorted start and end arrays
// - O(1) for count variables and array indices

// INTUITION:
// At any point in time, number of rooms needed = overlap count
// By sorting start and end times separately, we can:
// 1. Keep track of ongoing meetings by incrementing count at each start time
// 2. Decrement count at each end time
// 3. Maximum count at any point is minimum rooms needed
//
// Example:
// intervals = [(0,30),(5,10),(15,20)]
// start = [0,5,15]
// end = [10,20,30]
// t=0: count=1
// t=5: count=2
// t=10: count=1
// t=15: count=2
// t=20: count=1
// t=30: count=0
// Max count = 2 rooms needed

// ALGO:
// 1. Extract and sort start times and end times separately
// 2. Use two pointers to track current start and end indices
// 3. For each time point:
//    - If start time is earlier, increment room count
//    - Otherwise decrement room count (meeting ended)
// 4. Track maximum count seen so far
// 5. Return maximum count as minimum rooms needed

class Solution {
   /**
    * @param {Interval[]} intervals - Array of meeting intervals
    * @returns {number} - Minimum number of rooms required
    */
   minMeetingRooms(intervals) {
       // Extract and sort start/end times
       const startTimes = intervals.map(interval => interval.start)
                                 .sort((a, b) => a - b);
       const endTimes = intervals.map(interval => interval.end)
                               .sort((a, b) => a - b);
       
       let roomCount = 0;          // Current room count
       let maxRooms = 0;           // Maximum rooms needed
       let startIndex = 0;         // Current start time index
       let endIndex = 0;           // Current end time index
       
       // Process all meetings
       while (startIndex < intervals.length) {
           // If next start is before next end, need new room
           if (startTimes[startIndex] < endTimes[endIndex]) {
               startIndex++;
               roomCount++;
           }
           // Otherwise meeting ended, free up room
           else {
               endIndex++;
               roomCount--;
           }
           
           // Update maximum rooms needed
           maxRooms = Math.max(maxRooms, roomCount);
       }
       
       return maxRooms;
   }
}
