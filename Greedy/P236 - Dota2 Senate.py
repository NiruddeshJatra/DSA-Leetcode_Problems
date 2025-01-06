# Time Complexity:
# - O(N), where N is length of senate string
#   - While loop iterates at most N times since each senator gets at most one vote
#   - Each iteration does O(1) operations (append/popleft)
# Space Complexity:
# - O(N) to store indices in radiants and dires queues
#   - Each queue can store at most N indices initially
# INTUITION:
# The key observation is that optimal strategy is to eliminate the closest opposing senator.
# Using two queues is efficient because:
# 1. Lower index means earlier voting power
# 2. When a senator eliminates another, they vote next round at position n
# 3. Queues naturally maintain order and allow O(1) operations
# This simulates real voting process where each senator tries to eliminate closest opponent
# ALGO:
# 1. Initialize two queues for each party's senators:
#    - Store initial positions (0 to n-1)
#    - Use queue to maintain voting order
# 2. While both parties have senators:
#    - Compare front senators from each queue
#    - Lower index senator eliminates other and gets next vote at position n
#    - Remove both from front of queues
#    - Add surviving senator to back with new position n
# 3. Return winner based on which queue is non-empty
from typing import List
import collections

class Solution:
   def predictPartyVictory(self, senate: str) -> str:
       # Queues to store voting positions for each party
       radiant = collections.deque()
       dire = collections.deque()
       n = len(senate)
       
       # Initialize voting positions
       for i in range(n):
           if senate[i] == 'R':
               radiant.append(i)
           else:
               dire.append(i)
       
       # Simulate voting process
       nextPosition = n
       while radiant and dire:
           radiantPos = radiant.popleft()
           direPos = dire.popleft()
           
           # Senator with lower position wins and votes again
           if radiantPos < direPos:
               radiant.append(nextPosition)
           else:
               dire.append(nextPosition)
           nextPosition += 1
           
       # Return winner
       return 'Radiant' if radiant else 'Dire'
