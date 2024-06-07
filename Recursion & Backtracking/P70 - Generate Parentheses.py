# Time Complexity: O((4^n) / sqrt(n))
# Space Complexity: O((4^n) / sqrt(n)) due to the recursion stack and the space required to store the output.

# INTUITION:
# The goal is to generate all combinations of well-formed parentheses. To achieve this, we can use a backtracking approach. 
# We start with an empty string and keep adding open and close parentheses while maintaining the count of open and close 
# parentheses used. We can add an open parenthesis if we haven't reached the limit of `n`. We can add a close parenthesis if 
# the count of close parentheses is less than the count of open parentheses. This ensures that the parentheses are well-formed. 
# We continue this process until we have added `n` open and `n` close parentheses.

# ALGO:
# 1. Initialize an empty list `temp` to keep track of the current combination and an empty list `ans` to store the valid combinations.
# 2. Define a backtrack function that takes `open` and `close` as arguments representing the count of open and close 
#    parentheses used so far.
#     2.1 If the count of open and close parentheses both reach `n`, join the `temp` list into a string and append it to `ans`.
#     2.2 If the count of open parentheses is less than `n`, append an open parenthesis to `temp`, call the backtrack function 
#         with incremented open count, and then remove the last character from `temp`.
#     2.3 If the count of close parentheses is less than the count of open parentheses, append a close parenthesis to `temp`, 
#         call the backtrack function with incremented close count, and then remove the last character from `temp`.
# 3. Call the backtrack function with initial counts of open and close parentheses set to 0.
# 4. Return the list `ans` containing all the valid combinations.

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        temp = [] 
        ans = []

        def backtrack(open, close):
            if open == close == n:
                ans.append("".join(temp))
                return
            
            if open < n:
                temp.append("(")
                backtrack(open + 1, close)
                temp.pop()

            if close < open:
                temp.append(")")
                backtrack(open, close + 1)
                temp.pop()

        backtrack(0, 0)
        return ans
