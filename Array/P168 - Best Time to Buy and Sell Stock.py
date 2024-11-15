# Time Complexity: O(n), where n is the length of `prices`.
# The algorithm iterates through the `prices` list once, performing constant-time operations for each element.

# Space Complexity: O(1).
# The algorithm uses only a few variables (`buy`, `sell`, `profit`) to keep track of the necessary state.

# INTUITION:
# The goal is to determine the maximum profit that can be made by buying and selling a stock once.  
# By iterating through the prices, we maintain the minimum price seen so far (`buy`) and calculate the profit by subtracting it from the current price (`sell`).  
# The logic ensures that the stock is "bought" at the minimum price before being "sold" to maximize the profit.  
# This approach is efficient because it processes the input in a single pass, keeping the space usage minimal.

# ALGO:
# 1. Initialize `buy` to the first price in the array, and set `profit` to 0.
# 2. Iterate through each price in the array:
#    - Update `buy` if the current price is less than the current `buy`.
#    - Calculate the potential profit using the current price and update `profit` if this new profit is greater.
# 3. Return the maximum profit obtained.

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        maxProfit = 0
        for currentPrice in prices:
            if currentPrice < buy:
                buy = currentPrice
            maxProfit = max(maxProfit, currentPrice - buy)
        
        return maxProfit
