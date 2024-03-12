from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Time Complexity: O(n)
        # Space Complexity: O(1) - Since the size of the counter dictionaries are fixed

        # INTUITION:
        # We use a sliding window approach where we maintain counters for both strings.
        # We start by initializing counters for the first 'k' characters of s2 and s1.
        # Then, as we slide the window, we update the counters accordingly.
        # If at any point the counters match, s1 is a permutation of a substring of s2.

        # ALGO:
        # 1. Initialize the length of s2 (n) and s1 (k).
        # 2. If the length of s1 is greater than the length of s2, s1 can't be a permutation of any substring of s2, so return False.
        # 3. Initialize counters for the first 'k' characters of s2 and s1.
        # 4. If the counters for the initial windows match, return True.
        # 5. Iterate through the rest of the string starting from index 'k':
        #     5.1 Update the counters for the current window by adding the new character and removing the first character.
        #     5.2 If the count for the removed character becomes zero, remove it from the counter.
        #     5.3 If the updated counters match the counters for s1, return True.
        # 6. If no permutation of s1 is found in s2, return False.

        n, k = len(s2), len(s1)  # Length of s2 and s1
        if k > n:  # If length of s1 is greater than length of s2, s1 can't be a permutation of any substring of s2
            return False

        s2Count, s1Count = Counter(s2[:k]), Counter(s1)  # Counters for first 'k' characters of s2 and s1
        if s2Count == s1Count:  # If counters match, s1 is a permutation of first 'k' characters of s2
            return True

        for i in range(k, n):  # Loop through the rest of the string starting from index 'k'
            s2Count[s2[i]] = 1 + s2Count.get(s2[i], 0)  # Update counter for new character
            s2Count[s2[i - k]] -= 1  # Update counter for removed character

            if s2Count[s2[i - k]] == 0:  # If count becomes zero, remove character from counter
                s2Count.pop(s2[i - k])

            if s2Count == s1Count:  # If counters match, s1 is a permutation of substring of s2
                return True

        return False  # No permutation of s1 found in s2, return False
