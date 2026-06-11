class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        listofints = 0
        def strtoint(s):
            return ord(s)-ord('0')
        for i, v1 in enumerate(num1[::-1]):

            for j, v2 in enumerate(num2[::-1]):
                print(v1,v2,10**i)
                listofints+=strtoint(v2)*strtoint(v1)*(10**i)*(10**j)


        return str(listofints)