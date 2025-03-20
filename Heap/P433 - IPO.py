# Time Complexity:
# - O(N log N + K log N), where N is the number of projects and K is the maximum number of projects we can select.
# - O(N log N) for sorting the projects by their capital requirements.
# - O(K log N) for performing up to K heap operations, where each operation takes O(log N) time.

# Space Complexity:
# - O(N) for storing the paired capital and profit values, as well as the heap.

# INTUITION:
# This problem can be solved using a greedy approach. The key insight is that at any point, we should select the 
# project with the highest profit that we can afford with our current capital. This suggests using a max-heap to 
# efficiently retrieve the most profitable project.
#
# Let's think about this problem step by step:
# 1. We need to consider both the capital required and the profit for each project.
# 2. At each step, we want to choose the project that maximizes our profit among all projects we can afford.
# 3. As our capital increases, more projects become available to us.
#
# Example:
# If we have projects with [capital, profit] as: [1,2], [2,3], [1,4], [3,5] and initial capital w = 2, k = 3:
# - Initially, we can afford projects [1,2] and [1,4], so we choose [1,4] (higher profit).
# - Our capital becomes 2 + 4 = 6, making all projects affordable.
# - For our next 2 selections, we pick [3,5] and [2,3], ending with a capital of 6 + 5 + 3 = 14.

# ALGO:
# 1. Pair each project's capital requirement with its profit and sort by capital in ascending order.
# 2. Initialize a max-heap to store profits of available projects.
# 3. While we can still select projects (k > 0):
#    a. Add all projects that we can afford (capital ≤ current capital) to the max-heap.
#    b. If the heap is not empty, select the project with maximum profit and add its profit to our capital.
#    c. Decrement k.
# 4. Return the final capital.

class Solution:
   def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
       # Combine capital requirements and profits into pairs
       projects = list(zip(capital, profits))
       
       # Sort projects by capital requirements (ascending)
       projects.sort()
       
       # Max heap to store profits of available projects
       availableProjects = []
       
       # Index to track which projects we've considered
       projectIndex = 0
       
       # Complete up to k projects
       remainingSelections = k
       currentCapital = w
       
       while remainingSelections > 0:
           # Add all affordable projects to the max heap
           while projectIndex < len(projects) and projects[projectIndex][0] <= currentCapital:
               # Use negative value for profit to create a max heap (Python has min heap by default)
               heapq.heappush(availableProjects, -projects[projectIndex][1])
               projectIndex += 1
           
           # Select the most profitable project if available
           if availableProjects:
               # Convert back to positive value when retrieving from heap
               bestProfit = -heapq.heappop(availableProjects)
               currentCapital += bestProfit
           else:
               # If no projects are affordable, we can't increase our capital further
               break
               
           remainingSelections -= 1

       return currentCapital
