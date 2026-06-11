class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {')': '(', '}': '{', ']': '['}

        stack = []
        stack.append(s[0])
        s = s[1:]
        for i in s:
            print(i)
            if i in ['(', '{', '[']:
                stack.append(i)
            if i in [']', '}', ')']:
                if len(stack) == 0: return False 
                print('kk1')
                print('mapping[stack[-1]]',stack[-1])
                if mapping[i] == stack[-1]:
                    stack.pop()
                else: return False
            
        if len(stack) == 0: return True
        return False
            