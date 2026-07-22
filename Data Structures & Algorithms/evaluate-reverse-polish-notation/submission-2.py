class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands = ['+', '-', '*', '/']
        stack = []
        result = 0
        for tok in tokens:
            if tok not in operands:
                stack.append(tok)
            elif tok in operands:
                operand_2 = int(stack.pop())
                operand_1 = int(stack.pop())
                if tok == '+':
                    result = operand_1 + operand_2
                elif tok == '-':
                    result = operand_1 - operand_2
                elif tok == '*':
                    result = operand_1 * operand_2
                else:
                    result = operand_1 / operand_2
                stack.append(result)
        print(stack)  
        return int(stack[0])         