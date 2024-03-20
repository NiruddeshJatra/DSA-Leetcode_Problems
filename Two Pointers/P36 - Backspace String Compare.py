# Time Complexity: O(n)
# Space Complexity: O(1)

# INTUITION:
# This function compares two strings 's' and 't' after applying backspace rules ('#' character). It iterates through 
# both strings simultaneously, adjusting the pointers according to the backspace rules. If the resulting characters 
# at the pointers are not equal, or if one pointer reaches the end while the other doesn't, it returns False; otherwise, 
# it returns True.

# ALGORITHM:
# 1. Initialize pointers 'p1' and 'p2' at the end of strings 's' and 't' respectively.
# 2. Iterate through both strings simultaneously until at least one of the pointers reaches the beginning:
#    2.1 Count the number of backspaces encountered while iterating backwards in string 's' using 'backspace' variable.
#    2.2 Similarly, count the number of backspaces encountered while iterating backwards in string 't' using 'backspace' variable.
#    2.3 Compare characters at current pointers:
#        2.3.1 If both characters are not equal and neither is a backspace, return False.
#    2.4 If one pointer has reached the beginning while the other hasn't, return False.
#    2.5 Move both pointers backwards.
# 3. If the loop completes without returning False, return True.

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        p1, p2 = len(s)-1, len(t)-1
        
        while p1 >= 0 or p2 >= 0:
            backspace = 0
            while p1 >= 0:
                if s[p1] == "#":
                    backspace += 1
                    p1 -= 1
                elif backspace > 0:
                    backspace -= 1
                    p1 -= 1
                else:
                    break
                    
            backspace = 0
            while p2 >= 0:
                if t[p2] == "#":
                    backspace += 1
                    p2 -= 1
                elif backspace > 0:
                    backspace -= 1
                    p2 -= 1
                else:
                    break
                    
            if p1 >= 0 and p2 >= 0 and s[p1] != t[p2]:
                return False
            
            if (p1 >= 0) != (p2 >=0):
                return False
            p1 -= 1
            p2 -= 1
            
        return True
