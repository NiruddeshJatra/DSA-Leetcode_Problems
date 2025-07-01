# Time Complexity:
# - O(N), where N is the number of tokens in the input array.
# - We iterate through each token exactly once, and each stack operation (push/pop) takes O(1) time.

# Space Complexity:
# - O(N), for the stack that stores operands. In the worst case, all tokens are numbers before any operators.

# INTUITION:
# Reverse Polish Notation (RPN) is a postfix notation where operators come after their operands.
# This makes it perfect for stack-based evaluation because when we encounter an operator, 
# the operands we need are the most recent values we've seen (top of stack).
# 
# For example: "2 1 + 3 *" means ((2 + 1) * 3) = 9
# - Push 2, push 1
# - See '+': pop 1 and 2, compute 2+1=3, push 3  
# - Push 3
# - See '*': pop 3 and 3, compute 3*3=9, push 9
# 
# The stack naturally handles the order of operations since operators are applied immediately
# when encountered, and nested expressions are resolved from innermost to outermost.

# ALGO:
# 1. Initialize an empty stack to store operands
# 2. For each token in the input:
#    - If token is an operator (+, -, *, /):
#      a. Pop two operands from stack (second operand first, then first operand)
#      b. Apply the operator to the operands in correct order
#      c. Push the result back onto the stack
#    - If token is a number:
#      a. Convert to integer and push onto stack
# 3. After processing all tokens, the stack contains exactly one element (the final result)
# 4. Return the final result

from typing import List

class Solution:
   def evalRPN(self, tokens: List[str]) -> int:
       operandStack = []
       operators = {'+', '-', '*', '/'}

       for token in tokens:
           if token in operators:
               # Pop operands in reverse order (stack is LIFO)
               secondOperand = operandStack.pop()
               firstOperand = operandStack.pop()
               
               if token == '+':
                   result = firstOperand + secondOperand
               elif token == '-':
                   result = firstOperand - secondOperand
               elif token == '*':
                   result = firstOperand * secondOperand
               else:  # token == '/'
                   # Handle division with truncation towards zero
                   result = int(float(firstOperand) / secondOperand)
               
               operandStack.append(result)
           else:
               # Token is a number
               operandStack.append(int(token))

       return operandStack.pop()
