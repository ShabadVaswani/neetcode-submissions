class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, acc, total):
            print(total, target)
            if total == target:
                res.append(acc.copy())
                return
            if i >= len(nums) or total > target:
                return

            acc.append(nums[i])
            dfs(i, acc, total+nums[i])
            acc.pop()
            dfs(i+1, acc, total)
        dfs(0, [], 0)
        return res