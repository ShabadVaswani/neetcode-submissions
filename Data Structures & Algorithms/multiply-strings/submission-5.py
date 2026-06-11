class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        listofints = ["0"]*(len(num1)+len(num2))
        def strtoint(s):
            return ord(s)-ord('0')
        for i, v1 in enumerate(num1[::-1]):

            carry = '0'
            for j, v2 in enumerate(num2[::-1]):
                
                newint = strtoint(v1)*strtoint(v2)
                oldint = strtoint(listofints[i+j])
                ans = str((newint+oldint)+strtoint(carry))
                print(ans, v1, v2, carry, oldint, newint)
                if len(ans) > 1:
                    carry = ans[0]
                    ans = ans[1]
                else:
                    carry = str(0)
                listofints[i+j] = ans
            print(listofints)
            if carry: 
                listofints[i+j+1] = str(carry)
                carry = 0
        listofints=listofints[::-1]
        res = listofints
        for i in range(len(listofints)):
            if listofints[i] == '0':
                res=res[1:]
            else:
                break



        return str("".join(res))