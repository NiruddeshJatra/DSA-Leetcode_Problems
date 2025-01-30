# Time Complexity:
# - O(N), where N is length of seats array
# - Single pass through the array

# Space Complexity:
# - O(1), using only constant extra space
# - No additional data structures needed

# INTUITION:
# Track distance between occupied seats, but need special handling
# for edges. For edges, distance is doubled since person only has
# one neighbor. For middle seats, take half of distance between
# occupied seats.

# ALGO:
# 1. Track last occupied seat position
# 2. For first occupied seat:
#    - Double distance from start (edge case)
# 3. For subsequent occupied seats:
#    - Update max distance if larger gap found
#    - Update last occupied position
# 4. Check final edge case (distance to end)
# 5. Return max distance divided by 2

class Solution:
   def maxDistToClosest(self, seats: List[int]) -> int:
       lastOccupied = -1
       maxGap = 0
       
       for currentPos in range(len(seats)):
           if seats[currentPos] == 1:
               if lastOccupied == -1:
                   # First occupied seat - edge case
                   lastOccupied = currentPos
                   maxGap = currentPos * 2
               else:
                   # Update max gap and last occupied position
                   maxGap = max(maxGap, currentPos - lastOccupied)
                   lastOccupied = currentPos
       
       # Check distance from last occupied to end
       maxGap = max(maxGap, (len(seats) - lastOccupied - 1) * 2)
       
       return maxGap // 2
