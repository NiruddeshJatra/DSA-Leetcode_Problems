# Time Complexity: O(n), where n is the length of the prices array. We traverse the array once, making the time complexity linear.
# Space Complexity: O(1), since we only use a constant amount of extra space for the variables `profit` and `buy`.

# INTUITION:
# The goal is to maximize profit from buying and selling stock. The challenge allows buying and selling multiple times, as long as you sell before buying again.
#
# **Key Insight**:
# - We can simply sum up the differences between consecutive prices whenever the price increases, as this would represent a "buy low, sell high" scenario.

# ALGO:
# 1. **Initialize `profit` and `buy`**:
#    - `profit` will store the accumulated profit. Set it to 0 initially.
#    - `buy` will track the index where we are "buying" stock.
# 2. **Traverse the Prices**:
#    - For each price starting from the second day (`i = 1`), compare it with the previous day's price (`prices[buy]`):
#        - If today's price (`prices[i]`) is greater than the price at `buy`, then calculate the profit (`prices[i] - prices[buy]`) and add it to the total `profit`.
#        - Update `buy` to the current index (`i`) at the end of each iteration.
# 3. **Return the Total Profit**:
#    - After the loop completes, return the accumulated profit.

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Step 1: Initialize profit to 0 and buy to index 0
        profit = 0
        buy = 0

        # Step 2: Traverse the array from the second day onward
        for i in range(1, len(prices)):
            if prices[i] > prices[buy]:
                # Step 2.1: Add the profit from the increase in price
                profit += prices[i] - prices[buy]
            
            # Step 2.2: Update the buy index
            buy = i
        
        # Step 3: Return the total profit
        return profit
