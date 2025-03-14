# Time Complexity:
# - O(N), where N is the length of the prices array.
# - We only need to iterate through the array once.

# Space Complexity:
# - O(1), as we only use four variables regardless of the input size.

# INTUITION:
# The problem asks for the maximum profit by making at most two transactions (buy and sell).
# We can solve this in one pass by tracking the best we can do with one transaction and the best
# we can do with two transactions simultaneously.
#
# The key insight is to view this as a sequence of 4 operations:
# 1. First buy (buy1): Track the lowest price seen so far (minimize cost)
# 2. First sell (sell1): Track the maximum profit from one transaction
# 3. Second buy (buy2): Track the lowest effective price after accounting for the profit from the first transaction
# 4. Second sell (sell2): Track the maximum total profit from two transactions
#
# This approach allows us to find the optimal buying and selling points without explicitly identifying them.
#
# For example, with prices = [3,3,5,0,0,3,1,4]:
# - buy1 becomes 0 (min price seen)
# - sell1 becomes 3 (max profit from one transaction: buy at 0, sell at 3)
# - buy2 becomes -3 (min effective price: actual price - profit from first transaction)
# - sell2 becomes 7 (max profit from two transactions: 3 from first + 4 from second)

# ALGO:
# 1. Initialize buy1 and buy2 to infinity (representing the lowest prices to buy).
# 2. Initialize sell1 and sell2 to 0 (representing the maximum profits).
# 3. Iterate through each price in the array:
#    a. Update buy1 to be the minimum of current buy1 and the current price.
#    b. Update sell1 to be the maximum of current sell1 and (current price - buy1).
#    c. Update buy2 to be the minimum of current buy2 and (current price - sell1).
#    d. Update sell2 to be the maximum of current sell2 and (current price - buy2).
# 4. Return sell2, which represents the maximum profit from at most two transactions.

from typing import List

class Solution:
   def maxProfit(self, prices: List[int]) -> int:
       # Initialize the variables
       firstBuyCost = float('inf')      # Lowest price to buy first stock
       firstSellProfit = 0              # Maximum profit from first transaction
       secondBuyCost = float('inf')     # Lowest effective price to buy second stock
       secondSellProfit = 0             # Maximum profit from both transactions
       
       for currentPrice in prices:
           # Update the first buy cost (minimize it)
           firstBuyCost = min(firstBuyCost, currentPrice)
           
           # Update the first sell profit (maximize it)
           firstSellProfit = max(firstSellProfit, currentPrice - firstBuyCost)
           
           # Update the second buy cost
           # This is the current price minus the profit from first transaction
           # (effectively, how much we're "paying" for the second stock)
           secondBuyCost = min(secondBuyCost, currentPrice - firstSellProfit)
           
           # Update the second sell profit (maximize it)
           secondSellProfit = max(secondSellProfit, currentPrice - secondBuyCost)
       
       # Return the maximum profit from at most two transactions
       return secondSellProfit
