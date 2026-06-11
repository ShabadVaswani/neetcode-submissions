class Solution:
    def isHappy(self, n: int) -> bool:
        sqrs = set()
        print(n)
        while n != 1 and n not in sqrs :
            sqrs.add(n)
            n = sum(int(i)*int(i) for i in str(n))
        print(sqrs)
        return n==1
