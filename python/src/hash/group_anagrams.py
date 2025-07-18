from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count_to_values = defaultdict(list)
        for s in strs:
            # think of using array for string problem with character set limited
            # to lowercase English letters
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            count_to_values[tuple(count)].append(s)

        return list(count_to_values.values())

    def groupAnagrams2(self, strs: List[str]) -> List[List[str]]:
        str_to_values = defaultdict(list)

        for s in strs:
            key = "".join(sorted(s))
            str_to_values[key].append(s)

        return list(str_to_values.values())
