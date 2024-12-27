# Time Complexity:
# - postTweet: O(1), appending a new tweet to the user's list.
# - getNewsFeed: O(k log k), where k is the total number of tweets among the user's followees (bounded by the heap size).
# - follow: O(1), adding a followee to the set.
# - unfollow: O(1), removing a followee from the set.

# Space Complexity:
# - O(u + t), where u is the number of users (storing followers) and t is the total number of tweets.

# INTUITION:
# A simple Twitter model involves:
# 1. Users being able to post tweets, which are stored with timestamps.
# 2. Users being able to follow and unfollow other users.
# 3. A feed that retrieves the 10 most recent tweets from a user and their followees.

# ALGO:
# 1. Maintain a `tweets` dictionary to store tweets by user, along with a timestamp for ordering.
# 2. Use a `followed` dictionary to store the follow relationships as sets.
# 3. Use a min-heap in `getNewsFeed` to efficiently retrieve the most recent 10 tweets across all followees.

from collections import defaultdict
import heapq
from typing import List

class Twitter:

    def __init__(self):
        self.count = 0  # Global timestamp to track tweet order
        self.tweets = defaultdict(list)  # Stores tweets for each user
        self.followed = defaultdict(set)  # Stores follow relationships

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Add a new tweet for the given user.
        """
        self.tweets[userId].append([self.count, tweetId])  # Append tweet with a timestamp
        self.count -= 1  # Decrement count to maintain the order

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweets from the user and their followees.
        """
        res = []
        heap = []

        # Add the user to their own follow list (self-follow)
        self.followed[userId].add(userId)

        # Push the most recent tweet of each followee into the heap
        for followeeId in self.followed[userId]:
            if followeeId in self.tweets:
                index = len(self.tweets[followeeId]) - 1
                count, tweetId = self.tweets[followeeId][index]
                heap.append([count, tweetId, followeeId, index - 1])
        heapq.heapify(heap)

        # Extract the 10 most recent tweets
        while heap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(heap)
            res.append(tweetId)
            if index >= 0:  # Add the next tweet of the same followee to the heap
                count, tweetId = self.tweets[followeeId][index]
                heapq.heappush(heap, [count, tweetId, followeeId, index - 1])

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follow a user.
        """
        self.followed[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Unfollow a user.
        """
        if followeeId in self.followed[followerId]:
            self.followed[followerId].remove(followeeId)

# Example Usage:
# obj = Twitter()
# obj.postTweet(userId, tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId, followeeId)
# obj.unfollow(followerId, followeeId)
