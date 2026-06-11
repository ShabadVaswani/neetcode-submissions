class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dicti = {}
        for i in nums:
            dicti[i] = 1 + dicti.get(i, 0)

        listi = [[] for i in range(len(nums)+1)]

        for n, c in dicti.items():
            listi[c].append(n)
        soln = []
        for i in range(len(listi)-1,0,-1):
            for j in listi[i]:
                if k == 0: return soln
                soln.append(j)
                k-=1
        if k == 0: return soln

        