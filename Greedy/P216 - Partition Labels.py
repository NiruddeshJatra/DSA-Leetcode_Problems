# Time Complexity:
# - O(n), where `n` is the length of the string `s`.
#   - The first pass to record the last occurrence of each character takes O(n).
#   - The second pass to calculate partition lengths also takes O(n).

# Space Complexity:
# - O(1) (excluding the output list), as the `last` dictionary contains at most 26 entries (for each letter in the English alphabet).

# INTUITION:
# To partition the string into as many parts as possible where each letter appears in only one part, we:
# 1. Determine the last occurrence of each character in the string.
# 2. Iterate through the string and maintain a "current partition end" (`end`).
#    - Whenever the current index reaches `end`, we have a complete partition.

# ALGO:
# 1. Use a dictionary to store the last occurrence index of each character.
# 2. Initialize `start` and `end` to mark the current partition's bounds.
# 3. Iterate through the string:
#    - Update `end` to the furthest last occurrence of any character seen so far.
#    - If the current index equals `end`, append the partition size to the result and reset `start`.
# 4. Return the list of partition sizes.

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # Step 1: Record the last occurrence of each character
        last = {}
        for i, c in enumerate(s):
            last[c] = i

        # Step 2: Initialize variables
        start = end = 0
        ans = []

        # Step 3: Iterate through the string
        for i, c in enumerate(s):
            end = max(end, last[c])  # Extend the partition to include the last occurrence of `c`
            if i == end:  # Partition boundary is reached
                ans.append(end - start + 1)  # Append the size of the current partition
                start = end + 1  # Update the start for the next partition

        return ans
