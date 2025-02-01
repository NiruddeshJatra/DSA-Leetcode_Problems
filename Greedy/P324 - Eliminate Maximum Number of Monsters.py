# Time Complexity:
# - O(NlogN) due to sorting
# - Creating timeToReach array is O(N)
# - Iterating through timeToReach is O(N)
# - Overall complexity is O(NlogN)

# Space Complexity:
# - O(N) for storing timeToReach array
# - No additional space used other than input

# INTUITION:
# For each monster, we can calculate when it will reach city
# We want to eliminate monsters that reach earliest first
# Example: dist=[3,2,4], speed=[5,3,2]
# Times = [0.6, 0.67, 2]
# Minute 0: Kill monster at 0.6 (closest)
# Minute 1: Kill monster at 0.67
# Minute 2: Kill monster at 2
# We survive! Answer = 3

# ALGO:
# 1. Calculate arrival time for each monster (dist/speed)
# 2. Sort arrival times ascending
# 3. For each minute i:
#    - If monster arrives before/at minute i, we die
#    - If we can kill it before arrival, increment count
# 4. Return number of monsters killed

def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
   # Calculate time each monster takes to reach city
   arrivalTimes = [distance/velocity for distance, velocity in zip(dist, speed)]
   
   # Sort by arrival time
   arrivalTimes.sort()
   
   # Count monsters we can eliminate
   monstersKilled = 1  # We can always kill first monster
   
   # Check each monster starting from second one
   for minute in range(1, len(arrivalTimes)):
       # If monster arrives before or at current minute
       if arrivalTimes[minute] <= minute:
           # We cannot kill it in time
           break
       # We can kill this monster
       monstersKilled += 1
   
   return monstersKilled
