class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sortedIntervals = sorted([i for i in intervals])
        output = [sortedIntervals[0]]

        for start, end in sortedIntervals:
            lastEnd = output[-1][1]

            if start <= lastEnd: 
                output[-1][1] = max(lastEnd, end)
            else:
                output.append([start, end])
        
        return output