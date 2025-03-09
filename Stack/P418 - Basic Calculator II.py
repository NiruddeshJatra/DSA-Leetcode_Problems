# Time Complexity:
# - O(N), where N is the length of the input string s.
# - We iterate through the string once, and each operation (stack push, pop, etc.) takes O(1) time.

# Space Complexity:
# - O(N), where N is the length of the input string s.
# - In the worst case, our stack might need to store values for each character in the input string.

# INTUITION:
# This problem requires evaluating a basic calculator expression that can include numbers, +, -, *, /, (, and ).
# The key insight is to handle operations in the correct order of precedence:
# 1. First evaluate expressions within parentheses
# 2. Then handle multiplication and division from left to right
# 3. Finally handle addition and subtraction from left to right
#
# We use a stack to keep track of values and operations. When we encounter a closing parenthesis,
# we evaluate the expression within the parentheses and continue with the result.
#
# For example, with "2*(5+5*2)/3+(6/2+8)":
# - We first compute (5+5*2) = 5+10 = 15
# - Then 2*15/3 = 10
# - Then (6/2+8) = 3+8 = 11
# - Finally 10+11 = 21

# ALGO:
# 1. Initialize a stack, a current number, and a current sign (+, -, *, /).
# 2. Iterate through each character in the string (plus an additional '+' to handle the last number).
# 3. If the character is a digit, update the current number.
# 4. If the character is an operation or parenthesis:
#    a. Process the previous number based on the last sign.
#    b. For '(', push the current sign to the stack and reset.
#    c. For ')', calculate the value of the subexpression inside parentheses.
# 5. Return the sum of all values in the stack.

class Solution:
   def calculate(self, s: str) -> int:
       currentNum, stack, currentSign = 0, [], '+'
       s = s.replace(' ', '')  # Remove all whitespace
       
       def updateStack(num, operator):
           if operator == '+': 
               stack.append(num)
           elif operator == '-': 
               stack.append(-num)
           elif operator == '*': 
               stack.append(stack.pop() * num)
           elif operator == '/': 
               # Use int() to handle division toward zero as specified in the problem
               stack.append(int(stack.pop() / num))
       
       # Add a '+' at the end to handle the last number
       for char in s + '+':
           if char.isdigit():
               # Build multi-digit numbers
               currentNum = currentNum * 10 + int(char)
           elif char == '(':
               # Save the current sign before entering the parenthesis
               stack.append(currentSign)
               # Reset for the new sub-expression
               currentNum, currentSign = 0, '+'
           else:  # Operator or closing parenthesis
               # Process the last number with the previous sign
               updateStack(currentNum, currentSign)
               # Reset number and update sign for next iteration
               currentNum, currentSign = 0, char
               
               if char == ')':
                   # When closing a parenthesis, calculate the subexpression result
                   tempResult = 0
                   # Sum all values inside the parentheses
                   while isinstance(stack[-1], int):
                       tempResult += stack.pop()
                   
                   # Get the sign before the opening parenthesis
                   previousSign = stack.pop()
                   
                   # Apply this sign to the result of the parentheses expression
                   updateStack(tempResult, previousSign)
                   
                   # Reset for continuing evaluation
                   currentNum, currentSign = 0, '+'
       
       # Sum all values in the stack to get the final result
       return sum(stack)
