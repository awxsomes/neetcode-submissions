from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grps = defaultdict(list)
        # dict(letters: count) : List(strs)
        for i in strs:
            count = [0] * 26
            for j in i:
                count[ord(j) - ord('a')] += 1
            grps[tuple(count)].append(i)
            # print(grps)
        return list(grps.values())