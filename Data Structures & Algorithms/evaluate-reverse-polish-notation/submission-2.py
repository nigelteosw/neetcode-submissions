class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i == "+":
                first = stack.pop()
                second = stack.pop()
                stack.append(int(second) + int(first))
            elif i == "-":
                first = stack.pop()
                second = stack.pop()
                stack.append(int(second) - int(first))
            elif i == "*":
                first = stack.pop()
                second = stack.pop()
                stack.append(int(second) * int(first))
            elif i == "/":
                first = stack.pop()
                second = stack.pop()
                stack.append(int(second) / int(first))
            else:
                stack.append(i)
        return int(stack[-1])