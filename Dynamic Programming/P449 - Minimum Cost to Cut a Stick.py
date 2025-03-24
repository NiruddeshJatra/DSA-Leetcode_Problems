def minCost(self, n: int, cuts: List[int]) -> int:
   # Time Complexity:
   # - O(c³), where c is the number of cuts
   # - We have three nested loops: iterating through different cut ranges, 
   #   and finding the minimum cost of cutting

   # Space Complexity:
   # - O(c²) for the dynamic programming memoization table

   # INTUITION:
   # This is a classic dynamic programming problem of minimizing the cost of cutting a stick.
   # The key insights are:
   # 1. Cost of a cut includes the current length of the stick
   # 2. We want to find the optimal order of cuts to minimize total cost
   #
   # Imagine a wooden stick of length n, and we want to make several cuts.
   # Each time we make a cut, the cost is the current length of the stick.
   # The goal is to find the sequence of cuts that minimizes the total cost.

   # Example scenario:
   # n = 7, cuts = [1, 3, 4, 5]
   # Initial stick: |--------|  (length 7)
   # Possible cut orders will have different total costs

   # Recursive Memoization Solution
   def f(i, j):
       # Base case: no cuts possible in this range
       if i > j:
           return 0

       # If solution already computed, return memoized result
       if dp[i][j] != -1:
           return dp[i][j]

       # Initialize minimum cost to infinity
       mini = float('inf')

       # Try all possible ways to make cuts
       for k in range(i, j+1):
           # Calculate cost of current cut:
           # 1. Current stick length (cuts[j+1] - cuts[i-1])
           # 2. Cost of cuts in left subrange
           # 3. Cost of cuts in right subrange
           steps = cuts[j+1] - cuts[i-1] + f(i, k-1) + f(k+1, j)
           
           # Update minimum cost
           mini = min(mini, steps)

       # Memoize and return result
       dp[i][j] = mini
       return dp[i][j]
   
   # Preprocess cuts array
   c = len(cuts)
   cuts = [0] + cuts + [n]  # Add start and end points
   cuts.sort()  # Sort cuts in ascending order

   # Initialize memoization table with -1
   dp = [[-1] * (c + 1) for _ in range(c + 1)]
   
   # Call recursive function to find minimum cutting cost
   return f(1, c)

def minCost(self, n: int, cuts: List[int]) -> int:
   # Tabulation (Bottom-Up) Solution
   
   # Time Complexity:
   # - O(c³), where c is the number of cuts
   # - Three nested loops for computing minimum cutting costs
   
   # Space Complexity:
   # - O(c²) for the dynamic programming table
   
   # INTUITION:
   # Similar to recursive solution, but we build the solution iteratively
   # Bottom-up approach fills the dp table from smaller subproblems to larger ones

   # Preprocess cuts array
   c = len(cuts)
   cuts = [0] + cuts + [n]  # Add start and end points
   cuts.sort()  # Sort cuts in ascending order

   # Initialize DP table
   dp = [[0] * (c + 2) for _ in range(c + 2)]
   
   # Iterate through different range lengths
   for length in range(2, c + 1):
       for i in range(1, c - length + 2):
           j = i + length - 1
           
           # Initialize minimum cost to infinity
           mini = float('inf')
           
           # Try all possible cut points for current range
           for k in range(i, j + 1):
               # Calculate total cost of current cut
               steps = cuts[j+1] - cuts[i-1] + dp[i][k-1] + dp[k+1][j]
               
               # Update minimum cost
               mini = min(mini, steps)
           
           # Store minimum cost for current range
           dp[i][j] = mini
   
   # Return minimum cost for cutting the entire stick
   return dp[1][c]
