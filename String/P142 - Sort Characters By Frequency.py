# Time Complexity: O(n), where n is the length of the string s. 
# Counting the frequency of characters and building the bucket both take linear time.

# Space Complexity: O(n), for storing the frequency count and the bucket list.

# INTUITION:
# The idea is to group characters by their frequencies and then construct the result
# by concatenating characters based on their frequency from highest to lowest. 

# ALGO:
# 1. Use a Counter to count the frequency of each character in the string.
# 2. Create a bucket (list of lists) where the index represents the frequency.
# 3. For each character, append it to the appropriate bucket based on its frequency.
# 4. Iterate over the bucket from the highest frequency to the lowest.
# 5. For each character in the bucket, append it to the result the number of times equal to its frequency.
# 6. Finally, return the concatenated string as the result.

class Solution:
    def frequencySort(self, s: str) -> str:
        cnt = Counter(s)
        bucket = [[] for _ in range(len(s) + 1)]
        for c, freq in cnt.items():
            bucket[freq].append(c)

        ans = []
        for freq in range(len(s), -1, -1):
            for c in bucket[freq]:
                ans.append(c * freq)

        return "".join(ans)
