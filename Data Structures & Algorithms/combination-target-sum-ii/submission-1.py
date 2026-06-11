class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        bktrk = []
        candidates.sort()
        print(candidates)
        def dfs(startindex, currsum):
            if currsum >= target or startindex > len(candidates):
                if currsum == target:
                    res.append(bktrk[:])
                return
    
            for i in range(startindex, len(candidates)):
                if i > startindex and candidates[i] == candidates[i-1]:
                    continue
                print(bktrk)
                bktrk.append(candidates[i])
                dfs( i + 1, currsum+candidates[i])
                bktrk.pop(-1)
            return
            
        dfs(0, 0)

        return res
