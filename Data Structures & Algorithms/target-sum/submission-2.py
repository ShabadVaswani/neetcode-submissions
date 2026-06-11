class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        mem = {}
        def dfs(i, cursum):
            if i == len(nums)-1:
                if nums[i] == abs(cursum-target) :
                    if -nums[i] == abs(cursum-target):
                        return 2
                    return 1
                else:
                    return 0
            if (i, cursum) in mem:
                return mem[(i,cursum)]
            paths = 0
            paths+=dfs(i+1, cursum+nums[i])
            paths+=dfs(i+1, cursum-nums[i])
            mem[(i,cursum)] = paths
            

            return paths

        return dfs(0,0)