class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastindex = defaultdict(lambda: 0)
        for i, val in enumerate(s):
            lastindex[val] = i
        maxlast  = 0
        size = 0
        res = []
        for i, val in enumerate(s):
            maxlast = max(maxlast, lastindex[val])
            print(maxlast, i)
            size+=1
            if maxlast <= i:
                res.append(size)
                size = 0
        return res