class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
                return 0
        q = collections.deque()
        q.append((0, nums[0]))
        jump  = 0
        while q:
            for k in range(len(q)):
                index, val = q.popleft()
                for j in range(1, val+1):
                    newIndex = index+j
                    print(val, newIndex)
                    if newIndex == len(nums)-1:
                        return jump+1
                    if (newIndex, nums[newIndex]) not in q:
                        q.append((newIndex, nums[newIndex]))
            jump += 1
        return jump