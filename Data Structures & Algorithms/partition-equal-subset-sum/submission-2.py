class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        mem = set()
        res = False if sum(nums)%2 == 1 else sum(nums)/2
        if not res:
            return False
        def dfs(i):
            if i >= len(nums):
                return False
            tempmem = mem.copy()
            if nums[i] == res:
                return True
            for adn in tempmem:
                print(adn + nums[i] )
                if adn + nums[i] == res:
                    return True
                mem.add(adn+nums[i])
            mem.add(nums[i])
            return dfs(i+1)
        
        return dfs(0)

