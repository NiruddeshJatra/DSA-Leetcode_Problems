# Time Complexity:
# - O(n²), where n is the number of points.
# - We compare each point with every other point, resulting in n * (n-1) / 2 comparisons.

# Space Complexity:
# - O(n) in the worst case, where most points form different slopes with a reference point.
# - The slopes dictionary can store up to n-1 entries for each iteration.

# INTUITION:
# To find the maximum number of points on a line, we can use the fact that a line is uniquely
# determined by its slope and a point on it. For each point, we can calculate the slope it forms
# with every other point and keep track of how many points share the same slope.
#
# The key insight is that for a fixed point P, all points that form the same slope with P lie on the same line.
# By counting the frequency of each slope, we can find the maximum number of points that share a line with P.
#
# For example, if we have points (1,1), (2,2), and (3,3), they all lie on a line with slope 1.
# If we pick (1,1) as our reference point, both (2,2) and (3,3) form a slope of 1 with it.

# ALGO:
# 1. Handle edge cases: if there are ≤ 2 points, they're always collinear.
# 2. For each point p1:
#    a. Create a dictionary to count slopes.
#    b. For each other point p2:
#       i. Calculate the slope between p1 and p2 (handle vertical lines with infinity).
#       ii. Increment the count for this slope.
#       iii. Update the maximum count if needed.
# 3. Return the maximum count + 1 (to include the reference point).

class Solution:
   def maxPoints(self, points: List[List[int]]) -> int:
       # Edge case: if there are 0, 1, or 2 points, they always form a line
       if len(points) <= 2:
           return len(points)
       
       maxPointsOnLine = 1  # At least one point is always on a line
       
       # For each point, count how many other points form the same slope with it
       for i, point1 in enumerate(points):
           # Dictionary to store count of points for each slope
           slopeFrequency = defaultdict(int)
           x1, y1 = point1
           
           # Compare with all points after this one (no need to check previous points again)
           for x2, y2 in points[i+1:]:
               # Calculate slope between point1 and the current point
               if x1 - x2 == 0:
                   # Vertical line (infinite slope)
                   slope = float("inf")
               else:
                   # Normal slope calculation
                   slope = (y1 - y2) / (x1 - x2)
                   
                   # Handle negative zero and precision issues
                   if slope == 0:
                       slope = 0  # Convert -0.0 to 0.0
               
               # Count points with this slope
               slopeFrequency[slope] += 1
               
               # Update the maximum count
               maxPointsOnLine = max(maxPointsOnLine, slopeFrequency[slope])
       
       # Add 1 to include the reference point itself
       return maxPointsOnLine + 1
