from collections import Counter, defaultdict
from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = defaultdict(list)
        for string in strs:
            group_id = tuple(sorted(Counter(string).items()))
            dict[group_id].append(string)
        return list(dict.values())