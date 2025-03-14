# Time Complexity:
# - O(amount * n), where amount is the target amount and n is the number of coins.
# - We have amount states in our DP array, and for each state, we consider n coin denominations.

# Space Complexity:
# - O(amount), as we use a DP array of size amount+1 to store the minimum number of coins needed.

# INTUITION:
# This is the classic Coin Change problem: we need to find the minimum number of coins needed to make up
# the target amount, given a set of coin denominations.
#
# We use dynamic programming where dp[a] represents the minimum number of coins needed to make amount a.
# For each amount, we consider all possible coins and pick the one that results in the minimum number of coins.
#
# The key insight is that for any amount a, the minimum number of coins is 1 (the coin we're currently considering)
# plus the minimum number of coins needed to make up (a-c) where c is the value of the current coin.
#
# For example, with coins=[1,2,5] and amount=11:
# dp[0] = 0 (base case)
# dp[1] = 1 (1 coin of value 1)
# dp[2] = 1 (1 coin of value 2)
# dp[3] = 2 (1 coin of value 1 + 1 coin of value 2)
# ...
# dp[11] = 3 (2 coins of value 3 + 1 coin of value 5)

# ALGO:
# 1. Initialize a DP array of size amount+1 with infinity, and set dp[0] = 0 (base case: 0 coins needed for amount 0).
# 2. For each amount from 1 to the target amount:
#    a. For each coin denomination:
#       i. If the coin value is less than or equal to the current amount:
#          - Update dp[amount] = min(dp[amount], 1 + dp[amount-coin])
# 3. Return dp[amount] if it's not infinity, otherwise return -1 (indicating that the amount cannot be made up).

from typing import List

class Solution:
   def coinChange(self, coins: List[int], amount: int) -> int:
       # Initialize DP array with infinity
       minCoinsNeeded = [float('inf')] * (amount + 1)
       
       # Base case: 0 coins needed to make amount 0
       minCoinsNeeded[0] = 0
       
       # Fill the DP array
       for currentAmount in range(1, amount + 1):
           # Try each coin denomination
           for coinValue in coins:
               # Check if using this coin is valid
               if currentAmount - coinValue >= 0:
                   # Update with minimum coins needed
                   minCoinsNeeded[currentAmount] = min(
                       minCoinsNeeded[currentAmount],
                       1 + minCoinsNeeded[currentAmount - coinValue]
                   )
       
       # Return result, or -1 if amount cannot be made
       return minCoinsNeeded[amount] if minCoinsNeeded[amount] != float('inf') else -1
