# Time Complexity: O(n), where n is the length of the string s. 
# We iterate through the string once, performing constant time operations for each character.

# Space Complexity: O(1), as we are using a fixed-size dictionary to store the Roman numeral values.

# INTUITION:
# The idea is to iterate through the string and use a mapping of Roman numerals to their integer values. 
# If a smaller numeral appears before a larger numeral, it means we need to subtract it (e.g., IV = 4).

# ALGO:
# 1. Create a dictionary `m` to map Roman numeral characters to their corresponding integer values.
# 2. Initialize a variable `ans` to store the total integer value.
# 3. Iterate through each character in the string:
#    3.1 If the current numeral is less than the next numeral, subtract its value from `ans`.
#    3.2 Otherwise, add its value to `ans`.
# 4. Return the total value stored in `ans`.

class Solution:
    def romanToInt(self, s: str) -> int:
        m = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        ans = 0
        
        for i in range(len(s)):
            if i < len(s) - 1 and m[s[i]] < m[s[i+1]]:
                ans -= m[s[i]]
            else:
                ans += m[s[i]]
        
        return ans
