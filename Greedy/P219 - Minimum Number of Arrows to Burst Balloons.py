# Time Complexity:
# - O(N log N), where N is the number of balloons
#   - Sorting the points array takes O(N log N)
#   - The single pass through the array takes O(N)
#   - Overall complexity is dominated by the sorting: O(N log N)

# Space Complexity:
# - O(1), only using primitive variables (arrows, end)
#   - The sort is typically done in-place 
#   - No additional data structures are created

# INTUITION:
# This is a classic interval merging problem where:
# - Each balloon is represented by its start and end coordinates [start, end]
# - An arrow can burst multiple balloons if it intersects with all of them
# - We want to find minimum number of arrows needed
# By sorting balloons by start position and keeping track of intersection points,
# we can greedily find the minimum arrows needed

# ALGO:
# 1. Sort balloons by their start positions
# 2. Initialize arrows count to 1 and end point to first balloon's end
# 3. For each subsequent balloon:
#    - If current end >= balloon's start:
#      * Update end to min(current end, balloon's end) to maintain intersection
#    - Else:
#      * Need new arrow, increment arrows count
#      * Update end to current balloon's end
# 4. Return total arrows needed

class Solution:
   def findMinArrowShots(self, points: List[List[int]]) -> int:
       # Sort balloons by start position
       points.sort()
       # Initialize with first arrow
       arrows = 1
       # Track the rightmost point that current arrow can reach
       end = points[0][1]
       
       # Process remaining balloons
       for point in points[1:]:
           if end >= point[0]:
               # Balloons overlap, update intersection point
               end = min(end, point[1])
           else:
               # Need new arrow
               arrows += 1
               end = point[1]

       return arrows
