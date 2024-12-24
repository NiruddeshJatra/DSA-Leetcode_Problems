# Time Complexity:
# - O(N + T log T), where N is the number of tasks and T is the number of unique tasks.
#   - Building the frequency counter takes O(N).
#   - Each push/pop operation on the heap takes O(log T), and we perform these operations at most N times.

# Space Complexity:
# - O(T), where T is the number of unique tasks.
#   - The heap and the queue both store at most T elements.

# INTUITION:
# The goal is to schedule tasks in a way that respects the cooldown period `n` while minimizing the total time required.
# Using a max-heap, we always execute the most frequent task available, ensuring optimal scheduling.

# ALGO:
# 1. Count the frequency of each task using `Counter`.
# 2. Push the negative of the frequencies into a max-heap (to simulate a max-heap using Python's min-heap).
# 3. Use a queue (`nextTasks`) to keep track of tasks that are on cooldown, storing their remaining count and the time when they can be re-added to the heap.
# 4. For each unit of time:
#    - If the heap is non-empty, execute the most frequent task.
#    - If the task still has remaining occurrences, add it to the cooldown queue with its cooldown time.
#    - Check if any tasks in the cooldown queue can be re-added to the heap (i.e., their cooldown period is over).
# 5. Continue until both the heap and the cooldown queue are empty.
# 6. Return the total time elapsed.

import heapq
from collections import Counter, deque
from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)  # Count the frequency of each task
        heap = []
        for count in freq.values():
            heapq.heappush(heap, -count)  # Use negative values to simulate a max-heap

        nextTasks = deque()  # Queue to track tasks on cooldown
        time = 0  # Total time elapsed

        # Process tasks
        while heap or nextTasks:
            time += 1

            # If the heap is not empty, execute the most frequent task
            if heap:
                count = heapq.heappop(heap) + 1  # Execute task (-1 because heap stores negative counts)
                if count:  # If the task has remaining occurrences
                    nextTasks.append((count, time + n))  # Add it to the cooldown queue

            # Check if any tasks in the cooldown queue can be re-added to the heap
            if nextTasks and time == nextTasks[0][1]:
                heapq.heappush(heap, nextTasks.popleft()[0])  # Re-add task to the heap

        return time
