from collections import Counter 

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # dic = {}
        # for i in nums:
        #     if i in dic:
        #         dic[i] += 1
        #     else:
        #         dic[i] = 1
        # print(dic)
        # sorted_data = list(dict(sorted(dic.items(), key=lambda item: item[1], reverse=True)))
        # fin = []
        # print(sorted_data)
        # for i in range(k):
        #     fin.append(sorted_data[i])
        # return fin

        freqs = Counter(nums)
        buckets = [[] for _ in range(len(nums)+1)]

        for num, freq in freqs.items():
            buckets[freq].append(num)
        # print(buckets)

        keles = []
        for freq in range(len(nums),0,-1):
            for num in buckets[freq]:
                keles.append(num)
            if len(keles) == k:
                return keles
        return keles