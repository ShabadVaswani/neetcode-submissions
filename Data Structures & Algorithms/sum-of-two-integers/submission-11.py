class Solution:
    def getSum(self, a: int, b: int) -> int:
        k = 32
        while b and k:
            k-=1
            xr = (a^b)
            ad = (a & b) << 1
            print(a, b)
            b = ad
            a = xr
        if k==0:
            return a&0xFFFFFFFF
        return a