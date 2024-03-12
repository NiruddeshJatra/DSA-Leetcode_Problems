from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # Time Complexity: O(n)
        # Space Complexity: O(1) - Since the size of the counter dictionaries are fixed

        # INTUITION:
        # We use a sliding window approach where we maintain counters for both strings.
        # We start by initializing counters for the first 'k' characters of s and p.
        # Then, as we slide the window, we update the counters accordingly.
        # If at any point the counters match, we have found an anagram substring.

        # ALGO:
        # 1. Initialize the length of s (n) and p (k).
        # 2. If the length of p is greater than the length of s, there can be no anagrams, so return an empty list.
        # 3. Initialize counters for the first 'k' characters of s and p.
        # 4. If the counters for the initial windows match, add the starting index (0) to the answer list.
        # 5. Iterate through the rest of the string starting from index 'k':
        #     5.1 Update the counters for the current window by adding the new character and removing the first character.
        #     5.2 If the count for the removed character becomes zero, remove it from the counter.
        #     5.3 If the updated counters match the counters for p, add the starting index of the current window to the answer list.
        # 6. Return the answer list containing starting indices of anagram substrings.

        n, k = len(s), len(p)  # Length of s and p
        if k > n:  # If length of p is greater than length of s, return empty list
            return []

        sCount, pCount = Counter(s[:k]), Counter(p)  # Counters for first 'k' characters of s and p
        ans = [0] if sCount == pCount else []  # Initialize answer list with 0 if first window is an anagram, else empty list

        for i in range(k, n):  # Loop through the rest of the string starting from index 'k'
            sCount[s[i]] = 1 + sCount.get(s[i], 0)  # Update counter for new character
            sCount[s[i - k]] -= 1  # Update counter for removed character

            if sCount[s[i - k]] == 0:  # If count becomes zero, remove character from counter
                sCount.pop(s[i - k])

            if sCount == pCount:  # If counters match, add starting index of current window to answer list
                ans.append(i - k + 1)

        return ans  # Return list of starting indices of anagram substrings
