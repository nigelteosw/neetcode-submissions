class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for i in range(len(operations)):
            curr = operations[i]
            if curr == '+':
                a = stack.pop()
                b = stack.pop()
                res = int(a) + int(b)
                stack.append(b)
                stack.append(a)
                stack.append(str(res))
            elif curr == 'C':
                stack.pop()
            elif curr == 'D':
                a = stack.pop()
                res = int(a) * 2
                stack.append(a)
                stack.append(str(res))
            else:
                stack.append(curr)
        return sum([int(i) for i in stack])