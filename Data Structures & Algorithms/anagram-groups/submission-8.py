class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {}
        for string in strs:
            group_id = tuple(sorted(Counter(string).items()))
            if group_id not in dict:
                dict[group_id] = []
            dict[group_id].append(string)
        return list(dict.values())