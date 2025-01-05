# Time Complexity:
# - __init__: O(N log N) where N is number of initial tasks (each add operation is O(log N))
# - add: O(log N) for heap push operation
# - edit: O(log N) for heap push operation
# - rmv: O(1) for dictionary deletion
# - execTop: O(K log N) where K is number of invalid tasks to skip and N is total tasks
# Space Complexity:
# - O(N) where N is number of tasks
#   - taskQueue stores tuples of priority and taskId: O(N)
#   - taskInfo stores user and priority info: O(N)
# INTUITION:
# We need to manage tasks with different priorities and allow modifications. Using a combination of:
# 1. Max heap (implemented as min heap with negated values) for priority queue
#    - Allows O(log N) insertion and O(1) access to highest priority task
# 2. Dictionary for task information
#    - Provides O(1) lookup and modification of task details
#    - Helps validate tasks during execution
# This design efficiently handles all required operations while maintaining consistency.
# ALGO:
# Initialize:
# 1. Create empty max heap (taskQueue) and dictionary (taskInfo)
# 2. Process initial tasks using add method
# Add:
# 1. Push (-priority, -taskId) to heap (negated for max heap behavior)
# 2. Store (userId, priority) in taskInfo dictionary
# Edit:
# 1. Update priority in taskInfo
# 2. Push new (-priority, -taskId) to heap
# Remove:
# 1. Delete task from taskInfo dictionary
# Execute Top:
# 1. Pop tasks from heap until valid task found:
#    - Check if task exists in taskInfo
#    - Verify priority matches stored priority
# 2. Delete executed task and return userId
import heapq
from typing import List

class TaskManager:
   def __init__(self, tasks: List[List[int]]):
       self.taskQueue = []  # stores (-priority, -taskId)
       self.taskInfo = {}   # stores {taskId: (userId, priority)}
       
       for userId, taskId, priority in tasks:
           self.add(userId, taskId, priority)
       
   def add(self, userId: int, taskId: int, priority: int) -> None:
       heapq.heappush(self.taskQueue, (-priority, -taskId))
       self.taskInfo[taskId] = (userId, priority)
   
   def edit(self, taskId: int, newPriority: int) -> None:
       userId = self.taskInfo[taskId][0]
       self.taskInfo[taskId] = (userId, newPriority)
       heapq.heappush(self.taskQueue, (-newPriority, -taskId))
   
   def rmv(self, taskId: int) -> None:
       del self.taskInfo[taskId]
   
   def execTop(self) -> int:
       while self.taskQueue:
           priority, taskId = heapq.heappop(self.taskQueue)
           taskId = -taskId  # Convert back to positive
           
           # Skip if task was deleted or priority changed
           if taskId not in self.taskInfo or self.taskInfo[taskId][1] != -priority:
               continue
               
           userId = self.taskInfo[taskId][0]
           del self.taskInfo[taskId]
           return userId
           
       return -1
