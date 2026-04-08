class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            alive = True

            while alive and stack and stack[-1] > 0 and a < 0:
                if abs(a) > stack[-1]:
                    stack.pop()
                elif abs(a) == stack[-1]:
                    stack.pop()
                    alive = False
                else:
                    alive = False

            if alive:
                stack.append(a)

        return stack