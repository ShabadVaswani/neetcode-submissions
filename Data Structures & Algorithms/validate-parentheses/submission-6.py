class Solution:
    def isValid(self, s: str) -> bool:
        st = list(s)
        stack = []
        openings = ['(', '[', '{']
        closings =  [')',']','}']
        for i in st:
            if i in openings:
                stack.append(i)
            elif stack and i in closings:
                if stack[-1] == '(' and i ==')':
                    stack.pop()
                    continue
                elif stack[-1] == '[' and i ==']':
                    stack.pop()
                    continue
                elif stack[-1] == '{' and i =='}':
                    stack.pop()
                    continue
                else:
                    return False
            else:
                return False
        if stack:
            return False
        return True
                

            