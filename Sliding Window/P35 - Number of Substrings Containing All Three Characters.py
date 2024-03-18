# Time Complexity: O(n)
# Space Complexity: O(1)

# INTUITION:
# This method counts the number of substrings containing all three characters 'a', 'b', and 'c' in a given string 's'.

# ALGO:
# 1. Initialize variables: left pointer 'l', answer 'ans', and target dictionary 'target' with initial counts for 'a', 'b', and 'c'.
# 2. Iterate through the string:
#    2.1 Decrease the count of the current character in the target dictionary.
#    2.2 If the count of the current character reaches 0, decrement the target length.
#    2.3 While the target length is 0:
#        2.3.1 Increment the substring count.
#        2.3.2 Increase the count of the leftmost character.
#        2.3.3 If the count of the leftmost character becomes 1 again, increment the target length.
#        2.3.4 Move the left pointer 'l' to the right.
#    2.4 Add the substring count to the answer.
# 3. Return the answer.

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        target = {'a': 1, 'b': 1, 'c': 1}
        l, ans, targetLen = 0, 0, 3
        subarrCount = 0
        for r in range(len(s)):
            target[s[r]] -= 1
            if target[s[r]] == 0:
                targetLen -= 1

            while targetLen == 0:
                subarrCount += 1
                target[s[l]] += 1
                if target[s[l]] == 1:
                    targetLen += 1
                l += 1

            ans += subarrCount

        return ans
