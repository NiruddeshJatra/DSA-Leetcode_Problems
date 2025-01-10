# Time Complexity:
# - O(N log N), where N is the number of cars
# - Sorting the cars by position takes O(N log N)
# - After sorting, we do one pass through cars array which is O(N)

# Space Complexity:
# - O(N) to store the sorted pairs of position and speed
# - The zip operation creates a new list of tuples

# INTUITION:
# Cars form a fleet when a faster car catches up to a slower car ahead of it.
# Processing cars from right to left (highest to lowest position) is ideal because:
# 1. Cars can only catch up to cars ahead of them
# 2. Once cars form a fleet, they continue at the speed of the slowest car
# 3. Time to reach target determines if cars will form a fleet
# 4. Cars starting further right (closer to target) determine fleet formation

# ALGO:
# 1. Sort cars by position in descending order (right to left)
# 2. For each car:
#    - Calculate time to reach target = (target - position) / speed
#    - If current car takes longer than previous car:
#      * It forms a new fleet (can't catch up)
#      * Increment fleet count
#      * Update previous time to current time
# 3. Return total number of fleets

class Solution:
   def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
       # Combine position and speed into pairs and sort by position (descending)
       car_info = sorted(zip(position, speed), reverse=True)
       
       fleet_count = 0
       prev_arrival_time = 0
       
       # Process cars from right to left
       for pos, spd in car_info:
           # Calculate time for current car to reach target
           current_arrival_time = (target - pos) / spd
           
           # If current car is slower than previous fleet,
           # it forms a new fleet
           if current_arrival_time > prev_arrival_time:
               fleet_count += 1
               prev_arrival_time = current_arrival_time
               
       return fleet_count
