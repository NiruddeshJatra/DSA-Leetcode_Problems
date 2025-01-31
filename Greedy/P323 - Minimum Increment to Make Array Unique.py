# Time Complexity:
# - O(NlogN) due to sorting
# - The iteration through array is O(N)
# - Overall complexity is O(NlogN)

# Space Complexity: 
# - O(1) as we only use constant extra space
# - Sorting may require O(logN) space depending on implementation

# INTUITION:
# To make array unique with minimum increments:
# 1. Sort array first so we can process numbers in order
# 2. For each number, if it's not greater than previous
#    we must increment it to be at least prev + 1
# Example: [3,2,1,2,1,7]
# After sort: [1,1,2,2,3,7]
# 1. First 1 stays 1
# 2. Second 1 becomes 2 (+1)
# 3. First 2 becomes 3 (+1)
# 4. Second 2 becomes 4 (+2)
# 5. 3 becomes 5 (+2)
# 6. 7 stays 7
# Total moves = 6

# ALGO:
# 1. Sort the array
# 2. For each number from index 1 to n:
#    - If current <= previous:
#      - Calculate moves needed (prev + 1 - curr)
#      - Add moves to result
#      - Update current to prev + 1
# 3. Return total moves needed

def minIncrementForUnique(self, nums: List[int]) -> int:
   # Sort array to process numbers in order
   nums.sort()
   
   totalMoves = 0
   
   # Check each number with its previous
   for i in range(1, len(nums)):
       if nums[i] <= nums[i-1]:
           # Calculate moves needed to make current unique
           movesNeeded = nums[i-1] - nums[i] + 1
           # Add moves to total
           totalMoves += movesNeeded
           # Update current number
           nums[i] = nums[i-1] + 1
           
   return totalMoves
