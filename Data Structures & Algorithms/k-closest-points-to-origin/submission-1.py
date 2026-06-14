import math 

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points_v1 = []
        for pt in points:
            dist = math.sqrt((pt[0] - 0)**2 + (pt[1] - 0)**2)
            points_v1.append([dist, pt])
        print(points_v1)
        heapq.heapify(points_v1)
        ret = []
        while k > 0:
            val = heapq.heappop(points_v1)
            ret.append(val[1])
            k -= 1

        print(ret)
        return ret