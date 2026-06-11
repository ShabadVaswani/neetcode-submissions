class Solution:
    def reverse(self, x: int) -> int:
        y = 0
        k = 9
        print(((2**31)-1))
        pfn = ((2**31)-1)//10
        sign = 1 if x < 0 else 0
        x = -x if sign else x
        while x and k:
            k-=1
            y=(y*10)+(x%10)
            x//=10
            print(x, y)
        if k == 0 and x > 0:
            if pfn < y or (pfn == y and x > (((2**31)-1)//9)%10):
                return 0
            else:
                k-=1
                y=(y*10)+(x%10)
                x//=10
        if y > ((2**31)-1):
            return 0
        if sign:
            return -y
        return y