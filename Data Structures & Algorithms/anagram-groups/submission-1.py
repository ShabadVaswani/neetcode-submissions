class Solution:
    def giveHashmap(self, strs: List[str]) -> List[List[str]]:
        HashMap = [0]*26
        for i in strs:
            HashMap[ord(i)-ord('a')] +=1
        return HashMap
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ctrDict = {}
        
        for i in strs:
            splt = [*i];
            HashMap = tuple(self.giveHashmap(splt))
            if HashMap in ctrDict:
                ctrDict[HashMap].append(i)
            else:
                ctrDict[HashMap] = [i]

            
        l = []
        for i in ctrDict.keys():
            l.append(ctrDict[i])
        return l

    
