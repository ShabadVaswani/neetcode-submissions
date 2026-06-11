class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)
        time = 0
        q = deque()

        while maxHeap or q:
            time+=1
            if maxHeap:
                current = heapq.heappop(maxHeap) + 1
                if current < 0:
                    q.append([current,time+n])

            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
            print

        return time