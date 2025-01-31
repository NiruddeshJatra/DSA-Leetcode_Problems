# Time Complexity:
# - O(NlogN) due to sorting
# - The iteration itself is O(N)

# Space Complexity:
# - O(1) as we only use a few variables
# - Sorting may require O(logN) space depending on implementation

# INTUITION:
# The key insight is that to maximize our coins, we want to:
# 1. Always let Alice take the largest pile
# 2. We take the second largest pile
# 3. Bob gets the smallest pile
# Example: If piles = [1,2,3,4,5,6]
# Round 1: Alice(6), Me(5), Bob(1)
# Round 2: Alice(4), Me(3), Bob(2)
# This way we get middle elements from sorted array

# ALGO:
# 1. Sort piles in ascending order
# 2. For N piles, there will be N/3 turns
# 3. In each turn:
#    - Alice takes largest (right most)
#    - We take second largest (right - 1)
#    - Bob takes smallest (left most)
# 4. To get our coins: take every 2nd element from right
#    starting at second-to-last going up to N/3 elements

def maxCoins(self, piles: List[int]) -> int:
   # Sort piles in ascending order
   piles.sort()
   
   totalCoins = 0
   numRounds = len(piles) // 3
   
   # Start from second largest (index -2)
   # Go backwards by 2 (skip Alice's coin)
   # Stop after N/3 rounds
   for i in range(len(piles) - 2, len(piles) // 3 - 1, -2):
       totalCoins += piles[i]
       
   return totalCoins
