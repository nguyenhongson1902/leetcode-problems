# Design Twitter
# https://leetcode.com/problems/design-twitter/

from typing import List
import heapq


class Twitter:

    def __init__(self):
        self.users = {}
        self.followers = {}
        self.time = 1

    def postTweet(self, userId: int, tweetId: int) -> None: # O(1)
        if userId not in self.users:
            self.users[userId] = set()
            self.users[userId].add((-self.time, tweetId))
        else:
            self.users[userId].add((-self.time, tweetId))
        
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        followers = self.followers[userId] if userId in self.followers else set() # followers of userId
        # print("self.users", self.users)
        tweets = self.users[userId] if userId in self.users else set() # tweets of userId
        # print("tweets", tweets)
        all_tweets = []
        for tweet in tweets:
            all_tweets.append(tweet)
        # print("all_tweets", all_tweets)
        for follower_id in followers:
            all_tweets += list(self.users[follower_id]) if follower_id in self.users else []

        heapq.heapify(all_tweets) # O(n), n = len(all_tweets)

        result = []
        while all_tweets and len(result) < 10:
            time, tweet_id = heapq.heappop(all_tweets)
            result.append(tweet_id)

        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followers:
            self.followers[followerId] = set()
            self.followers[followerId].add(followeeId)
        else:
            self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        followers = self.followers[followerId] if followerId in self.followers else set()
        if followeeId in followers:
            self.followers[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)