class Solution:
    def reverse(self, x: int) -> int:
        y = 0
        k = 10
        print(((2**31)-1)<1234236467)
        sign = x < 0
        x = -x if sign else x
        while x and k:
            k-=1
            y=(y*10)+(x%10)
            x//=10
            print(x, y)
        if y > ((2**31)-1):
            return 0
        if sign:
            return -y
        return y