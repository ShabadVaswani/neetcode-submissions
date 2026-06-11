class MedianFinder:

    def __init__(self):
        self.maxHeap = []
        heapq.heapify(self.maxHeap)
        self.minHeap = []
        heapq.heapify(self.minHeap)

    def addNum(self, num: int) -> None:
        heapq.heappush(self.minHeap, num)

        if len(self.minHeap) >= 1 and len(self.maxHeap) >= 1:
            if self.minHeap[0] < -self.maxHeap[0]: # largest of smaller greater than smallest of larger            
                heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap)) # pop from larger add to smaller
        if abs(len(self.minHeap) - len(self.maxHeap)) > 1:
            if len(self.minHeap) > len(self.maxHeap): # len of larger elements greater than smaller
                heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap)) # pop from larger add to smaller
            else:
                heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap)) # pop from smaller add to larger

        

        

    def findMedian(self) -> float:
        print(self.maxHeap, self.minHeap)
        if len(self.minHeap) == len(self.maxHeap):
            return ((self.minHeap[0]-self.maxHeap[0])/2)
        elif len(self.minHeap) < len(self.maxHeap):
            return -self.maxHeap[0]
        else:
            return self.minHeap[0]
        