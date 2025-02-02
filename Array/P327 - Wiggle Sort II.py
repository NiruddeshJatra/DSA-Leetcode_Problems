# Time Complexity:
# - O(NlogN) due to sorting
# - Rearrangement operations are O(N)
# - Overall complexity is O(NlogN)

# Space Complexity:
# - O(N) for creating new subarrays during slicing
# - Original array is modified in-place after rearrangement

# INTUITION:
# To create wiggle sort where nums[0] < nums[1] > nums[2] < nums[3]...
# 1. Sort array first to work with ordered elements
# 2. Split array into two parts around middle
# 3. Place larger numbers in odd positions (from right)
# 4. Place smaller numbers in even positions (from middle)
# Example: [1,5,1,1,6,4] -> sorted [1,1,1,4,5,6]
# Split: [1,1,1] and [4,5,6]
# Result: [1,6,1,5,1,4]
# Achieves wiggle pattern: < > < > < >

# ALGO:
# 1. Sort the array
# 2. Find middle point
# 3. Split into two parts:
#    - First half + middle element
#    - Second half
# 4. Place elements in reverse order:
#    - Smaller numbers (up to mid) in even indices
#    - Larger numbers (after mid) in odd indices
# 5. This ensures wiggle pattern as each odd index
#    gets larger number than surrounding even indices

def wiggleSort(self, nums: List[int]) -> None:
   # Sort array in ascending order
   nums.sort()
   
   # Find middle index
   middleIndex = (len(nums) - 1) // 2
   
   # Rearrange array:
   # nums[::2] = even indices
   # nums[1::2] = odd indices
   # ::-1 reverses the sequences
   nums[::2], nums[1::2] = nums[middleIndex::-1], nums[:middleIndex:-1]
