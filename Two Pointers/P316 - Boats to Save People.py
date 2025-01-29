# Time Complexity:
# - O(N log N), where N is the number of people
# - Dominated by sorting the people array
# - Two-pointer traversal is O(N)

# Space Complexity:
# - O(1), using only constant extra space
# - Sorting is typically done in-place

# INTUITION:
# Sort people by weight and use two pointers from ends.
# Try to pair heaviest person with lightest person.
# If sum exceeds limit, heaviest must go alone.
# This greedy approach ensures minimum number of boats.

# ALGO:
# 1. Sort people by weight in ascending order
# 2. Use two pointers: left for lightest, right for heaviest
# 3. For each iteration:
#    - Try to pair current heaviest with lightest
#    - If sum <= limit, both can go (increment left)
#    - Always include heaviest (decrement right)
#    - Count one boat used
# 4. Return total boats needed

class Solution:
   def numRescueBoats(self, people: List[int], limit: int) -> int:
       people.sort()
       boats = 0
       leftPtr = 0
       rightPtr = len(people) - 1
       
       while leftPtr <= rightPtr:
           currentWeight = people[leftPtr] + people[rightPtr]
           
           # If lightest and heaviest can share boat
           if currentWeight <= limit:
               leftPtr += 1
               
           # Always include heaviest person
           rightPtr -= 1
           boats += 1
           
       return boats
