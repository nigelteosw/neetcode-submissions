class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time = []

        cars = sorted(list(zip(position, speed)), reverse=True)
        for car in cars:
            timeToReach = (target - car[0]) / car[1]
            time.append(timeToReach)
            if len(time) >= 2 and time[-1] <= time[-2]:
                time.pop()

        return len(time)