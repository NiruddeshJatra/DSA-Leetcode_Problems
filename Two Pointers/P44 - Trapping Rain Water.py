# Time Complexity: O(n)
# Space Complexity: O(1)

# INTUITION:
# This function calculates the total amount of water that can be trapped between the bars in the array 'height'.
# It uses a helper function 'helper' to compute the amount of water trapped within a subarray where the leftmost 
# bar is higher than the rightmost bar. It iterates through each subarray and calculates the trapped water by 
# considering the difference in height between the leftmost bar and the bars to its right.

# ALGORITHM:
# 1. Define a helper function 'helper' to calculate the trapped water within a subarray:
#    1.1 Initialize pointers 'l' and 'r' at indices 0 and 1 respectively.
#    1.2 Initialize 'ans' to 0 to store the total trapped water.
#    1.3 While 'l' is less than the length of 'subHeight' and 'r' is within the bounds of 'subHeight':
#        1.3.1 Initialize 'currentWidth' to 0.
#        1.3.2 While 'r' is within the bounds of 'subHeight' and the height at 'subHeight[r]' is less than 
#              the height at 'subHeight[l]':
#              1.3.2.1 Increment 'currentWidth' by the difference in height between 'subHeight[l]' and 
#                      'subHeight[r]'.
#              1.3.2.2 Increment 'r'.
#        1.3.3 If 'r' is within the bounds of 'subHeight' and 'currentWidth' is not 0:
#              1.3.3.1 Add 'currentWidth' to 'ans'.
#              1.3.3.2 Update 'l' to 'r'.
#              1.3.3.3 Increment 'r' by 1.
#        1.3.4 Otherwise, increment both 'l' and 'r' by 1.
#    1.4 Return a list containing 'ans' and 'l - 1'.
# 2. Call the 'helper' function with 'height' as input and store the result in 'res'.
# 3. Initialize 'water' to the first element of 'res'.
# 4. If 'res[1]' is not equal to 'len(height) - 2':
#    4.1 Call the 'helper' function with the reverse of the subarray starting from index 'res[1]' and store 
#        the result in 'res2'.
#    4.2 Add the first element of 'res2' to 'water'.
# 5. Return 'water', which represents the total amount of trapped water.

class Solution:
    def trap(self, height: List[int]) -> int:
        def helper(subHeight):
            l, r = 0, 1
            ans = 0
            while l < len(subHeight) and r < len(subHeight):
                currentWidth = 0
                
                while r < len(subHeight) and subHeight[r] < subHeight[l]:
                    currentWidth += (subHeight[l] - subHeight[r])
                    r += 1
                
                if r < len(subHeight) and currentWidth != 0:
                    ans += currentWidth
                    l = r
                    r = l + 1
                else:
                    l += 1
                    r += 1
                    
            return [ans, l - 1]
        
        res = helper(height)
        water = res[0]
        if res[1] != len(height) - 2:
            res2 = helper(height[res[1]:][::-1])
            water += res2[0]
            
        return water
