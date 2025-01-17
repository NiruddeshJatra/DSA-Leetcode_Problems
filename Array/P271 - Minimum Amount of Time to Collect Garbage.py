# Time Complexity:
# - O(N * K) where N is number of houses and K is average length of garbage strings
# - Each character in each house is counted
# - Travel array traversed up to 3 times (once per truck)

# Space Complexity:
# - O(1) as we only use constant extra space
# - No additional data structures needed

# INTUITION:
# To minimize collection time, each truck should:
# 1. Only travel to houses that have its type of garbage
# 2. Stop at the last house containing its garbage type
# 3. Count time for both collection and travel
# 
# Process each truck separately because:
# - They can move independently
# - Only need to go to houses with their garbage type
# - Can optimize travel by finding last occurrence

# ALGORITHM:
# For each garbage type (P,G,M):
# 1. Scan houses right-to-left to find last occurrence
# 2. Count collection time for each piece of garbage
# 3. Add travel time for path to last needed house
# 4. Sum up times for all three trucks

class Solution:
   def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
       totalTime = 0
       
       # Process each type of garbage truck
       for truckType in 'PGM':  # Paper, Glass, Metal
           # Flag to track if we've found any garbage of this type
           hasGarbage = False
           
           # Scan houses right to left
           for houseIndex in range(len(garbage) - 1, -1, -1):
               # Count collection time for current house
               if truckType in garbage[houseIndex]:
                   hasGarbage = True
                   totalTime += garbage[houseIndex].count(truckType)
               
               # Add travel time if we need to reach this house
               if hasGarbage and houseIndex > 0:
                   totalTime += travel[houseIndex - 1]
       
       return totalTime
