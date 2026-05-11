class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = defaultdict(int)
        count_arr = [[] for i in range(len(nums))]

        for num in nums:
            hm[num] = hm[num] + 1
        
        for key, v in hm.items():
            count_arr[v - 1].append(key)
        
        res = []
        for i in range(len(count_arr) - 1, -1, -1):
            if len(count_arr[i]) == 0:
                continue
            else:
                vals = count_arr[i]
                for j in range(len(vals) - 1, -1, -1):
                    res.append(vals[j])
                    k -= 1
                    if k == 0:
                        return res
                
