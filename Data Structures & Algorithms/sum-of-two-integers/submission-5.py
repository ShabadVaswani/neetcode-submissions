class Solution:
    def getSum(self, a: int, b: int) -> int:
        mx, mn = max(a, b), min(a, b)
        if mn > 0 or  mx < 0:
            flag = mn < 0 and mx < 0
            if flag:
                mx, mn = -mn, -mx
            pw = 0
            res = 0
            carry = 0
            while mx or carry:
                if mx%2 ==1 and mn %2 == 1:
                    if carry == 1:
                        res|=1*2**pw
                    carry = 1
                elif mx%2 ==0 and mn %2 == 0:
                    if carry == 1:
                        res|=1*2**pw
                        carry = 0
                elif mx%2 ==1 or mn %2 == 1:
                    if carry == 0:
                        res|=1*2**pw
                    else:
                        carry = 1
                mx = mx >> 1
                mn = mn >> 1

                pw +=1
            if flag:
                return -res
            return res
        else:
            nsign = abs(mn) > mx 
            mx, mn = max(abs(mn), mx), min(abs(mn), mx)
            pw = 0
            res = 0
            carry = 0
            while mx:
                if carry == 0:
                    if mx%2 < mn%2:
                        carry = 1
                    res|=(mx%2 ^ mn%2)*2**pw
                if carry == 1:
                    print(1, mx%2, mn%2, res)
                    if mx%2 > mn%2:
                        carry = 0
                    res|=(int(mx%2 == mn%2))*2**pw


                mx = mx >> 1
                mn = mn >> 1

                pw +=1
            if nsign:
                return -res
            return res