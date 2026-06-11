class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        farthest = 0
        current_window_end = 0
        jump = 0
        for i in range(len(nums)-1):
            farthest =max(farthest, nums[i]+i)
            print(current_window_end)
            if current_window_end == i:
                current_window_end = farthest
                jump+=1


        return jump
            