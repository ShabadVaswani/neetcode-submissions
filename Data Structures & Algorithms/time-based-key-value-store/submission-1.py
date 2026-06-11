class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.store.keys(): self.store[key].append([value, timestamp])
        else:
            self.store[key] = [[value, timestamp]]

    def get(self, key: str, timestamp: int) -> str:
        if key in self.store.keys():
            ls = self.store[key]
        else:
            return ""
        print(ls)
        l, r = 0, len(ls)-1
        res = ""
        while l <= r:
            mid = (l+r)//2
            print(res)
            midval = ls[mid][1]
            if midval <= timestamp:
                res = ls[mid][0]
            if timestamp < midval:
                r = mid - 1
            else:
                l = mid + 1

        return res
        
