class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = sorted(stones)
        while len(stones) >= 2:
            stones = sorted(stones)
            first, second = stones.pop(), stones.pop()
            if first == second:
                continue
            elif first > second:
                stones.append(first - second)
            else:
                stones.append(second - first)
        return 0 if not stones else stones[0]