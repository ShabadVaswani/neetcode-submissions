class Solution:
    def operations(self, num1, num2, operator):
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            result = int(num1/num2)
            
                
        return result

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i in {'+', '-', '*', '/'}:
                num2 = stack.pop()
                num1 = stack.pop()
                operation = i
                print(num1, num2, operation)
                stack.append(self.operations(num1, num2, operation))
            else:
                stack.append(int(i))
            
        return stack[0]



