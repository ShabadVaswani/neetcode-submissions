class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums)-1
        zeros = 0
        for i in range(len(nums)-2, -1, -1):
            print(nums[i])
            if nums[i] == 0 :
                 zeros+=1
                 continue
            if nums[i] > zeros:
                goal = i 
                zeros = 0
            else:
                zeros+=1
                if goal == nums[i]:
                    goal = goal - nums[i]
                    break
        return goal == 0