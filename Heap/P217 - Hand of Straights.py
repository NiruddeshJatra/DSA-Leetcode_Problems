# Time Complexity:
# - O(n log n), where `n` is the length of the `hand`.
#   - Building the min-heap takes O(n log n).
#   - Iterating through the elements and maintaining the heap also takes O(n log n).

# Space Complexity:
# - O(n) due to the `freq` dictionary and the heap.

# INTUITION:
# To determine if we can divide the hand into groups of `groupSize` consecutive integers:
# 1. Count the frequency of each card in the hand.
# 2. Use a min-heap to always work with the smallest available card.
# 3. Start from the smallest card and try to form groups of size `groupSize` by consuming the cards in consecutive order.
# 4. If at any point a card needed to complete a group is unavailable, return `False`.

# ALGO:
# 1. Count the frequency of each card using `Counter`.
# 2. Initialize a min-heap with the keys of the frequency dictionary.
# 3. While there are cards left in the frequency dictionary:
#    - Attempt to form a group starting with the smallest card.
#    - Decrease the count of each card in the group; if any card runs out, remove it from the frequency dictionary and heap.
#    - If a group cannot be formed, return `False`.
# 4. If all cards are used up successfully, return `True`.

import heapq
from collections import Counter
from typing import List

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # Step 1: Count the frequency of each card
        freq = Counter(hand)

        # Step 2: Initialize a min-heap with unique cards
        heap = list(freq.keys())
        heapq.heapify(heap)

        # Step 3: Try to form groups
        while heap:
            curVal = heap[0]  # Start with the smallest card
            for _ in range(groupSize):
                if curVal not in freq:
                    return False  # Cannot form a group
                freq[curVal] -= 1
                if freq[curVal] == 0:
                    del freq[curVal]
                    if curVal == heap[0]:
                        heapq.heappop(heap)
                curVal += 1  # Move to the next card in the group

        # Step 4: If all groups are formed, return True
        return True
