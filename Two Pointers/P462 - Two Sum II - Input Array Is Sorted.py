# Time Complexity:
# - O(n), where n is the length of the numbers array
# - We use two pointers that move towards each other, visiting each element at most once

# Space Complexity:
# - O(1), only using constant extra space for the two pointers
# - No additional data structures are needed

# INTUITION:
# The problem asks to find two numbers in a sorted array that sum to a target
# Key insight: Since the array is sorted, we can use two pointers technique
# Strategy:
# - Start with pointers at both ends of the array
# - If sum is too large, move right pointer left (decrease sum)
# - If sum is too small, move left pointer right (increase sum)
# - The sorted property guarantees we'll find the solution if it exists
# Example:
# numbers = [2,7,11,15], target = 9
# Start: left=0(2), right=3(15), sum=17 > 9, move right left
# Next: left=0(2), right=2(11), sum=13 > 9, move right left  
# Next: left=0(2), right=1(7), sum=9 = 9, found answer at indices 1,2

# ALGO:
# 1. Initialize two pointers: left at start, right at end
# 2. Calculate sum of elements at both pointers
# 3. If sum equals target, return the indices (1-indexed)
# 4. If sum is greater than target, move right pointer left
# 5. If sum is less than target, move left pointer right
# 6. Repeat until target sum is found

class Solution:
   def twoSum(self, numbers: List[int], target: int) -> List[int]:
       # Initialize two pointers at opposite ends
       leftPointer, rightPointer = 0, len(numbers) - 1
       
       # Continue until pointers meet
       while leftPointer < rightPointer:
           currentSum = numbers[leftPointer] + numbers[rightPointer]
           
           if currentSum > target:
               # Sum too large, decrease by moving right pointer left
               rightPointer -= 1
           elif currentSum < target:
               # Sum too small, increase by moving left pointer right
               leftPointer += 1
           else:
               # Found target sum, return 1-indexed positions
               return [leftPointer + 1, rightPointer + 1]
       
       # This line should never be reached given problem constraints
       return []
