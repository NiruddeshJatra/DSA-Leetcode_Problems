# Time Complexity:
# - O(N log N), where N is the length of skill array
# - Dominated by the sorting operation
# - Two-pointer traversal is O(N)

# Space Complexity:
# - O(1), using constant extra space
# - Sorting is typically done in-place

# INTUITION:
# Sort the array and use two pointers from both ends to form teams.
# All teams must have equal total skill, so check if current pair sum
# matches previous pair sum. Multiply skills for chemistry score.

# ALGO:
# 1. Sort skill array in ascending order
# 2. Use two pointers from start and end 
# 3. For each pair:
#    - Check if sum equals previous team's sum
#    - Calculate chemistry (product) and add to result
# 4. Return -1 if any team has different sum

class Solution:
   def dividePlayers(self, skill: List[int]) -> int:
       skill.sort()
       leftPtr = 0 
       rightPtr = len(skill) - 1
       totalChemistry = 0
       targetSum = 0

       while leftPtr < rightPtr:
           currentSum = skill[leftPtr] + skill[rightPtr]
           
           if leftPtr > 0 and currentSum != targetSum:
               return -1
               
           targetSum = currentSum
           currentChemistry = skill[leftPtr] * skill[rightPtr]
           totalChemistry += currentChemistry
           
           leftPtr += 1
           rightPtr -= 1

       return totalChemistry
