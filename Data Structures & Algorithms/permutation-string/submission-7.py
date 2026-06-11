class Solution:
    def matchUpdate(self, before, after):
        
        if before == True:
            return -1
        else:
            return +1
    def ordi(self,s):
        return ord(s)-ord('a')
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        hashone, hashtwo = [0] * 26, [0] * 26
        matches = 0

        for i in range(len(s1)):
            hashone[ord(s1[i]) - ord('a')]+=1
            hashtwo[ord(s2[i]) - ord('a')]+=1

        for i in range(len(hashone)):
            if hashone[i] == hashtwo[i]:
                matches += 1
        if matches == 26:
            return True

        l, r = 0, len(s1)-1
        while r < len(s2)-1:
            # adding element
            print(self.ordi(s2[r]), s2[l], s2[r], matches)
            r+=1 #jump
            print(s2[r])
            before = hashone[self.ordi(s2[r])] == hashtwo[self.ordi(s2[r])]
            hashtwo[self.ordi(s2[r])] += 1 # add
            after = hashone[self.ordi(s2[r])] == hashtwo[self.ordi(s2[r])]
            print('adba', before, after)

            if before != after:
                matches += self.matchUpdate(before, after)

            # removing element
            before = hashone[self.ordi(s2[l])] == hashtwo[self.ordi(s2[l])]
            hashtwo[self.ordi(s2[l])] -= 1 # remove

            after = hashone[self.ordi(s2[l])] == hashtwo[self.ordi(s2[l])]
            l+=1 # jump
            print('remba', before, after)
            if before != after:
                matches += self.matchUpdate(before, after)
            
            if matches == 26:
                return True

        
        return False