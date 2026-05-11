class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numsDict = dict() 
        for i in nums:
            numsDict[i] = numsDict.get(i, 0) + 1
            numsCount = [[] for i in range(len(nums))]

        for key, v in numsDict.items():
            numsCount[v - 1].append(key)
        kFreqElems = []
        print(numsCount)
        for i in range(len(numsCount) - 1, -1, -1):
            values = numsCount[i]
            if len(values) > 0:
                for i in range(len(values) - 1, -1, -1):
                    kFreqElems.append(values[i])
                    k -= 1
                    print(values[i], k)
                    if k == 0:
                        return kFreqElems
            if k == 0:
                break
        return kFreqElems