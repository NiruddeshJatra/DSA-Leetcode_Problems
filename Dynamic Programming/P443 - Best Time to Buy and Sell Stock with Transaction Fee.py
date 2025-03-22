# Time Complexity:
# - O(n) where n is the length of the prices array.
# - We process each day once and consider 2 possible states (buying or selling) for each day.

# Space Complexity:
# - O(n) for the DP table that stores the maximum profit for each state at each day.
# - This could be optimized to O(1) space by using only two variables for each state.

# INTUITION:
# This is the "Best Time to Buy and Sell Stock with Transaction Fee" problem. The key difference from the standard stock trading problem is that we need to pay a fee when selling a stock, which reduces our profit.

# When thinking about this problem, we need to consider what decisions we can make each day:

# 1. If we don't currently own a stock (buy=1 state):
#    - We can choose to buy a stock today, investing prices[i] money
#    - Or we can choose to do nothing and wait

# 2. If we already own a stock (buy=0 state):
#    - We can choose to sell the stock today, gaining prices[i] money but paying the transaction fee
#    - Or we can choose to do nothing and continue holding

# The transaction fee introduces an important consideration: we should only sell if the profit from selling (after deducting the fee) is greater than the profit from continuing to hold.

# Let's walk through an example to understand this better. Consider prices = [1,3,2,8,4,9] with fee = 2:
# - Day 0: Buy at price 1 (profit: -1)
# - Day 1: Could sell at price 3, but after fee, profit would be 3-1-2=0. Better to hold.
# - Day 2: Price drops to 2, so definitely hold.
# - Day 3: Sell at price 8, profit becomes 8-1-2=5
# - Day 4: Buy at price 4 (profit: 5-4=1)
# - Day 5: Sell at price 9, final profit becomes 1+(9-4-2)=4

# This approach gives us the maximum profit of 8 (buying at 1, selling at 8, buying at 4, selling at 9, with fees included).

# ALGORITHM:
# 1. Create a DP array where dp[i][buy] represents the maximum profit we can make starting from day i
#    with state 'buy' (buy=1 means we can buy, buy=0 means we're holding a stock and can sell).

# 2. The recurrence relation is:
#    - If buy=1 (can buy): dp[i][buy] = max(-prices[i] + dp[i+1][0], dp[i+1][1])
#      (either buy today and move to holding state, or skip buying)
   
#    - If buy=0 (can sell): dp[i][buy] = max(prices[i] - fee + dp[i+1][1], dp[i+1][0])
#      (either sell today with the transaction fee and move to buying state, or skip selling)

# 3. We process days from the end to the beginning (bottom-up approach) to build our solution.

# 4. The answer is dp[0][1], which represents the maximum profit starting from day 0 in a state
#    where we can buy a stock.

class Solution:
   def maxProfit(self, prices: List[int], fee: int) -> int:
       n = len(prices)
       
       # Create a DP table
       # dp[i][j] represents the maximum profit starting from day i
       # with j=1 meaning we can buy, and j=0 meaning we can sell
       dp = [[0] * 2 for _ in range(n + 1)]
       
       # Start from the last day and work backwards
       for i in range(n-1, -1, -1):
           for buy in range(2):
               if buy:
                   # If we're in a position to buy (not holding a stock):
                   # Option 1: Buy the stock today (-prices[i]) and move to holding state
                   # Option 2: Skip buying today, remain in buy state
                   dp[i][buy] = max(-prices[i] + dp[i+1][0], dp[i+1][1])
               else:
                   # If we're in a position to sell (holding a stock):
                   # Option 1: Sell the stock today (+prices[i] - fee) and move to buy state
                   # Option 2: Skip selling today, remain in sell state
                   dp[i][buy] = max(prices[i] - fee + dp[i+1][1], dp[i+1][0])
       
       # The result is the maximum profit starting from day 0 in a state where we can buy
       return dp[0][1]
