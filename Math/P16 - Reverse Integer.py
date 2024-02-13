class Solution:
    def reverse(self, x: int) -> int:
       
        if x < 0:
            negative = True
        else:
            negative = False
        
        reversed = int(str(abs(x))[::-1])
        
        if reversed>(2**31-1) or reversed<-2**31:
                return 0
        
        if negative:
            return reversed*(-1)
        return reversed
