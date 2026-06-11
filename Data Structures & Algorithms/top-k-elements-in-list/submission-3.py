class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {}
        frequency = [[] for i in range(10001)]
        output = []
        k2 = int(k)
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for ke in count.keys():
            frequency[count[ke]].append(ke)
        for i in range(10000, 0, -1):
            if len(frequency[i])>0:
                output.extend(frequency[i])
                k2 = k2 - len(frequency[i])
                if k2 == 0:
                    break
        return output

