# Time Complexity: O(n)
# Space Complexity: O(n)

# INTUITION
# As keypads can be remapped, which means that the 8 most frequently used letters can be typed by a single push of a button, the 8 second most frequent letters can be typed by two pushes, and so on. Therefore, we can design the algorithm based on this feature.

# ALGO
# 1. CREATE a dictionary that stores the frequency of each letter
# 2. SORT the dictionary based on the number of frequencies from high to low
# 3. INITIALIZE button_push to 1 and minimum_pushes to 0
# 4. FOR EACH frequency IN sorted_count_letters.values():
#    4.1 ADD frequency * button_push to minimum_pushes
#    4.2 UPDATE button_push to 1after every 8th iteration
# 5. RETURN minimum_pushes
 

from collections import Counter


class Solution:
    def minimumPushes(self, word: str) -> int:
        countLetters = Counter(word)
        sortedCountLetters = dict(
            sorted(countLetters.items(), key=lambda item: item[1], reverse=True)
        )
        buttonPush, minimumPushes = 1, 0
        i = 1
        for freq in sortedCountLetters.values():
            minimumPushes += freq * buttonPush
            i += 1
            if i > 8:
                i = 1
                buttonPush += 1
        return minimumPushes
