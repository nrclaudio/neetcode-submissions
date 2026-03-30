class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen_anagram = {}
        for i, string in enumerate(strs):
            if tuple(sorted(string)) not in seen_anagram.keys():
                seen_anagram[tuple(sorted(string))] = [i]
            else:
                seen_anagram[tuple(sorted(string))].append(i)
        result=[]
        for k, v in seen_anagram.items():
            within_list = []
            for value in v:
                within_list.append(strs[value])
            result.append(within_list)
        return result