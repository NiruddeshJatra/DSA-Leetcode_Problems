# Time Complexity: O(N log N), N = number of events
# Space Complexity: O(N)

# INTUITION:
# Track user mentions and offline status efficiently
# Handle different message types (ALL, HERE, specific users)
# Adjust mentions based on offline periods and message types

# ALGO:
# 1. Sort events by timestamp with priority to OFFLINE
# 2. Maintain arrays for:
#    - Mentions count
#    - Offline status
#    - Last mentioned timestamp
# 3. Process events sequentially:
#    - MESSAGE (ALL): increment all mentions
#    - MESSAGE (HERE): increment online/recently online users
#    - MESSAGE (specific users): increment specific users
#    - OFFLINE: mark user offline, potentially remove a mention

class Solution:
   def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
       mentions = [0] * numberOfUsers
       offline = [(False, 0)] * numberOfUsers
       mentionedTimestamp = [0] * numberOfUsers
      events.sort(key = lambda x: (int(x[1]), x[0] != "OFFLINE"))
       
       for event in events:
           instruction, timestamp, users = event
           timestamp = int(timestamp)
           
           if instruction == "MESSAGE":
               if users == "ALL":
                   mentions = [count + 1 for count in mentions]
                   mentionedTimestamp = [timestamp] * numberOfUsers
               
               elif users == "HERE":
                   for id in range(numberOfUsers):
                       if not offline[id][0] or (offline[id][0] and offline[id][1] <= timestamp):
                           mentions[id] += 1
                           mentionedTimestamp[id] = timestamp
                           if offline[id][0]:
                               offline[id] = (False, timestamp)
               
               else:
                   for user in users.split():
                       id = int(user[2:])
                       mentions[id] += 1
                       mentionedTimestamp[id] = timestamp
           
           else:  # OFFLINE
               id = int(users)
               offline[id] = (True, timestamp + 60)
               if timestamp <= mentionedTimestamp[id] < timestamp + 60:
                   mentions[id] -= 1
       
       return mentions
