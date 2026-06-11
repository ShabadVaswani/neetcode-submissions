class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        visited = set()
        res = 0
        
        # Use a for loop for 'r' so it ALWAYS moves forward cleanly
        for r in range(len(s)):
            # 1. SHRINK LOOP: If s[r] is a duplicate, keep removing from left
            while s[r] in visited:
                visited.remove(s[l])
                l += 1
            
            # 2. Add the current character (now safe)
            visited.add(s[r])
            
            # 3. Update result
            res = max(res, r - l + 1)
            
        return res