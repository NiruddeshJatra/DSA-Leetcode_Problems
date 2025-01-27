# Time Complexity: 
# - O(N log N + M log M), where N is length of players and M is length of trainers
# - Sorting both arrays dominates the time complexity
# - The two-pointer traversal is O(N + M)

# Space Complexity:
# - O(1), as we only use a constant amount of extra space
# - Sorting is typically done in-place

# INTUITION:
# Sort both arrays to optimize matching. Use two pointers to find valid player-trainer 
# pairs where player's ability level is less than or equal to trainer's capacity.

# ALGO:
# 1. Sort both players and trainers arrays in ascending order
# 2. Use two pointers to traverse both arrays simultaneously
# 3. If current player's ability <= current trainer's capacity, match them
# 4. Always advance trainer pointer regardless of match
# 5. Return total number of matches found

class Solution:
   def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
       players.sort()  # Sort players by ability
       trainers.sort()  # Sort trainers by capacity
       
       playerCount = len(players)
       trainerCount = len(trainers)
       playerPtr = trainerPtr = matchCount = 0
       
       while playerPtr < playerCount and trainerPtr < trainerCount:
           if players[playerPtr] <= trainers[trainerPtr]:
               matchCount += 1
               playerPtr += 1
           trainerPtr += 1
           
       return matchCount
