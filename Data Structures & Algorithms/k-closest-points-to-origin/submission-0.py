class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        heapq.heapify(distances)
        for x, y in points:
            dist = -(x ** 2 + y ** 2)
            heapq.heappush(distances, [dist, x, y])
            if len(distances) > k:
                heapq.heappop(distances)

        res = []
        for _, x, y in distances:
            res.append([x, y])

        return res