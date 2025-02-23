# Time Complexity:
# - O(N) where N is length of input string
# - Combination calculation takes O(1) as it's bounded by small modulos
# - Final digit calculation is linear scan of string

# Space Complexity:
# - O(N) to store coefficients array
# - O(1) for CRT lookup table
# - O(1) for remaining variables

# INTUITION:
# Instead of repeatedly adding and taking modulo which takes O(N²), we can:
# 1. Use binomial theorem to express final digits as linear combination of input digits
# 2. Apply Chinese Remainder Theorem (CRT) for mod 10 calculations
# 3. Pre-calculate coefficients using combinations modulo 2 and 5
#
# Example:
# For "12345" after 3 steps to get "99":
# - Each final digit can be expressed as weighted sum of input digits
# - Weights are determined by how many paths reach that position
# - Using CRT avoids explicit addition chains

# ALGO:
# 1. If string length is 2, directly compare digits
# 2. Otherwise:
#    - Calculate number of steps needed (n-2)
#    - Compute combination values modulo 2 and 5
#    - Use CRT lookup to get mod 10 coefficients
#    - Calculate final two digits using coefficient array
#    - Compare digits for equality

class Solution:
   def hasSameDigits(self, inputString: str) -> bool:
       stringLength = len(inputString)
       
       # Base case: already 2 digits
       if stringLength == 2:
           return inputString[0] == inputString[1]
           
       numSteps = stringLength - 2
       
       def calculateModuloCombination(n: int, k: int, modulo: int) -> int:
           """Calculate C(n,k) mod p using Lucas theorem"""
           result = 1
           while n > 0 or k > 0:
               nMod, kMod = n % modulo, k % modulo
               if kMod > nMod:
                   return 0
                   
               numerator = denominator = 1
               for i in range(kMod):
                   numerator = numerator * (nMod - i) % modulo
                   denominator = denominator * (i + 1) % modulo
                   
               result = result * numerator * pow(denominator, modulo-2, modulo) % modulo
               n //= modulo
               k //= modulo
           return result
       
       # CRT lookup table for mod 10 values
       crtTable = {
           (0,0):0, (0,1):6, (0,2):2, (0,3):8, (0,4):4,
           (1,0):5, (1,1):1, (1,2):7, (1,3):3, (1,4):9
       }
       
       # Calculate mod 10 coefficients using CRT
       coefficients = []
       for i in range(numSteps + 1):
           mod2Value = calculateModuloCombination(numSteps, i, 2)
           mod5Value = calculateModuloCombination(numSteps, i, 5)
           coefficients.append(crtTable[(mod2Value, mod5Value % 5)])
       
       # Calculate final digits using coefficients
       firstDigit = sum(int(digit) * coefficients[i] % 10 
                       for i, digit in enumerate(inputString[:numSteps+1])) % 10
       secondDigit = sum(int(digit) * coefficients[i] % 10 
                        for i, digit in enumerate(inputString[1:numSteps+2])) % 10
       
       return firstDigit == secondDigit
