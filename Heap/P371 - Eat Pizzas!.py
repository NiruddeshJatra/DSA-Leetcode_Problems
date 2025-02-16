# Time Complexity:
# - O(N log N) where N is number of pizzas
# - O(N) to build heap
# - O(R log N) for R rounds of heap operations where R = N/4

# Space Complexity:
# - O(N) for storing pizzas in heap
# - Original array is modified in place
# - No additional significant space needed

# INTUITION:
# In each round 4 pizzas are consumed, and Bob can choose either 1st or 2nd heaviest.
# Making pizzas negative turns max heap problem into min heap problem.
# For first half of rounds, Bob takes heaviest pizza (1st).
# For second half, Alice takes heaviest so Bob takes 2nd heaviest.
# Example: pizzas = [10,8,6,4] with 1 round:
# - Make negative: [-10,-8,-6,-4]
# - First round: Bob takes 10 (first half)
# Total = 10

# ALGO:
# 1. Convert pizzas to negative to use min heap
# 2. Calculate total rounds (N/4) and odd rounds ((R+1)/2)
# 3. For each round:
#    - If in first half (odd rounds):
#      * Take heaviest pizza (first element)
#    - If in second half (even rounds):
#      * Skip heaviest (Alice takes it)
#      * Take second heaviest
# 4. Return total weight

from typing import List
import heapq

class Solution:
   def maxWeight(self, pizzas: List[int]) -> int:
       # Convert to negative for min heap (effectively max heap)
       negativePizzas = [-weight for weight in pizzas]
       heapq.heapify(negativePizzas)
       
       totalWeight = 0
       totalRounds = len(pizzas) // 4
       
       # Calculate rounds where Bob takes heaviest pizza
       if totalRounds % 2 == 1:
           oddRounds = totalRounds // 2 + 1
       else:
           oddRounds = totalRounds // 2
       
       # Process each round
       for roundNum in range(totalRounds):
           if roundNum < oddRounds:
               # First half: Take heaviest pizza
               totalWeight += (-heapq.heappop(negativePizzas))
           else:
               # Second half: Skip heaviest, take second heaviest
               heapq.heappop(negativePizzas)  # Alice takes heaviest
               totalWeight += (-heapq.heappop(negativePizzas))  # Bob takes second heaviest
       
       return totalWeight
