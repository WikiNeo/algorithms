import heapq
from collections import defaultdict
from typing import List


class Twitter:
    def __init__(self):
        self.count = 0  # count will be used as key for heap
        self.followMap = defaultdict(set)   # follow/unfollow O(1) with set
        self.tweetMap = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1 # we decrease the value here to use it for minHeap to get latest tweet

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []

        self.followMap[userId].add(userId)  # follow self to get 10 tweets from self and followee
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap: # we only process if the followee(self) has tweet
                index = len(self.tweetMap[followeeId]) - 1  # get the last index
                count, tweetId = self.tweetMap[followeeId][index]
                # add data to heap, index - 1 for prev tweet
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])

        while minHeap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(minHeap)  # get data from heap
            res.append(tweetId)
            if index >= 0:  # do further process if we are not out of bound
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
