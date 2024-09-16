# Time Complexity: O(n), where n is the length of the `bills` array. We loop through the `bills` array exactly once, performing constant-time operations for each bill.
# Space Complexity: O(1), as we are only using a constant amount of extra space to track the number of $5 and $10 bills.

# INTUITION:
# The goal is to determine if it's possible to provide correct change to every customer in line. The customers pay with either $5, $10, or $20 bills, and the cashier must provide change using the $5 and $10 bills they have collected.
#
# **Key Insight**:
# - When the customer gives a $5 bill, no change is required.
# - When the customer gives a $10 bill, the cashier needs to give back one $5 bill.
# - When the customer gives a $20 bill, the cashier should ideally give back one $10 bill and one $5 bill. If that's not possible, they must give back three $5 bills.

# ALGO:
# 1. **Track the Number of $5 and $10 Bills**:
#    - Initialize two variables, `five` and `ten`, to keep track of the number of $5 and $10 bills we have in hand.
# 2. **Iterate Through the `bills` Array**:
#    - For each `bill` in `bills`:
#        - If the bill is $5, increment `five` since no change is required.
#        - If the bill is $10, check if we have a $5 bill to provide as change. If so, decrement `five` and increment `ten`. If not, return `False` since we can't provide change.
#        - If the bill is $20, first try to give one $10 bill and one $5 bill as change. If that's not possible, try to give three $5 bills. If neither is possible, return `False`.
# 3. **Return True**:
#    - If we successfully process all customers, return `True` since we could provide correct change in every case.

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        # Step 1: Initialize variables to track the number of $5 and $10 bills
        five, ten = 0, 0

        # Step 2: Iterate through each bill in the `bills` array
        for bill in bills:
            if bill == 5:
                # No change is required, just increment the count of $5 bills
                five += 1
            elif bill == 10:
                # Need to provide one $5 bill as change
                if five > 0:
                    five -= 1
                    ten += 1
                else:
                    return False  # Can't provide change
            else:
                # The customer gives a $20 bill, try to provide one $10 and one $5 as change
                if ten > 0 and five > 0:
                    ten -= 1
                    five -= 1
                elif five >= 3:
                    # If we can't provide a $10 bill, provide three $5 bills instead
                    five -= 3
                else:
                    return False  # Can't provide change

        # Step 3: Return True if we successfully gave change to all customers
        return True
