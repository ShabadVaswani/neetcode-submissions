class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(bktrk, ls, cursum):
            if ls[0] > target or cursum > target:
                return
            
            if cursum == target:
                res.append(bktrk)
                return

            for i in range(len(ls)):
                dfs(bktrk + [ls[i]], ls[i:], cursum+ls[i])
            return 
        dfs([], nums, 0)


        return res