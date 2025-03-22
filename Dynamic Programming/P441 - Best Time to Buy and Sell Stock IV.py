# Time Complexity:
# - O(n * k) where n is the length of the prices array and k is the maximum number of transactions allowed.
# - We process each day once, and for each day we consider k possible transactions and 2 possible states (buying or selling).

# Space Complexity:
# - O(k) as we only store two rows of the DP table at any time (current and ahead), each with 2 * (k+1) elements.
# - This is a space optimization from the original O(n * k) approach.

# INTUITION:
# This is the "Best Time to Buy and Sell Stock IV" problem, where we need to find the maximum profit
# we can make with at most k transactions. A transaction consists of buying a stock on one day and
# selling it on a future day.

# The key insight is to break this problem down into subproblems based on three dimensions:
# 1. The current day we're considering (i)
# 2. Whether we're currently holding a stock or not (buy)
# 3. How many transactions we have left to complete (cap)

# On any given day, if we don't hold a stock, we have two choices:
# - Buy a stock today (reduces our cash by prices[i])
# - Do nothing (our state remains the same)

# If we already hold a stock, we have two choices:
# - Sell the stock today (increases our cash by prices[i] and completes one transaction)
# - Do nothing (continue holding)

# Our goal is to maximize the profit across all possible choices and days.

# Example:
# Consider prices = [3,2,6,5,0,3] and k = 2
# - We might buy at day 1 (price 2), sell at day 2 (price 6), then buy at day 4 (price 0) and sell at day 5 (price 3)
# - This gives us a total profit of (6-2) + (3-0) = 7

# ALGORITHM:
# 1. We use a bottom-up dynamic programming approach with a state represented by (day, holding, transactions).
# 2. We optimize space by only keeping track of the next day's values (ahead) and the current day's values (cur).
# 3. For each day, we consider two states:
#    - buy=1: We can either buy a stock or do nothing
#    - buy=0: We can either sell a stock or do nothing
# 4. We compute the maximum profit recursively and return the final result.
# 5. Our recurrence relation looks like:
#    - If buying: max(-prices[i] + dp[i+1][0][cap], dp[i+1][1][cap])
#    - If selling: max(prices[i] + dp[i+1][1][cap-1], dp[i+1][0][cap])

class Solution:
   def maxProfit(self, k: int, prices: List[int]) -> int:
       # Handle edge cases
       if not prices or k == 0:
           return 0
           
       n = len(prices)
       
       # Initialize our DP table for the next day
       # ahead[buy][cap] represents the maximum profit starting from the next day,
       # with buy indicating whether we're holding a stock (0=no, 1=yes),
       # and cap indicating how many transactions we have left
       ahead = [[0] * (k + 1) for _ in range(2)]
       
       # Start from the last day and work backwards
       for i in range(n-1, -1, -1):
           # Initialize DP table for the current day
           cur = [[0] * (k + 1) for _ in range(2)]
           
           # Consider each possible state
           for buy in range(2):
               # Consider each possible number of remaining transactions
               for cap in range(1, k + 1):
                   if buy:
                       # If we're in a position to buy (not holding any stock):
                       # Option 1: Buy the stock today (-prices[i]) and move to not-buy state
                       # Option 2: Skip buying today, remain in buy state
                       cur[buy][cap] = max(-prices[i] + ahead[0][cap], ahead[1][cap])
                   else:
                       # If we're in a position to sell (holding a stock):
                       # Option 1: Sell the stock today (+prices[i]), complete a transaction, move to buy state
                       # Option 2: Skip selling today, remain in not-buy state
                       cur[buy][cap] = max(prices[i] + ahead[1][cap-1], ahead[0][cap])
           
           # Update our ahead values for the next iteration
           ahead = cur
       
       # The result is the maximum profit starting from day 0,
       # in a position to buy (buy=1), with k transactions available
       return ahead[1][k]
