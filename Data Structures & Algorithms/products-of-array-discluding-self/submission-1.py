class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        uptillNow = [1]
        future = [1]
        for i in nums:
            uptillNow.append(uptillNow[-1]*i)
        #uptillNow = uptillNow[1:]
        print(uptillNow)
        for i in nums[::-1]:
            future.append(future[-1]*i)
        #future = future[1:][::-1]
        future = future[::-1]
        res = []
        for i in range(len(nums)):
            print(nums[i], future[i+1], uptillNow[i])
            res.append(future[i+1]*uptillNow[i])
        return res
