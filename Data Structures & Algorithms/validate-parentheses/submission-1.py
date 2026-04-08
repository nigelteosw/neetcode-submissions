class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {')': '(', ']': '[', '}': '{'}
        stack = []
        for i in s:
            if i in mapping.values():
                stack.append(i)
            else:
                if not stack:
                    return False
                last = stack.pop()
                if not (last == mapping[i]):
                    return False
                
        return True if not stack else False