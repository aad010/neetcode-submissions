class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
            [1,2,2,3,3,3], k = 2
            {1: 1, 2: 2, 3: 3}
            [[],[1],[2],[3]]

           [3,2] 

        '''
        numsDict = defaultdict(int)
        for i in nums:
            numsDict[i] = numsDict[i] + 1
        
        numsArr = [[] for i in range(0, len(nums) + 1)]
        print(numsDict)

        for key, v in numsDict.items():
            numsArr[v].append(key)
        result = []
        print(numsArr)
        for i in range(len(nums), 0, -1):
            if len(numsArr[i]) > 0:
                arr = numsArr[i]
                print("before" + str(k))
                for j in range(len(arr) - 1, -1, -1): 
                    if k > 0:
                        result.append(arr[len(arr) - 1])
                        arr.pop()
                        k -= 1
                        print("after" + str(k))
                    elif k == 0:
                        break
            if k == 0: 
                break
        return result


    