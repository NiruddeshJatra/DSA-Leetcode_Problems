# Time Complexity:
# - O(NlogN + MlogM) where N is number of jobs and M is number of workers
# - Sorting jobs and workers arrays: O(NlogN + MlogM)
# - Single pass through workers array: O(M)
# - Each job is considered at most once: O(N)
# - Overall: O(NlogN + MlogM)

# Space Complexity:
# - O(N) for creating jobs array with zipped pairs
# - Sorting may require O(logN) or O(logM) additional space
# - Overall O(N)

# INTUITION:
# For each worker, we want maximum profit from jobs they can do
# Key insights:
# 1. Sort both jobs and workers by difficulty/capability
# 2. Keep track of best profit seen so far
# 3. Workers with higher capability can do any job easier workers could
# Example: 
# difficulty = [2,4,6,8], profit = [10,20,30,40], workers = [4,5,6,7]
# Sort: jobs = [(2,10), (4,20), (6,30), (8,40)]
# Worker 4: can do (2,10), (4,20) -> gets 20
# Worker 5: same jobs -> gets 20
# Worker 6: adds (6,30) -> gets 30
# Worker 7: same jobs -> gets 30
# Total = 100

# ALGO:
# 1. Combine difficulty and profit into pairs
# 2. Sort jobs by difficulty and workers by capability
# 3. For each worker:
#    - Check all jobs they can do (difficulty <= capability)
#    - Keep track of max profit seen so far
#    - Add max profit to total
#    - Next worker can start from where last worker stopped
# 4. Return total profit

def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
   # Combine jobs into (difficulty, profit) pairs and sort
   jobs = sorted(zip(difficulty, profit))
   
   # Sort workers by capability
   worker.sort()
   
   totalProfit = 0      # Total profit from all assignments
   bestProfitSeen = 0   # Best profit seen so far
   jobIndex = 0         # Current job being considered
   
   # Process each worker
   for capability in worker:
       # Find all jobs current worker can do
       while jobIndex < len(jobs) and jobs[jobIndex][0] <= capability:
           # Update best profit if current job pays more
           bestProfitSeen = max(bestProfitSeen, jobs[jobIndex][1])
           jobIndex += 1
           
       # Add best possible profit for current worker
       totalProfit += bestProfitSeen
   
   return totalProfit
