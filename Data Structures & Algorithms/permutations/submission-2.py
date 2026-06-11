class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        visited = [0] * 20
        bktrk = []
        print(visited)

        def dfs():
            if len(bktrk) == len(nums):
                res.append(bktrk[:])
                return
            for i in nums:
                if visited[i]:
                    continue
                visited[i]+=1
                bktrk.append(i)
                dfs()
                visited[i]-=1
                bktrk.pop(-1)

        dfs()
        return res