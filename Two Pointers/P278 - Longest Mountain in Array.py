# Time Complexity:
# - O(N), where N is the length of the input array
# - We only need to traverse the array once from left to right
# - All operations within the loop are O(1)

# Space Complexity:
# - O(1), we only use a constant amount of extra space
# - Only storing a few variables regardless of input size

# INTUITION:
# A mountain array is made up of strictly increasing elements followed by
# strictly decreasing elements. We can find it by:
# 1. Tracking when we start going uphill (increasing)
# 2. Tracking when we start going downhill (decreasing)
# 3. A valid mountain must have both uphill and downhill portions
# 4. Reset when we find invalid sequences

# ALGORITHM:
# 1. Start traversing array from index 1
# 2. If current element > previous:
#    - Mark mountain start
#    - Update length based on whether it's new mountain or continuing
# 3. If mountain started and current < previous:
#    - Mark mountain end
#    - Increment length
# 4. In all other cases:
#    - Reset mountain tracking
# 5. Update maxLength whenever we have a valid mountain end

class Solution:
   def longestMountain(self, arr: List[int]) -> int:
       if len(arr) < 3:
           return 0
           
       maxLength = 0
       currentLength = 0
       isUphill = False
       isDownhill = False
       
       for i in range(1, len(arr)):
           if arr[i] > arr[i-1]:
               isUphill = True
               if currentLength == 0 or isDownhill:
                   currentLength = 2
               else:
                   currentLength += 1
               isDownhill = False
                   
           elif isUphill and arr[i] < arr[i-1]:
               isDownhill = True
               currentLength += 1
               
           else:
               currentLength = 0
               isUphill = False
               isDownhill = False
               
           if isDownhill:
               maxLength = max(maxLength, currentLength)
               
       return maxLength
