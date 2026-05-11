class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        '''
            given 2-d array (points) where points[i] = [xi, yi] reps 
            coordinates of a point on an X-Y axis plane

            also given integer k

            return k closest points to origin (0, 0)

            ex: points = [[0,2],[2,2]], k = 1

            sqrt((0-0)^2 + (2-0)^2) = sqrt(0 + 4) = 2
            sqrt((2-0)^2 + (2-0)^2) = sqrt(4+4) = 2.82
            minheap: 2

            2
          2.82
        '''
        distances = []
        for x, y in points:
            distance = ((x - 0)**2 + (y - 0)**2)
            distances.append([distance, x, y])
        
        result = []
        heapq.heapify(distances)
        while k > 0:
            distance, x, y = heapq.heappop(distances)
            result.append([x,y])
            k -= 1
        return result