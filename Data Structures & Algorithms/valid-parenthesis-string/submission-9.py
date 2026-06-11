class Solution:
    def checkValidString(self, s: str) -> bool:
        maxi, mini = 0, 0
        for i in s:
            if i == '(':
                maxi += 1
                mini += 1
            if i == '*':
                mini -= 1
                maxi += 1
            if i == ')':
                mini -= 1
                maxi -= 1
            if maxi < 0:
                return False
            if mini < 0:
                mini = 0
        if mini > 0:
            return False
        return True