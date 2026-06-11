class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        print(nums)
        l, r2, r1 = 0, len(nums) - 2, len(nums) - 1
        res = []
        while l < len(nums):
            while l < r1:
                adn = nums[l] + nums[r2] + nums[r1]
                if adn == 0 and l!=r2:
                    print(l,r2,r1)
                    res.append([nums[l], nums[r2], nums[r1]])
                    r2 = r2-1
                    while r2 - 1 > l and nums[r2-1] == nums[r2]: r2-=1
                
                if r2 <= l:
                    r1 = r1 - 1
                    while r1 - 1 > l and nums[r1] == nums[r1+1]: 
                        r1-=1
                    r2 = r1-1
                else:
                    r2 = r2 -1
            
            while l + 1 < len(nums) and nums[l+1] == nums[l]: l+=1
            l+=1
            r1=len(nums)-1
            
            #while r1 - 1 > l and nums[r1] == nums[r1+1]: r1-=1
            r2=r1-1
        return res
