"""
### Problem
Design an algorithm that collects daily price quotes for some stock and returns the span of that stock's price for the current day. The span of the stock's price today is defined as the maximum number of consecutive days (starting from today and going backward) for which the price of the stock was less than or equal to today's price.

### Intuition
The problem can be efficiently solved using a stack. The stack will store pairs of (span, price), where span is the number of consecutive days the price was less than or equal to the current day's price. 

### Approach
1. **Initialize the StockSpanner**:
   - The `StockSpanner` class contains a stack to store the span and price.

2. **Process the Next Price**:
   - Initialize the span to 1 for the current day's price.
   - While the stack is not empty and the current price is greater than or equal to the price at the top of the stack, pop the stack and add the span of the popped price to the current span.
   - Push the current span and price onto the stack.
   - Return the current span.

### Time Complexity
O(n) for n calls to the `next` method, as each price is pushed and popped from the stack at most once.

### Space Complexity
O(n) for storing the stack elements.

### Code
"""

class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        span = 1
        while self.stack and price >= self.stack[-1][1]:
            span += self.stack.pop()[0]
        self.stack.append([span, price])
        return span
