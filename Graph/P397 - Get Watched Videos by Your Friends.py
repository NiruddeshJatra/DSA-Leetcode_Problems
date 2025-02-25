# Time Complexity:
# - O(N + E + V * log V), where:
#   - N is the number of people
#   - E is the total number of friendship connections
#   - V is the total number of unique videos watched by friends at the target level
# - BFS takes O(N + E) time to traverse the friendship graph
# - Sorting the videos takes O(V * log V) time

# Space Complexity:
# - O(N + V), where:
#   - N is the space for the BFS queue and visited set
#   - V is the space for storing video frequency counts

# INTUITION:
# This problem can be broken down into two main steps:
# 1. Find all friends at exactly level K distance from the given person using BFS
# 2. Count the frequency of videos watched by these level-K friends and sort them accordingly
#
# BFS is ideal for finding nodes at a specific distance (level) from a starting node in a graph.
# We use a queue to keep track of friends and their distances from the starting person.
# Once we reach the target level, we collect all videos watched by those friends and count their frequencies.
# Finally, we sort the videos first by frequency (ascending) and then lexicographically.

# ALGO:
# 1. Initialize a BFS queue with the starting person and level 0
# 2. Process the queue until empty:
#    a. If current level matches target level, collect videos watched by this friend
#    b. Otherwise, add all unvisited friends of current person to the queue
# 3. Count the frequency of each video watched by level-K friends
# 4. Sort the videos by frequency (ascending) and then by name (lexicographically)
# 5. Return the sorted list of video names

from collections import deque, defaultdict

class Solution:
   def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
       # Initialize queue for BFS with [person_id, level]
       friendQueue = deque()
       friendQueue.append([id, 0])
       
       # Track visited people to avoid cycles
       visitedFriends = {id}
       
       # Dictionary to store video frequency counts
       videoFrequency = defaultdict(int)
       
       # BFS to find friends at exactly the target level
       while friendQueue:
           currentFriend, currentLevel = friendQueue.popleft()
           
           # If we've reached the target level, collect videos
           if currentLevel == level:
               for video in watchedVideos[currentFriend]:
                   videoFrequency[video] += 1
               continue
           
           # Add unvisited friends to the queue for next level
           for nextFriend in friends[currentFriend]:
               if nextFriend not in visitedFriends:
                   visitedFriends.add(nextFriend)
                   friendQueue.append([nextFriend, currentLevel + 1])
       
       # Sort videos by frequency and then lexicographically
       sortedVideos = sorted(videoFrequency.items(), key=lambda item: (item[1], item[0]))
       
       # Extract just the video names from the sorted list
       return [video for video, _ in sortedVideos]
