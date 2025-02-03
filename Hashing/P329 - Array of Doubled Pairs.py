# Time Complexity:
# - O(NlogN) for sorting the array
# - O(N) for counting frequencies
# - O(N) for iterating through array
# - Overall O(NlogN) due to sorting

# Space Complexity:
# - O(N) for frequency counter
# - O(1) additional space as we modify input array
# - Overall O(N) for storing frequencies

# INTUITION:
# For each number x, we need to find its pair (either x*2 or x/2)
# Key insights:
# 1. For positive numbers: look for x*2
# 2. For negative numbers: look for x/2 (must be even)
# 3. Process numbers in sorted order to handle negatives first
# Example: [4,-2,2,-4]
# Sort: [-4,-2,2,4]
# -4 needs -2: found
# -2 needs -1: not needed (already used)
# 2 needs 4: found
# 4 already used

# ALGO:
# 1. Count frequency of each number
# 2. Sort array to handle negative numbers first
# 3. For each number x:
#    - Skip if already used (freq[x] = 0)
#    - For negative x: must be even to have valid pair
#    - Find required pair (x*2 or x/2)
#    - Check if pair exists and available
#    - Decrease frequencies of both numbers
# 4. Return true if all pairs found

def canReorderDoubled(self, arr: List[int]) -> bool:
   # Count frequencies of all numbers
   numFrequencies = Counter(arr)
   
   # Sort array to handle negative numbers first
   arr.sort()
   
   # Check each number for its pair
   for num in arr:
       # Skip if number already used in a pair
       if numFrequencies[num] == 0:
           continue
           
       # For negative numbers, must be even to have valid pair
       if num < 0 and num % 2 != 0:
           return False
           
       # Calculate required pair
       pairNeeded = num * 2 if num > 0 else num // 2
       
       # Check if pair exists and is available
       if pairNeeded not in numFrequencies or numFrequencies[pairNeeded] == 0:
           return False
           
       # Use both numbers in pair
       numFrequencies[num] -= 1
       numFrequencies[pairNeeded] -= 1
   
   return True
