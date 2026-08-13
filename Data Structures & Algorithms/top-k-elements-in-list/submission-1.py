class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for i in nums:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        print(dic)
        sorted_data = list(dict(sorted(dic.items(), key=lambda item: item[1], reverse=True)))
        fin = []
        print(sorted_data)
        for i in range(k):
            fin.append(sorted_data[i])
        return fin