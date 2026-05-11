class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Solution One
        # counter = dict()
        # print(k)
        # for i in nums:
        #     if i in counter:
        #         counter[i] = counter[i] + 1
        #     else:
        #         counter[i] = 1
        
        # topKElemsArr = []

        # for key,v in counter.items():
        #     topKElemsArr.append([v,key])

        # topKElemsArr.sort()

        # resultArr = []
        # counter = 0

        # for i in range(len(topKElemsArr) - 1, -1, -1):
        #     resultArr.append(topKElemsArr[i][1])
        #     counter += 1

        #     if counter == k:
        #         print("YAY")
        #         break
        
        # return resultArr

        # Solution Two
        counter = dict()
        print(k)
        for i in nums:
            if i in counter:
                counter[i] = counter[i] + 1
            else:
                counter[i] = 1

        frequencyCounter = [[] for i in range(len(nums) + 1)]

        for key, value in counter.items():
            frequencyCounter[value].append(key)

        result = []
        for i in range(len(frequencyCounter) - 1, -1, -1):
            for j in frequencyCounter[i]:
                result.append(j)
                if len(result) == k:
                    return result   