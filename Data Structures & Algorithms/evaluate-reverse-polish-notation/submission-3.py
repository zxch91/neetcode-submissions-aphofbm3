class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []

        for token in tokens:
            if token == '+':
                popped1 = stack.pop()
                popped2 = stack.pop()
                summed = popped1 + popped2
                stack.append(summed)
            elif token == '-':
                popped1 = stack.pop()
                popped2 = stack.pop()
                summed = popped2 - popped1
                stack.append(summed)
            elif token == '*':
                popped1 = stack.pop()
                popped2 = stack.pop()
                summed = popped1 * popped2
                stack.append(summed)
            elif token == '/':
                popped1 = stack.pop()
                popped2 = stack.pop()
                stack.append(int(popped2 / popped1))
            else:
                stack.append(int(token))
        return stack[-1]