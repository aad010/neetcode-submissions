class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        arr = list(zip(timestamp, username, website))
        arr.sort()

        collector = defaultdict(list)

        for time, user, web in arr:
            collector[user].append(web)
        
        patternCounter = defaultdict(int)

        for user in collector:
            vals = collector[user]
            patterns = set()
            for i in range(len(vals)):
                for j in range(i + 1, len(vals)):
                    for k in range(j + 1, len(vals)):
                        patterns.add((vals[i], vals[j], vals[k]))
            for p in patterns:
                patternCounter[p] += 1
        
        res = 0
        currPattern = tuple()
        for p in patternCounter:
            if res < patternCounter[p] or (patternCounter[p] == res and p < currPattern):
                res = patternCounter[p]
                currPattern = p
        
        return list(currPattern)