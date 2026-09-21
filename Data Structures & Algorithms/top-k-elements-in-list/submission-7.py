from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = defaultdict(int)
        for i in nums:
            freqs[i] += 1
        
        sorteditems = dict(sorted(freqs.items(), key=lambda item: item[1], reverse=True))
        # print(sorteditems)
        return list(sorteditems.keys())[:k]