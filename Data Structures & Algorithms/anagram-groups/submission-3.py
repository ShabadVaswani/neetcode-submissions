class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sortedDictionary = {}
        for s in strs: 
            sortedString = "".join(sorted(list(s)))
            if sortedString in sortedDictionary:
                sortedDictionary[sortedString].append(s)
            else:
                sortedDictionary[sortedString] = [s]
            
        
        return list(sortedDictionary.values())