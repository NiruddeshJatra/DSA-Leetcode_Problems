# Time Complexity:
# - O(N + B) where N is number of flights and B is number of bookings
#   - Iterating through bookings: O(B)
#   - Prefix sum calculation: O(N)
#   - No sorting or other operations needed

# Space Complexity:
# - O(N) for the answer array
#   - Uses N+1 space to handle boundary cases
#   - No other significant space usage

# INTUITION:
# This is a difference array / prefix sum problem because:
# - Multiple ranges need updating 
# - Each booking affects a continuous range
# - We can mark start and end points
# Using difference array lets us:
# - Add value at start index
# - Subtract at end+1 index
# - Running sum gives actual values

# ALGO:
# 1. Create array of size n+1 filled with zeros
# 2. For each booking:
#    - Add seats at start index
#    - Subtract seats at end+1 index
# 3. Calculate prefix sum to get actual bookings
#    - Each position adds to previous
# 4. Return array excluding last element

class Solution:
   def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
       # Initialize difference array
       ans = [0] * (n+1)
       
       # Mark start and end points for each booking
       for start, end, flight in bookings:
           ans[start-1] += flight  # Add at start
           ans[end] -= flight      # Subtract at end+1
       
       # Calculate prefix sum
       for i in range(1, n):
           ans[i] += ans[i-1]
       
       # Return result excluding last element
       return ans[:-1]
