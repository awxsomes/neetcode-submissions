class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        # {sortedword: index}
        for i in range(len(strs)):
            word = "".join(sorted(strs[i]))
            if word in dic:
                dic[word].append(strs[i])
            else:
                dic[word] = [strs[i]]
        print(dic)
        finallist =[]
        for key, value in dic.items():
            finallist.append(value)

        return finallist