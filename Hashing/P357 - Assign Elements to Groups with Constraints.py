# Time Complexity:
# - O(N + G * sqrt(M)), where:
#   N = length of elements array for building earliest indices map
#   G = length of groups array
#   M = maximum value in groups array
# - For each group value, we find all divisors up to sqrt(M)
# - Divisor calculation takes O(sqrt(M)) time per group value

# Space Complexity:
# - O(N) for earliestIndices hashmap storing first occurrence of each number
# - O(sqrt(M)) for divisors set storing divisors of current group value
# - O(G) for output array storing assigned indices
# - Overall space: O(N + sqrt(M) + G)

# INTUITION:
# Imagine you're organizing a competition where:
# - You have a list of numbers (elements)
# - Teams (groups) need to find players whose number either divides their team size
#   or is a multiple of it
# - Each team wants the earliest available player meeting their criteria
# - Special case: Team 0 wants the earliest non-zero player
#
# For efficient matching, we:
# 1. First record earliest occurrences of all numbers (like taking attendance)
# 2. For each team, find all their possible matches (divisors) and pick earliest one
# 3. Handle Team 0 separately as it has different rules

# ALGORITHM:
# 1. Build earliestIndices map and track first non-zero element
# 2. For each group value g:
#    - If g is 0: assign earliest non-zero index
#    - Otherwise:
#      a. Find all divisors of g up to sqrt(g)
#      b. For each divisor, check if it exists in elements
#      c. Find earliest index among all valid divisors
#      d. Assign -1 if no valid divisor found

class Solution:
   def assignElements(self, groups: List[int], elements: List[int]) -> List[int]:
       # Track earliest occurrence of each number and first non-zero
       earliestIndices = {}
       earliestNonZeroIndex = float('inf')
       
       for index, number in enumerate(elements):
           # Record first occurrence of each number
           if number not in earliestIndices:
               earliestIndices[number] = index
           # Update earliest non-zero number index
           if number != 0 and index < earliestNonZeroIndex:
               earliestNonZeroIndex = index
       
       # Convert float('inf') to -1 if no non-zero found
       earliestNonZeroIndex = -1 if earliestNonZeroIndex == float('inf') else earliestNonZeroIndex
       
       assignedIndices = []
       for groupValue in groups:
           # Special case: Group 0 wants earliest non-zero
           if groupValue == 0:
               assignedIndices.append(earliestNonZeroIndex)
               continue
           
           # Find all divisors of current group value
           divisors = set()
           squareRoot = int(groupValue ** 0.5)
           for divisor in range(1, squareRoot + 1):
               if groupValue % divisor == 0:
                   divisors.add(divisor)
                   if divisor != groupValue // divisor:  # Avoid duplicates for perfect squares
                       divisors.add(groupValue // divisor)
           
           # Find earliest index among all valid divisors
           earliestValidIndex = float('inf')
           for divisor in divisors:
               if divisor in earliestIndices:
                   earliestValidIndex = min(earliestValidIndex, earliestIndices[divisor])
           
           # Convert float('inf') to -1 if no valid divisor found
           assignedIndices.append(-1 if earliestValidIndex == float('inf') else earliestValidIndex)
       
       return assignedIndices
