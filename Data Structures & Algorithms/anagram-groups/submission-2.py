class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for s in strs:
            hmap = [0]*26
            for i in s:
                hmap[ord(i) - ord('a')] += 1
            d[tuple(hmap)].append(s)
        return d.values()

    
