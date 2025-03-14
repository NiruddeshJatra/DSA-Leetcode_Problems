# Time Complexity:
# - O(amount * n), where amount is the target amount and n is the number of coin denominations.
# - We have amount states in our DP array, and for each state, we consider n coin denominations.

# Space Complexity:
# - O(amount), as we use a 1D DP array of size amount+1 to store the number of ways to make each amount.

# INTUITION:
# This is the Coin Change 2 problem: we need to find the number of different ways to make up the target amount,
# given a set of coin denominations.
#
# We use dynamic programming where dp[w] represents the number of ways to make amount w.
# Unlike the standard Coin Change problem (which asks for the minimum number of coins),
# this problem asks for the total number of combinations.
#
# The key insight is to process each coin denomination one by one and update the DP array.
# For each coin, we add the number of ways to make amount (w-coin) to the number of ways to make amount w.
#
# For example, with coins=[1,2,5] and amount=5:
# Initial: dp = [1, 0, 0, 0, 0, 0]
# After coin 1: dp = [1, 1, 1, 1, 1, 1] (1 way to make each amount using only 1s)
# After coin 2: dp = [1, 1, 2, 2, 3, 3] (additional ways using 2s)
# After coin 5: dp = [1, 1, 2, 2, 3, 4] (additional way using one 5)
# So there are 4 ways to make amount 5.

# ALGO:
# 1. Initialize a DP array of size amount+1 with zeros, and set dp[0] = 1 (base case: 1 way to make amount 0).
# 2. For each coin denomination:
#    a. For each amount from coin value to the target amount:
#       i. Update dp[amount] += dp[amount-coin]
# 3. Return dp[amount], which represents the number of ways to make the target amount.

from typing import List

class Solution:
   def change(self, amount: int, coins: List[int]) -> int:
       # Initialize DP array
       waysToMakeAmount = [0] * (amount + 1)
       
       # Base case: there's 1 way to make amount 0 (by using no coins)
       waysToMakeAmount[0] = 1
       
       # Process each coin denomination
       for coinValue in coins:
           # Update the DP array for each amount from coinValue to amount
           for currentAmount in range(coinValue, amount + 1):
               # Add the number of ways to make (currentAmount - coinValue)
               waysToMakeAmount[currentAmount] += waysToMakeAmount[currentAmount - coinValue]
       
       # Return the number of ways to make the target amount
       return waysToMakeAmount[amount]
