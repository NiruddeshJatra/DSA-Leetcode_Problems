# Time Complexity:
# - O(n) where n is the length of the prices array.
# - We process each day exactly once and for each day we consider 2 possible states (buying or selling).

# Space Complexity:
# - O(n) for the DP table that stores the maximum profit for each state at each day.
# - We need to look up values from i+2, so we can't easily optimize this to O(1) space.

# INTUITION:
# This is the "Best Time to Buy and Sell Stock with Cooldown" problem. The key constraint here is that
# after selling a stock, you cannot buy another stock on the next day (you need a cooldown period).
#
# To understand this problem, let's think about the decisions we can make on each day:
#
# 1. If we don't own a stock (buy=1 state):
#    - We can choose to buy a stock today, spending prices[i] money
#    - Or we can choose to do nothing and wait
#
# 2. If we already own a stock (buy=0 state):
#    - We can choose to sell the stock today, gaining prices[i] money
#    - Or we can choose to do nothing and continue holding
#
# The cooldown rule adds an important twist: after selling a stock on day i, we can't buy on day i+1.
# We need to wait until day i+2 at the earliest. This is captured in our recurrence relation by
# moving to dp[i+2][1] after a sell action instead of dp[i+1][1].
#
# Example with prices = [1,2,3,0,2]:
# - Day 0: Buy at price 1 (profit: -1)
# - Day 1: Hold (profit still -1)
# - Day 2: Sell at price 3 (profit: 2)
# - Day 3: Cooldown (can't buy due to cooldown rule)
# - Day 4: Buy at price 2 (profit: 0)
# - We end with profit 2, which is the maximum possible

# ALGORITHM:
# 1. Create a DP array where dp[i][buy] represents the maximum profit we can make starting from day i
#    with state 'buy' (buy=1 means we can buy, buy=0 means we're holding a stock and can sell).
#
# 2. The recurrence relation is:
#    - If buy=1 (can buy): dp[i][buy] = max(-prices[i] + dp[i+1][0], dp[i+1][1])
#      (either buy today and move to holding state, or skip buying)
#    
#    - If buy=0 (can sell): dp[i][buy] = max(prices[i] + dp[i+2][1], dp[i+1][0])
#      (either sell today and move to cooldown state, or skip selling)
#
# 3. We process days from the end to the beginning (bottom-up approach) to build our solution.
#
# 4. The answer is dp[0][1], which represents the maximum profit starting from day 0 in a state
#    where we can buy a stock.

class Solution:
   def maxProfit(self, prices: List[int]) -> int:
       n = len(prices)
       
       # Create a DP table with n+2 days to handle the cooldown period safely
       # dp[i][j] represents the maximum profit starting from day i
       # with j=1 meaning we can buy, and j=0 meaning we can sell
       dp = [[0] * 2 for _ in range(n + 2)]
       
       # Start from the last day and work backwards
       for i in range(n-1, -1, -1):
           for buy in range(2):
               if buy:
                   # If we can buy on this day, we have two options:
                   # 1. Buy the stock: -prices[i] + profit from holding state
                   # 2. Don't buy: profit remains the same as next day's buy state
                   dp[i][buy] = max(-prices[i] + dp[i+1][0], dp[i+1][1])
               else:
                   # If we can sell on this day, we have two options:
                   # 1. Sell the stock: +prices[i] + profit from day i+2 (after cooldown)
                   # 2. Don't sell: profit remains the same as next day's sell state
                   dp[i][buy] = max(prices[i] + dp[i+2][1], dp[i+1][0])
       
       # The result is the maximum profit starting from day 0 in a state where we can buy
       return dp[0][1]
