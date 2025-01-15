# Time Complexity:
# - O(N) where N is length of nums array
# - Each element is pushed and popped at most once
# - While loop inside for loop still gives O(N) total operations

# Space Complexity:
# - O(N) for the stack in worst case
# - Best case O(K) when K elements remain after removals 

# INTUITION:
# To find the most competitive subsequence we need to:
# 1. Keep smallest possible numbers in their leftmost valid positions
# 2. Remove larger numbers when we find smaller ones that can replace them
# 3. Track how many numbers we can still remove (k)
# Using a monotonic stack is optimal because:
# - We want increasing order from left to right when possible
# - Stack lets us easily remove larger numbers when we find smaller ones
# - We can track remaining numbers to remove with k counter

# ALGORITHM:
# 1. Initialize empty stack and calculate numbers to remove (k)
# 2. For each number:
#    - While current number is smaller than stack top AND we can still remove numbers:
#      * Remove stack top (it's bigger than current)
#      * Decrement numbers we can still remove
#    - Add current number to stack
# 3. If we still need to remove numbers, remove from end of stack
# 4. Return stack as final subsequence

class Solution:
   def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
       # Calculate how many numbers we need to remove
       numbersToRemove = len(nums) - k
       monotonicStack = []
       
       # Process each number in array
       for currentNum in nums:
           # Remove larger numbers from stack when possible
           while (monotonicStack and 
                 monotonicStack[-1] > currentNum and 
                 numbersToRemove > 0):
               monotonicStack.pop()
               numbersToRemove -= 1
           
           # Add current number to stack
           monotonicStack.append(currentNum)
       
       # Remove any remaining numbers needed from end
       if numbersToRemove > 0:
           monotonicStack = monotonicStack[:-numbersToRemove]
           
       return monotonicStack
