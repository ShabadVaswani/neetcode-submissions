class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = digits[::-1]
        
        carry = 1
        for i in range(len(digits)):
            
            
            if carry:
                if digits[i] == 9:
                    digits[i] = 0
                    carry = 1
                else:
                    digits[i]+=1
                    carry = 0
        if carry: digits.append(1)
        return digits[::-1]

        