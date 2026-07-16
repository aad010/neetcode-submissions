class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        print(intervals)
        res = [intervals[0]]

        for i in range(1, len(intervals)):
            if intervals[i][0] <= res[-1][1]:
                val = res.pop()
                res.append([val[0], max(val[1], intervals[i][1])])
                print(res)
            else:
                res.append(intervals[i])

        return res