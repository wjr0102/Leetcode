'''
    粗暴实现
'''
class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.tweets = []
        self.follows = {}
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        if userId not in self.follows:
            self.follows[userId] = {userId}
        self.tweets.append((tweetId,userId))
        

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        if userId not in self.follows:
            return []
        i = len(self.tweets) - 1
        j = 0
        res = []
        while i>=0 and len(res)<10:
            tweet = self.tweets[i]
            # print(tweet)
            # print(type(tweet))
            if tweet[1] in self.follows[userId]:
                res.append(tweet[0])
            i -= 1
        return res
        

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId not in self.follows:
            self.follows[followerId] = {followerId}

        self.follows[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId == followeeId:
            return
        if followerId in self.follows:
            if followeeId in self.follows[followerId]:
                self.follows[followerId].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)