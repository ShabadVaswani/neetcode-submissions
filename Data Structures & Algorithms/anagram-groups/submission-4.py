class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashDictionary = defaultdict(list)
        for s in strs: 
            stringHash = [0]*26
            for char in s: 
                stringHash[ord(char)-ord('a')] +=1
            stringHash = tuple(stringHash)
            hashDictionary[stringHash].append(s)
            
        
        return list(hashDictionary.values())