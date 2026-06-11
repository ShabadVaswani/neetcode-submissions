class Solution:
    def getSum(self, a: int, b: int) -> int:
        k = 32
        while b and k:
            k-=1
            a, b = (a^b), (a & b) << 1
        if k==0:
            return a&0xFFFFFFFF
        return a