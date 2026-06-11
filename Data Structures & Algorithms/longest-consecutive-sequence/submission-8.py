class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        st = set(nums)
        maxLen = 0
        for i in st:
            curLen = 0
            k = i
            if k+1 in st:
                continue
            while k in st:
                k=k-1
                curLen = curLen + 1
            if curLen>maxLen:
                maxLen = curLen

        return maxLen
            