class Solution:

    def encode(self, strs: List[str]) -> str:
        
        enc = ''
        for x in range(len(strs)):
            l = str(len(strs[x]))
            enc = enc + l + '*'
            enc = enc + strs[x]
            
        print(enc)
        return enc
        


    def decode(self, s: str) -> List[str]:
        
        i = 0
        itemList = []
        while i < len(s):
            num = ''
            while s[i] != '*':
                num += s[i]
                i+=1
            i+=1
            item = ''
            num = int(num)
            while num:
                item += s[i] 
                i+=1
                num-=1
            itemList.append(item)
        print(itemList)
        return itemList
            

