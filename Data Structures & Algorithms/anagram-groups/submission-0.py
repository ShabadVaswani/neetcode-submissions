class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ctrDict = {}
        for i in strs:
            if tuple(sorted(i)) in ctrDict:
                ctrDict[tuple(sorted(i))].append(i)
            else:
                ctrDict[tuple(sorted(i))] = [i]
        l = []
        for i in ctrDict.keys():
            l.append(ctrDict[i])
        return l
