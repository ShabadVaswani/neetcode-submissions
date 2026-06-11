class Twitter:

    def __init__(self):
        self.posts = defaultdict(list)
        self.following = defaultdict(set)
        self.timer = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts[userId].append((-self.timer, tweetId))
        print("str worked")
        self.timer = self.timer+1

    def getNewsFeed(self, userId: int) -> List[int]:
        if len(self.posts[userId]) <= 10:
            followingpostlist = [self.posts[userId][:]]
        else:
            followingpostlist = [self.posts[userId][-10:]]
        for user in self.following[userId]:

            if len(self.posts[user]) <= 10:
                followingpostlist.append(self.posts[user][:])
            else:
                followingpostlist.append(self.posts[user][-10:])
        print(followingpostlist)
        heap = []
        res = []
        for i in range(10):
            for l in followingpostlist:
                if len(l) > 0:
                    heapq.heappush(heap, l.pop())
            if heapq:
                #res.append(heapq.heappop(heap)[0])
                if heap:
                    #print(heapq.heappop(heap))
                    res.append(heapq.heappop(heap)[1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        if followeeId not in self.following[followerId]:
            return
        self.following[followerId].remove(followeeId)
        
