class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hmap = defaultdict(int)

        for i in  hand:
            if i in hmap:
                hmap[i] += 1
            else:
                hmap[i] = 1
        k = list(hmap.keys())
        k.sort()
        while len(k)>0:
            if len(k)<groupSize:
                return False
            for i in range(groupSize):
                
                if i < groupSize-1 and k[i] +1 != k[i+1]:
                    return False                    
                hmap[k[i]] -= 1
                
                
            k = [i for i in k if hmap[i]!=0 ]
            
        return True
