# Time Complexity:
# - O(n), where n is the length of the input array.
# - We iterate through the array exactly once.

# Space Complexity:
# - O(n) in the worst case, where each number forms its own range.
# - The result list will have at most n ranges.

# INTUITION:
# The goal is to identify consecutive ranges of integers in a sorted array and represent them
# in a compact format. For consecutive elements, we want to show the range as "start->end".
# For isolated elements, we simply show the element itself.
#
# We can solve this by iterating through the array once and keeping track of the current range.
# When a number breaks the consecutive sequence, we format and add the current range to our result.
#
# For example, with [0,1,2,4,5,7]:
# - First, we start a range with 0
# - 1 and 2 extend this range (0,1,2)
# - 4 breaks the sequence, so we add "0->2" to our result and start a new range with 4
# - 5 extends the range (4,5)
# - 7 breaks the sequence, so we add "4->5" and start a new range with 7
# - Finally, we add "7" as a standalone range

# ALGO:
# 1. Handle the empty array case.
# 2. Iterate through the array:
#    a. If we don't have a current range pattern, start one with the current number.
#    b. If the current number is consecutive to the previous one, extend the range.
#    c. Otherwise, format the previous range and add it to the result, then start a new range.
# 3. Add the last range to the result.
# 4. Return the list of formatted ranges.

class Solution:
   def summaryRanges(self, nums: List[int]) -> List[str]:
       # Handle empty array case
       if not nums:
           return []
       
       ranges = []
       currentRange = ""
       consecutiveCount = 0
       
       for i in range(len(nums)):
           # Start a new range
           if currentRange == "":
               currentRange = str(nums[i])
               consecutiveCount = 1
           else:
               # If current number is consecutive to previous number
               if nums[i] == nums[i-1] + 1:
                   consecutiveCount += 1
               else:
                   # Current number breaks the sequence, finish the previous range
                   if consecutiveCount > 1:
                       # Format as "start->end" for ranges with multiple elements
                       currentRange += "->" + str(nums[i-1])
                   
                   # Add the formatted range to our result
                   ranges.append(currentRange)
                   
                   # Start a new range with the current number
                   currentRange = str(nums[i])
                   consecutiveCount = 1
       
       # Handle the last range
       if consecutiveCount > 1:
           currentRange += "->" + str(nums[-1])
       
       # Add the last range to our result
       ranges.append(currentRange)
       
       return ranges
