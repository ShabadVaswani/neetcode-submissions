class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        x = set(nums)
        d1 = collections.defaultdict(set)
        for i in nums:
            if i in x:
                if i-1 in x:
                    continue
                d1[i] = 1
                if i + 1 in x:
                    k = i +1
                    d1[i] = 1
                    while k in x:
                        d1[i]+=1
                        k+=1
        return max(d1.values())



